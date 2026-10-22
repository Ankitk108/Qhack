"""VQE for a three-term fermionic Hamiltonian mapped to six qubits."""

import pennylane as qp
import pennylane.numpy as np


w0 = qp.fermi.FermiWord({(0, 0): "-", (1, 0): "+"})
w1 = qp.fermi.FermiWord({(0, 1): "-", (1, 1): "+"})
w2 = qp.fermi.FermiWord({(0, 2): "-", (1, 2): "+"})


def build_hamiltonian(coeffs):
    """Build the real-coefficient Jordan–Wigner qubit Hamiltonian."""
    fermionic_hamiltonian = coeffs[0] * w0 + coeffs[1] * w1 + coeffs[2] * w2
    qubit_hamiltonian = qp.fermi.jordan_wigner(fermionic_hamiltonian)
    mapped_coeffs, pauli_words = qubit_hamiltonian.terms()
    real_coeffs = [float(np.real(coefficient)) for coefficient in mapped_coeffs]
    return qp.Hamiltonian(real_coeffs, pauli_words)


dev = qp.device("default.qubit", wires=6)


@qp.qnode(dev)
def vqe_circuit(params, coeffs):
    """Prepare a trial state and return its Hamiltonian expectation value."""
    for wire in range(3):
        qp.RY(params[wire], wires=wire)
    return qp.expval(build_hamiltonian(coeffs))


def optimization(coeffs):
    """Optimize the trial state and return the final ground-state estimate."""
    params = np.array(np.random.uniform(0.0, 2.0 * np.pi, 3), requires_grad=True)
    optimizer = qp.AdamOptimizer(stepsize=0.1)

    for _ in range(100):
        params = optimizer.step(lambda current: vqe_circuit(current, coeffs), params)

    return vqe_circuit(params, coeffs)

# Imports used by the original challenge grader.
import json
import pennylane as qp
import pennylane.numpy as np

# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    coeffs = json.loads(test_case_input)
    np.random.seed(40)
    output = optimization(coeffs)
    return str(output)


def check(solution_output: str, expected_output: str) -> None:
    solution_output = json.loads(solution_output)
    expected_output = json.loads(expected_output)
    assert abs(solution_output - expected_output) < 0.1


# These are the public test cases
test_cases = [("[-2,2,5]", "-2"), ("[7,6,-6]", "-6")]

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

