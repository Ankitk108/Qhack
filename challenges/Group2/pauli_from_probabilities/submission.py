import json
import pennylane as qp
import pennylane.numpy as np


# A three-qubit state is prepared for you. You do not need to change this.
def prepare(angles):
    """Prepares the state whose Pauli expectation values you have to measure."""
    qp.RY(angles[0], wires=0)
    qp.RX(angles[1], wires=1)
    qp.RY(angles[2], wires=2)
    qp.CNOT(wires=[0, 1])
    qp.RZ(angles[3], wires=1)
    qp.CNOT(wires=[1, 2])
    qp.RX(angles[3], wires=0)


def measure_pauli_word(word, angles):
    """Measure a Pauli word using computational-basis probabilities only."""
    letter_to_basis = {"I": "none", "Z": "none", "X": "H", "Y": "SH"}
    basis = [letter_to_basis[letter] for letter in word]

    device = qp.device("default.qubit", wires=3)

    @qp.qnode(device)
    def probability_circuit():
        prepare(angles)
        for wire, change in enumerate(basis):
            if change == "H":
                qp.Hadamard(wires=wire)
            elif change == "SH":
                qp.adjoint(qp.S(wires=wire))
                qp.Hadamard(wires=wire)
        return qp.probs(wires=[0, 1, 2])

    probabilities = probability_circuit()
    carried_wires = [wire for wire, letter in enumerate(word) if letter != "I"]
    signs = [
        int((-1) ** sum((outcome >> (2 - wire)) & 1 for wire in carried_wires))
        for outcome in range(8)
    ]
    value = float(np.dot(np.array(signs), probabilities))
    return basis, signs, value


# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    word, angles = json.loads(test_case_input)
    basis, signs, value = measure_pauli_word(word, angles)
    return json.dumps([basis, signs, float(value)])


def check(solution_output: str, expected_output: str) -> None:
    got = json.loads(solution_output)
    expected = json.loads(expected_output)
    assert got[0] == expected[0]
    assert got[1] == expected[1]
    assert np.isclose(got[2], expected[2], rtol=0.0, atol=1e-6)


# These are the public test cases
test_cases = [
    (
        '["ZIZ", [0.79, 2.75, 2.89, 0.33]]',
        '[["none", "none", "none"], '
        "[1, -1, 1, -1, -1, 1, -1, 1], 0.931986472711103]",
    ),
    (
        '["XYI", [1.45, 0.22, 1.72, 1.4]]',
        '[["H", "SH", "none"], '
        "[1, 1, -1, -1, -1, -1, 1, 1], 0.9673999542626387]",
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

