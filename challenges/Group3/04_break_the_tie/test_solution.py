import pennylane.numpy as np

from .submission import estimate_mean, rotation_angle


def test_rotation_angle_encodes_the_requested_probability():
    for fraction in (0.0, 0.2, 0.5, 1.0):
        angle = rotation_angle(fraction)
        assert np.isclose(np.sin(angle / 2) ** 2, fraction, atol=1e-10)


def test_public_high_mean_case_selects_the_larger_candidate():
    result = estimate_mean(
        [0.125] * 8,
        [0.6, 0.7, 0.8, 0.9, 1.0, 1.0, 1.0, 1.0],
        8,
    )
    assert np.isclose(result, 0.8745681972617296, atol=1e-9)
