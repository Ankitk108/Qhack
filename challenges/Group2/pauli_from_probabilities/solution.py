"""Reconstruct Pauli-word expectation values from outcome probabilities."""

import pennylane as qp
import pennylane.numpy as np


def prepare(angles):
    """Prepare the challenge's fixed three-qubit state."""
    qp.RY(angles[0], wires=0)
    qp.RX(angles[1], wires=1)
    qp.RY(angles[2], wires=2)
    qp.CNOT(wires=[0, 1])
    qp.RZ(angles[3], wires=1)
    qp.CNOT(wires=[1, 2])
    qp.RX(angles[3], wires=0)


def measure_pauli_word(word, angles):
    """Measure a Pauli word using one probability circuit and classical parity."""
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

