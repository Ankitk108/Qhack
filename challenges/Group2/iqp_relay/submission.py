import json
import pennylane as qp
import pennylane.numpy as np

# Write any helper functions you need here


n_qubits = 4
dev = qp.device("default.qubit", wires=n_qubits)


@qp.qnode(dev)
def iqp_circuit(weights, pattern, observable):
    """Implement the IQP circuit and return its Pauli-Z-word expectation."""
    for parameter_index, rotation_group in enumerate(pattern):
        for wires in rotation_group:
            qp.PauliRot(
                weights[parameter_index],
                "X" * len(wires),
                wires=wires,
            )

    measured_wires = [wire for wire, bit in enumerate(observable) if bit]
    if measured_wires:
        measured_observable = qp.prod(
            *(qp.PauliZ(wire) for wire in measured_wires)
        )
    else:
        measured_observable = qp.Identity(0)
    return qp.expval(measured_observable)


def optimize_iqp(pattern, observable):
    """Return parameters minimizing the IQP cost."""
    if not any(observable):
        return np.zeros(len(pattern), requires_grad=True)

    for parameter_index, rotation_group in enumerate(pattern):
        anticommuting_factors = sum(
            observable[wire] for wires in rotation_group for wire in wires
        )
        if anticommuting_factors % 2 == 1:
            exact_weights = [0.0] * len(pattern)
            exact_weights[parameter_index] = np.pi
            return np.array(exact_weights, requires_grad=True)

    best_weights = None
    best_cost = float("inf")
    for initial_value in (0.3, 0.7, 1.1):
        weights = np.full(len(pattern), initial_value, requires_grad=True)
        optimizer = qp.AdamOptimizer(stepsize=0.1)
        for _ in range(200):
            weights = optimizer.step(
                lambda current: iqp_circuit(current, pattern, observable),
                weights,
            )
        cost = float(iqp_circuit(weights, pattern, observable))
        if cost < best_cost:
            best_cost = cost
            best_weights = weights

    return best_weights


# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    test_pattern, test_observable = json.loads(test_case_input)
    params = optimize_iqp(test_pattern, test_observable)
    cost = iqp_circuit(params, test_pattern, test_observable)
    weights = [0.3, -0.7, 0.2, 1.1]
    expval = iqp_circuit(weights, test_pattern, test_observable)
    return str([float(expval), float(cost)])


def check(solution_output: str, expected_output: str) -> None:
    solution_expval, solution_min = json.loads(solution_output)
    expected_expval, expected_min = json.loads(expected_output)

    params = [0.3, -0.7, 0.2, 1.1]
    test_pattern = [
        [[0], [1]],
        [[1, 2]],
        [[0, 2], [1, 3]],
        [[0, 1, 2, 3]],
    ]
    test_observable = [1, 0, 1, 0]
    names = list(
        qp.specs(iqp_circuit)(params, test_pattern, test_observable)["resources"]
        .gate_types.keys()
    )
    assert names.count("IQP") == 0
    assert np.allclose(solution_expval, expected_expval, atol=1e-3)
    assert np.allclose(solution_min, expected_min, atol=2e-2)


# These are the public test cases
test_cases = [
    (
        "[[[[0], [1]], [[1, 2]], [[0, 2], [1, 3]], "
        "[[0, 1, 2, 3]]], [1, 0, 1, 0]]",
        "[0.7306816499355087, -1]",
    ),
    (
        "[[[[0], [2]], [[1, 2, 3]], [[0, 1], [2, 3]], "
        "[[0, 1, 2]]], [1, 1, 0, 1]]",
        "[0.9362933635841989, -1]",
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

