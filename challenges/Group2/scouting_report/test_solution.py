"""Tests for expval-only single-wire tomography."""

import pennylane as qp
import pytest

from .solution import bloch_and_purity


def test_rotated_single_qubit_public_case():
    def prep():
        qp.RY(0.6, wires=0)
        qp.RZ(1.3, wires=0)

    bloch, purity = bloch_and_purity(prep, 1, 0)
    assert bloch == pytest.approx(
        [0.151041200225, 0.544065877074, 0.82533561491], abs=1e-5
    )
    assert purity == pytest.approx(1.0, abs=1e-10)


def test_nonzero_target_wire_public_case():
    def prep():
        qp.RX(0.8, wires=0)
        qp.CRX(1.4, wires=[0, 1])

    bloch, purity = bloch_and_purity(prep, 2, 1)
    assert bloch == pytest.approx([0.0, -0.149440145691, 0.87412830171], abs=1e-5)
    assert purity == pytest.approx(0.893216322497, abs=1e-5)


@pytest.mark.parametrize("target_wire", [0, 1])
def test_bell_state_local_reduction_is_maximally_mixed(target_wire):
    def prep():
        qp.Hadamard(wires=0)
        qp.CNOT(wires=[0, 1])

    bloch, purity = bloch_and_purity(prep, 2, target_wire)
    assert bloch == pytest.approx([0.0, 0.0, 0.0], abs=1e-10)
    assert purity == pytest.approx(0.5, abs=1e-10)


def test_target_wire_in_larger_register_is_respected():
    def prep():
        qp.PauliX(wires=2)

    bloch, purity = bloch_and_purity(prep, 4, 2)
    assert bloch == pytest.approx([0.0, 0.0, -1.0], abs=1e-10)
    assert purity == pytest.approx(1.0, abs=1e-10)

