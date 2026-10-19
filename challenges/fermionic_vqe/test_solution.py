"""Tests for the fermionic VQE challenge."""

import pennylane as qp
import pennylane.numpy as np
import pytest

from .solution import build_hamiltonian, optimization, vqe_circuit


@pytest.mark.parametrize("coeffs", [[-2, 2, 5], [7, 6, -6], [-3, -2, 4], [0, 0, 0]])
def test_hamiltonian_has_real_coefficients_and_correct_spectrum(coeffs):
    hamiltonian = build_hamiltonian(coeffs)
    mapped_coeffs, _ = hamiltonian.terms()
    assert all(not np.iscomplexobj(coefficient) for coefficient in mapped_coeffs)

    eigenvalues = np.linalg.eigvalsh(qp.matrix(hamiltonian, wire_order=range(6)))
    expected_ground_energy = sum(min(coefficient, 0) for coefficient in coeffs)
    assert eigenvalues[0] == pytest.approx(expected_ground_energy, abs=1e-8)


def test_vqe_circuit_returns_scalar_tensor_and_is_trainable():
    params = np.array([0.2, 0.4, 0.6], requires_grad=True)
    energy = vqe_circuit(params, [-2, 2, 5])
    gradient = qp.grad(vqe_circuit)(params, [-2, 2, 5])
    assert np.ndim(energy) == 0
    assert gradient.shape == (3,)
    assert np.all(np.isfinite(gradient))


@pytest.mark.parametrize(
    ("coeffs", "expected"),
    [([-2, 2, 5], -2), ([7, 6, -6], -6), ([-3, -2, 4], -5)],
)
def test_optimization_finds_ground_energy(coeffs, expected):
    np.random.seed(40)
    assert optimization(coeffs) == pytest.approx(expected, abs=0.1)

