"""Tests for constructing and optimizing IQP circuits."""

import pennylane as qp
import pennylane.numpy as np
import pytest

from .solution import iqp_circuit, optimize_iqp


PUBLIC_CASES = [
    (
        [[[0], [1]], [[1, 2]], [[0, 2], [1, 3]], [[0, 1, 2, 3]]],
        [1, 0, 1, 0],
        0.7306816499355087,
    ),
    (
        [[[0], [2]], [[1, 2, 3]], [[0, 1], [2, 3]], [[0, 1, 2]]],
        [1, 1, 0, 1],
        0.9362933635841989,
    ),
]


@pytest.mark.parametrize(("pattern", "observable", "expected"), PUBLIC_CASES)
def test_public_fixed_weight_expectations(pattern, observable, expected):
    value = iqp_circuit([0.3, -0.7, 0.2, 1.1], pattern, observable)
    assert value == pytest.approx(expected, abs=1e-3)


@pytest.mark.parametrize(("pattern", "observable", "_"), PUBLIC_CASES)
def test_optimizer_reaches_public_minimum(pattern, observable, _):
    weights = optimize_iqp(pattern, observable)
    assert len(weights) == len(pattern)
    assert iqp_circuit(weights, pattern, observable) == pytest.approx(-1.0, abs=2e-2)


def test_circuit_uses_one_pauli_rotation_per_encoded_subset_and_no_iqp_template():
    pattern = PUBLIC_CASES[0][0]
    specs = qp.specs(iqp_circuit)([0.3, -0.7, 0.2, 1.1], pattern, [1, 0, 1, 0])
    gate_types = specs["resources"].gate_types
    assert gate_types.get("PauliRot", 0) == sum(len(group) for group in pattern)
    assert gate_types.get("IQP", 0) == 0


def test_identity_observable_is_constant_one():
    pattern = [[[0]], [[1, 2]]]
    value = iqp_circuit(np.array([0.7, -1.2]), pattern, [0, 0, 0, 0])
    assert value == pytest.approx(1.0, abs=1e-10)

