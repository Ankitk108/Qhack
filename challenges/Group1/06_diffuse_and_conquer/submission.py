"""Apply QSVT matrix inversion to one diffusion-reaction time step."""

import pennylane as qp
import pennylane.numpy as np


phi = np.array([0.03, 0.04, 0.07, 0.09])
source = np.array([1.0, 2.0, 1.0, 0.5])
dt = 0.01
h = 0.2

phi_qsvt = [
    -5.497787143782138,
    1.5707963267948966, 1.5707963267948966, 1.5707963267948966,
    1.5707963267948966, 1.5707963267948966, 1.5707963267948966,
    1.5707963267948966, 1.5707963267948966, 1.5707963267948966,
    1.5707963267948966, 1.5707963267948966, 1.5707963267948966,
    1.5707963267948966, 1.5707963267948968, 1.5707963267948963,
    1.5707963267948968, 1.5707963267948961, 1.5707963267948972,
    1.5707963267948957, 1.5707963267948977, 1.4728569598289858,
    1.663449244812472, 1.4844150925203923, 1.6496152611111905,
    1.4997920149429393, 1.6333707689488446, 1.5162790064498395,
    1.6171200864777835, 1.531874246110498, 1.6024345108599611,
    1.5454075127341322, 1.5901314304180914, 1.5563445410214334,
    1.5805114301199141, 1.5645466238299222, 1.5735916541136388,
    1.5699211382379552, 1.5698688162965302, 1.5706106116874756,
    1.5707839787248004, 0.7853981064335358,
]
C = 0.05

b = phi + dt * source

D2 = np.array(
    [
        [-2.0, 1.0, 0.0, 0.0],
        [1.0, -2.0, 1.0, 0.0],
        [0.0, 1.0, -2.0, 1.0],
        [0.0, 0.0, 1.0, -2.0],
    ]
) / h**2


def build_matrix(nu, k):
    """Return the backward-Euler diffusion-reaction matrix."""
    return (1.0 + k * dt) * np.eye(4) - nu * dt * D2


device = qp.device("default.qubit", wires=4)


@qp.qnode(device)
def qsvt_diffusion(nu, k):
    """Return a state containing the QSVT inverse branch in amplitudes 0–3."""
    matrix = build_matrix(nu, k)
    normalized_matrix = matrix / np.linalg.norm(matrix, ord=2)

    qp.StatePrep(b / np.linalg.norm(b), wires=[2, 3])
    qp.Hadamard(wires=0)

    def inverse_transform():
        block_encoding = qp.BlockEncode(normalized_matrix, wires=[1, 2, 3])
        projectors = [
            qp.PCPhase(angle, dim=4, wires=[1, 2, 3]) for angle in phi_qsvt
        ]
        qp.QSVT(block_encoding, projectors)

    qp.ctrl(inverse_transform, control=0, control_values=0)()
    qp.ctrl(qp.adjoint(inverse_transform), control=0, control_values=1)()
    qp.Hadamard(wires=0)
    return qp.state()

# Imports used by the original challenge grader.
import json
import pennylane as qp
import pennylane.numpy as np

# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    ins = json.loads(test_case_input)
    out_state = qsvt_diffusion(*ins)[:4]
    rescaled_out = out_state * np.linalg.norm(b) / C
    output = rescaled_out / np.linalg.norm(rescaled_out)

    return str(np.real(output).tolist())


def check(solution_output: str, expected_output: str) -> None:
    solution_output = json.loads(solution_output)
    expected_output = json.loads(expected_output)
    fidelity = np.dot(solution_output, expected_output)
    assert fidelity >= 0.99, "Your circuit doesn't look quite right "


# These are the public test cases
test_cases = [
    ("[0.2,0.5]", "[0.27959746, 0.42869397, 0.56892447, 0.64371709]"),
    ("[1.0, 1.2]", "[0.28550356, 0.4595721 , 0.59350887, 0.59584262]"),
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

