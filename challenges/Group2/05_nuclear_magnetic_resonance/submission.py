"""Time evolution under a driven one-qubit NMR Hamiltonian."""

import jax.numpy as jnp
import pennylane as qp


dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def nmr_evolve(B0: float, B1: float, omega: float, time: float) -> "jnp.ndarray":
    """Evolve |0> under the NMR Hamiltonian and return basis probabilities."""
    if time == 0:
        return qp.probs(wires=0)

    coeffs = [
        B0,
        lambda parameter, t: parameter * jnp.cos(omega * t),
        lambda parameter, t: -parameter * jnp.sin(omega * t),
    ]
    ops = [qp.PauliZ(0), qp.PauliX(0), qp.PauliY(0)]
    hamiltonian = qp.dot(coeffs, ops)

    qp.evolve(hamiltonian)([B1, B1], t=[0.0, time])
    return qp.probs(wires=0)

# Imports used by the original challenge grader.
import json
import pennylane as qp
import pennylane.numpy as np

# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    ins = json.loads(test_case_input)
    output = nmr_evolve(*ins).tolist()
    return str(output)


def check(solution_output: str, expected_output: str) -> None:
    solution_output = json.loads(solution_output)
    expected_output = json.loads(expected_output)
    assert jnp.allclose(
        jnp.array(solution_output), jnp.array(expected_output), atol=0.03
    ), "Your code does not yield the correct probabilities"


# These are the public test cases
test_cases = [
    ("[1,2,0.5,0.3]", "[0.6962061524391174, 0.3037952184677124]"),
    ("[1, 1, 0.25, 0.6]", "[0.7278291583061218, 0.272170752286911]"),
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

