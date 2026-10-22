"""Quantum feature-state overlap kernel and pairwise kernel matrices."""

import pennylane as qp
import pennylane.numpy as np


WIRES = tuple(range(4))
dev = qp.device("default.qubit", wires=WIRES)


@qp.qnode(dev)
def quantum_kernel(x1, x2):
    """Return the squared overlap between two angle-embedded datapoints."""
    qp.AngleEmbedding(x1, wires=WIRES)
    qp.adjoint(qp.AngleEmbedding)(x2, wires=WIRES)
    return qp.expval(qp.Projector([0, 0, 0, 0], wires=WIRES))


def kernel_matrix(X1, X2):
    """Return all pairwise quantum-kernel values for two datasets."""
    values = np.array(
        [[quantum_kernel(x1, x2) for x2 in X2] for x1 in X1]
    )
    return values.reshape((len(X1), len(X2)))

# Imports used by the original challenge grader.
import json
import pennylane as qp
import pennylane.numpy as np

# These functions are responsible for testing the solution
def run(test_case_input: str) -> str:
    ins = json.loads(test_case_input)
    output = kernel_matrix(*ins)
    return output


def check(solution_output: str, expected_output: str) -> None:
    expected_output = json.loads(expected_output)
    assert np.allclose(solution_output.tolist(), expected_output, rtol=1e-4)


# These are the public test cases
test_cases = [
    (
        "[[[0.32058496, 0.07741205, 0.53200578, 0.91373749], "
        "[0.71838322, 0.45665254, 0.19871986, 0.1157332], "
        "[0.04515, 0.66228969, 0.69793587, 0.64664178]], "
        "[[0.32058496, 0.07741205, 0.53200578, 0.91373749], "
        "[0.71838322, 0.45665254, 0.19871986, 0.1157332], "
        "[0.04515, 0.66228969, 0.69793587, 0.64664178]]]",
        "[[1, 0.76528062, 0.87759179], [0.76528062, 1, 0.77075905], "
        "[0.87759179, 0.77075905, 1]]",
    ),
    (
        "[[[0.94727029, 0.40665627, 0.05521391, 0.06570142], "
        "[0.32897296, 0.89902984, 0.59060573, 0.11193315]], "
        "[[0.11815914, 0.47388796, 0.64337692, 0.59215516], "
        "[0.69635966, 0.65039949, 0.17727646, 0.76091743]]]",
        "[[0.71461545, 0.85406897], [0.89085434, 0.81902278]]",
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

