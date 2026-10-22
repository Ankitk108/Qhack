"""Single-qubit, single-layer quantum neural network."""

import json

import pennylane as qp
import pennylane.numpy as np


dev = qp.device("default.qubit", wires=1)


def training_circuit(theta_vec):
    """Apply the trainable RZ-RY-RZ block."""
    qp.RZ(theta_vec[0], wires=0)
    qp.RY(theta_vec[1], wires=0)
    qp.RZ(theta_vec[2], wires=0)


def encoding_circuit(x):
    """Encode one scalar as an RX rotation."""
    qp.RX(x, wires=0)


@qp.qnode(dev)
def quantum_neural_network(x, theta_vec):
    """Apply the encoding and trainable blocks and return Pauli-Z expectation."""
    encoding_circuit(x)
    training_circuit(theta_vec)
    return qp.expval(qp.PauliZ(wires=0))


def run(test_case_input: str) -> str:
    values = json.loads(test_case_input)
    return str(quantum_neural_network(values[0], values[1:]))


def check(solution_output: str, expected_output: str) -> None:
    assert np.isclose(
        json.loads(solution_output), json.loads(expected_output), rtol=1e-4
    )


test_cases = [
    ('[0.4859371, 1.32682562, -1.06015833, -4.41959946]', '0.827549'),
    ('[-0.72318627, -4.91395046, -5.0609724, 0.1125593]', '0.865457'),
]


if __name__ == "__main__":
    for index, (input_, expected) in enumerate(test_cases):
        print(f"Running test case {index} with input '{input_}'...")
        output = run(input_)
        check(output, expected)
        print("Correct!")
