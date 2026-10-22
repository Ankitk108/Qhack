"""Tests for the elementary four-qubit QFT implementation."""

import pennylane as qp
import pennylane.numpy as np

from .submission import qft_four_qubits


def circuit_operations():
    with qp.queuing.AnnotatedQueue() as queue:
        result = qft_four_qubits()
    return result, list(queue.queue)


def test_function_returns_nothing_and_uses_only_allowed_gates():
    result, operations = circuit_operations()
    assert result is None
    assert {operation.name for operation in operations} <= {
        "Hadamard",
        "ControlledPhaseShift",
        "SWAP",
    }


def test_has_complete_elementary_gate_pattern():
    _, operations = circuit_operations()
    names = [operation.name for operation in operations]
    assert names.count("Hadamard") == 4
    assert names.count("ControlledPhaseShift") == 6
    assert names.count("SWAP") == 2
    assert len(operations) == 12


def test_swap_network_corrects_wire_order():
    _, operations = circuit_operations()
    swaps = [tuple(operation.wires) for operation in operations if operation.name == "SWAP"]
    assert swaps == [(0, 3), (1, 2)]


def test_unitary_matches_pennylane_qft_including_phases():
    user_unitary = qp.matrix(qft_four_qubits, wire_order=range(4))()
    reference_unitary = qp.matrix(qp.QFT(wires=range(4)))
    assert np.allclose(user_unitary, reference_unitary, atol=1e-8)

