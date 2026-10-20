"""Tests for the hidden-subgroup symmetry score."""

import pennylane.numpy as np
import pytest

from .solution import symmetry_score


@pytest.mark.parametrize(
    ("data", "labels", "s", "expected"),
    [
        (
            [[0, 0, 0], [1, 1, 0], [0, 0, 1], [1, 1, 1], [1, 0, 1]],
            [0, 0, 1, 1, 2],
            [1, 1, 0],
            0.9,
        ),
        (
            [[0, 0, 0], [1, 1, 0], [0, 0, 1]],
            [0, 0, 0],
            [1, 1, 0],
            5 / 6,
        ),
    ],
)
def test_public_cases(data, labels, s, expected):
    score = symmetry_score(np.array(data), np.array(labels), np.array(s))
    assert score == pytest.approx(expected, abs=1e-12)


def test_complete_same_label_pairs_score_one():
    data = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
    labels = np.array([4, 4, 9, 9])
    assert symmetry_score(data, labels, np.array([1, 0])) == pytest.approx(1.0)


def test_no_same_label_partner_scores_one_half():
    data = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
    labels = np.array([0, 1, 2, 3])
    assert symmetry_score(data, labels, np.array([1, 0])) == pytest.approx(0.5)


def test_partner_with_different_label_does_not_count():
    data = np.array([[0, 0], [1, 0], [0, 1]])
    labels = np.array([7, 8, 7])
    assert symmetry_score(data, labels, np.array([1, 0])) == pytest.approx(0.5)

