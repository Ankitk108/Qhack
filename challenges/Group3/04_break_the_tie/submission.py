import json
import pennylane as qp
import pennylane.numpy as np

# Two helpers are given to you. You do not need to change either one.
def rotation_angle(fraction):
    """The RY angle that puts amplitude sqrt(fraction) on |1>.

    Args:
        fraction (float): a number in [0, 1].

    Returns:
        float: the angle theta with sin(theta / 2)**2 == fraction.
    """
    return float(2 * np.arcsin(np.sqrt(fraction)))

def run_circuit(num_wires, circuit):
    """Runs a circuit as an analytic QNode on a fresh default.qubit simulator.

    This exists so that you only have to write the circuit itself. There are no
    shots anywhere in this challenge, so every number that comes back is exact.

    Args:
        num_wires (int): the number of wires the circuit needs.
        circuit (callable): takes no arguments, applies operations, and returns a
            single measurement.

    Returns:
        list[float]: what the circuit measured, flattened into plain floats.
    """
    device = qp.device("default.qubit", wires=num_wires)
    return [float(value) for value in np.asarray(qp.QNode(circuit, device)()).ravel()]





def estimate_mean(probabilities, values, n):
    """Estimates the average of a quantity over a discrete distribution with
    amplitude estimation, resolving the two-fold ambiguity in the readout.

    Args:
        probabilities (list[float]): the probability of each outcome, summing to 1.
            Its length is a power of two, 2**m, where m is the number of data wires.
        values (list[float]): the value of the quantity at each outcome, all
            non-negative, same length as probabilities.
        n (int): the number of estimation wires.

    Returns:
        float: the estimated average of the quantity.
    """

    probabilities = np.array(probabilities, dtype=float)
    values = np.array(values, dtype=float)
    m = int(round(np.log2(len(probabilities))))     # number of data wires
    


    probabilities = np.array(probabilities, dtype=float)
    values = np.array(values, dtype=float)

    m = int(round(np.log2(len(probabilities))))
    f_max = float(np.max(values))

    # Rescale f into [0, 1].
    if f_max == 0.0:
        scaled_values = np.zeros_like(values)
    else:
        scaled_values = values / f_max

    data_wires = list(range(m))
    objective_wire = m

    target_wires = list(range(m + 1))
    estimation_wires = list(range(m + 1, m + 1 + n))

    # ------------------------------------------------------------------
    # Amplitude-estimation circuit
    # ------------------------------------------------------------------

    def scaled_function(index):
        return float(scaled_values[index])

    def amplitude_estimation_circuit():
        qp.QuantumMonteCarlo(
            probs=probabilities,
            func=scaled_function,
            target_wires=target_wires,
            estimation_wires=estimation_wires,
        )

        return qp.probs(wires=estimation_wires)

    estimation_probabilities = run_circuit(
        m + 1 + n,
        amplitude_estimation_circuit,
    )

    # Find one of the two mirror peaks.
    number_of_bins = 2**n
    peak_bin = int(np.argmax(estimation_probabilities))
    estimated_phase = peak_bin / number_of_bins

    # Convert that phase into the two ambiguous candidates a and 1-a.
    candidate_a = float(
        (1.0 - np.cos(np.pi * estimated_phase)) / 2.0
    )
    candidate_b = float(1.0 - candidate_a)

    # ------------------------------------------------------------------
    # Direct tie-breaker circuit
    # ------------------------------------------------------------------

    def tie_breaker_circuit():
        # StatePrep expects amplitudes, hence sqrt(probabilities).
        qp.StatePrep(
            np.sqrt(probabilities),
            wires=data_wires,
        )

        for outcome, fraction in enumerate(scaled_values):
            # PennyLane associates computational basis states with
            # big-endian bit strings in the specified wire order.
            binary_outcome = format(outcome, f"0{m}b")
            control_values = [
                int(bit) for bit in binary_outcome
            ]

            controlled_ry = qp.ctrl(
                qp.RY,
                control=data_wires,
                control_values=control_values,
            )

            controlled_ry(
                rotation_angle(float(fraction)),
                wires=objective_wire,
            )

        return qp.probs(wires=objective_wire)

    objective_probabilities = run_circuit(
        m + 1,
        tie_breaker_circuit,
    )

    direct_amplitude = float(objective_probabilities[1])

    # Pick the amplitude-estimation candidate closest to the direct result.
    if abs(candidate_a - direct_amplitude) <= abs(
        candidate_b - direct_amplitude
    ):
        selected_amplitude = candidate_a
    else:
        selected_amplitude = candidate_b

    return float(f_max * selected_amplitude)

# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    probabilities, values, n = json.loads(test_case_input)
    return json.dumps(float(estimate_mean(probabilities, values, n)))


def check(solution_output: str, expected_output: str) -> None:
    got = json.loads(solution_output)
    exp = json.loads(expected_output)
    assert np.isclose(got, exp, rtol=0.0, atol=1e-9), \
        "Wrong average. It has to be f_max times whichever of the two candidates " \
        "your tie-breaker picks out -- the amplitude-estimation estimate, not the " \
        "exact sum of p_i f_i, and not always the smaller of the two candidates."


# These are the public test cases
test_cases = [
    ('[[0.4008104395612045, 0.24310382032676792, 0.14744992052145606, 0.0894328975684541, 0.054243794362206846, 0.03290052437982574, 0.019955176756987287, 0.012103426523097706], [0.0, 0.25, 1.0, 2.25, 4.0, 6.25, 9.0, 12.25], 8]', '1.160949660702857'),
    ('[[0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125], [0.6, 0.7, 0.8, 0.9, 1.0, 1.0, 1.0, 1.0], 8]', '0.8745681972617296')
]

# This will run the public test cases locally
for i, (input_, expected_output) in enumerate(test_cases):
    print(f"Running test case {i} with input '{input_}'...")

    try:
        output = run(input_)

    except Exception as exc:
        print(f"Runtime Error. {exc}")

    else:
        if message := check(output, expected_output):
            print(f"Wrong Answer. Have: '{output}'. Want: '{expected_output}'.")

        else:
            print("Correct!")
