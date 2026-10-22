"""Tests for the quantum-kernel challenge."""

import pennylane.numpy as np
import pytest

from .submission import kernel_matrix, quantum_kernel


PUBLIC_DATA = np.array(
    [
        [0.32058496, 0.07741205, 0.53200578, 0.91373749],
        [0.71838322, 0.45665254, 0.19871986, 0.11573320],
        [0.04515000, 0.66228969, 0.69793587, 0.64664178],
    ]
)


def analytical_kernel(x1, x2):
    return float(np.prod(np.cos((x1 - x2) / 2.0) ** 2))


def test_kernel_matches_closed_form():
    for x1 in PUBLIC_DATA:
        for x2 in PUBLIC_DATA:
            assert quantum_kernel(x1, x2) == pytest.approx(
                analytical_kernel(x1, x2), abs=1e-10
            )


def test_self_kernel_is_one_and_kernel_is_symmetric():
    matrix = kernel_matrix(PUBLIC_DATA, PUBLIC_DATA)
    assert np.diag(matrix) == pytest.approx(np.ones(len(PUBLIC_DATA)), abs=1e-10)
    assert matrix == pytest.approx(matrix.T, abs=1e-10)


def test_rectangular_kernel_matrix_has_correct_orientation():
    X1 = PUBLIC_DATA[:2]
    X2 = PUBLIC_DATA[1:]
    matrix = kernel_matrix(X1, X2)
    assert matrix.shape == (2, 2)
    assert matrix[0, 1] == pytest.approx(
        analytical_kernel(X1[0], X2[1]), abs=1e-10
    )


def test_empty_first_dataset_preserves_matrix_shape():
    matrix = kernel_matrix([], PUBLIC_DATA)
    assert matrix.shape == (0, len(PUBLIC_DATA))

