"""Analytical hidden-subgroup symmetry score for labeled binary data."""

import pennylane.numpy as np


def symmetry_score(data, labels, s):
    """Return the compatibility score of labeled data with XOR symmetry ``s``."""
    labeled_points = {
        tuple(int(bit) for bit in point): int(label)
        for point, label in zip(data, labels)
    }

    compatible = 0
    for point, label in zip(data, labels):
        partner = tuple(int(bit) ^ int(shift) for bit, shift in zip(point, s))
        if labeled_points.get(partner) == int(label):
            compatible += 1

    return float(0.5 + compatible / (2 * len(data)))

