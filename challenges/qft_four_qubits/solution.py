"""Elementary-gate implementation of the four-qubit QFT."""

import math

import pennylane as qp


def qft_four_qubits():
    """Apply the four-qubit QFT without using PennyLane's QFT template."""
    for target in range(4):
        qp.Hadamard(wires=target)
        for control in range(target + 1, 4):
            angle = math.pi / (2 ** (control - target))
            qp.ControlledPhaseShift(angle, wires=[control, target])

    qp.SWAP(wires=[0, 3])
    qp.SWAP(wires=[1, 2])

