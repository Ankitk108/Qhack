import json
import pennylane as qp
import pennylane.numpy as np


def bloch_and_purity(prep, num_wires, target_wire):
    """Reconstruct one wire's Bloch vector using expectation values only."""
    dev = qp.device("default.qubit", wires=num_wires)

    def expectation_circuit(observable):
        @qp.qnode(dev)
        def circuit():
            prep()
            return qp.expval(observable(target_wire))

        return circuit

    measure_x = expectation_circuit(qp.PauliX)
    measure_y = expectation_circuit(qp.PauliY)
    measure_z = expectation_circuit(qp.PauliZ)

    bloch = [float(measure_x()), float(measure_y()), float(measure_z())]
    purity = float(0.5 * (1.0 + sum(component**2 for component in bloch)))
    return bloch, purity


# These functions are responsible for testing the solution.
def build_prep(gate_list):
    """Turn [gate_name, parameters, wires] entries into a preparation."""
    def prep():
        for name, parameters, wires in gate_list:
            getattr(qp, name)(*parameters, wires=wires)

    return prep


def run(test_case_input: str) -> str:
    case = json.loads(test_case_input)
    gate_list = case["gates"]
    target_wire = case["target_wire"]
    num_wires = 1 + max(max(wires) for _, _, wires in gate_list)
    bloch, purity = bloch_and_purity(
        build_prep(gate_list), num_wires, target_wire
    )
    return json.dumps([bloch, purity])


def check(solution_output: str, expected_output: str) -> None:
    got = json.loads(solution_output)
    expected = json.loads(expected_output)
    assert np.allclose(got[0], expected[0], atol=1e-5)
    assert np.isclose(got[1], expected[1], atol=1e-5)


# These are the public test cases
test_cases = [
    (
        '{"gates": [["RY", [0.6], [0]], ["RZ", [1.3], [0]]], '
        '"target_wire": 0}',
        "[[0.151041200225, 0.544065877074, 0.82533561491], 1.0]",
    ),
    (
        '{"gates": [["RX", [0.8], [0]], ["CRX", [1.4], [0, 1]]], '
        '"target_wire": 1}',
        "[[0.0, -0.149440145691, 0.87412830171], 0.893216322497]",
    ),
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

