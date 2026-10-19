import json
import pennylane as qp
import pennylane.numpy as np

dev = qp.device("default.qubit", wires=3, shots=1)


@qp.qnode(dev)
def circuit(generator, oracle, diffuser):
    """Implement Grover search with one auxiliary qubit."""
    generator()

    qp.Hadamard(wires=2)
    qp.ctrl(oracle, control=2)()
    qp.Hadamard(wires=2)

    qp.ctrl(diffuser, control=2, control_values=0)(generator)
    return qp.counts(wires=[0, 1])


# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:

    # useful functions
    @qp.prod
    def generator():
        # Creates the uniform initial quantum state
        qp.Hadamard(0)
        qp.Hadamard(1)

    def oracle():
        # Creates an oracle that marks two out of the four possible quantum states
        if random == 0:
            qp.PauliZ(wires=0)
        elif random == 1:
            qp.PauliX(wires=0)
            qp.PauliZ(wires=0)
            qp.PauliX(wires=0)
        elif random == 2:
            qp.PauliZ(wires=1)
        else:
            qp.PauliX(wires=1)
            qp.PauliZ(wires=1)
            qp.PauliX(wires=1)

    def diffuser(generator):
        # Creates the diffuser that reflects the state over the initial state |psi>.
        qp.Reflection(generator())

    # private tests
    for _ in range(1000):
        random = np.random.randint(0, 3)
        result = circuit(generator, oracle, diffuser)
        if random == 0 and ("01" in result or "00" in result):
            return "Incorrect state"
        if random == 1 and ("10" in result or "11" in result):
            return "Incorrect state"
        if random == 2 and ("10" in result or "00" in result):
            return "Incorrect state"
        if random >= 3 and ("01" in result or "11" in result):
            return "Incorrect state"
    return "Correct state"


def check(solution_output: str, expected_output: str) -> None:
    assert solution_output == "Correct state", "Not the correct quantum state."


# These are the public test cases
test_cases = [("No input", "No output")]

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

