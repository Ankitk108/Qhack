"""Tests for the QSVT diffusion-reaction solver."""

import pennylane.numpy as np
import pytest

from .solution import C, b, build_matrix, phi_qsvt, qsvt_diffusion


def normalized_qsvt_solution(nu, k):
    branch = qsvt_diffusion(nu, k)[:4]
    rescaled = branch * np.linalg.norm(b) / C
    return np.real(rescaled / np.linalg.norm(rescaled))


@pytest.mark.parametrize(
    ("nu", "k", "expected"),
    [
        (0.2, 0.5, [0.27959746, 0.42869397, 0.56892447, 0.64371709]),
        (1.0, 1.2, [0.28550356, 0.45957210, 0.59350887, 0.59584262]),
    ],
)
def test_public_cases_exceed_required_fidelity(nu, k, expected):
    output = normalized_qsvt_solution(nu, k)
    assert np.dot(output, np.array(expected)) >= 0.99


@pytest.mark.parametrize(("nu", "k"), [(0.0, 0.0), (0.5, 0.0), (2.0, 2.0)])
def test_qsvt_direction_matches_classical_solution(nu, k):
    output = normalized_qsvt_solution(nu, k)
    classical = np.linalg.solve(build_matrix(nu, k), b)
    classical = classical / np.linalg.norm(classical)
    assert np.dot(output, classical) >= 0.99


def test_fixed_polynomial_metadata():
    assert C == pytest.approx(0.05)
    assert len(phi_qsvt) == 42

