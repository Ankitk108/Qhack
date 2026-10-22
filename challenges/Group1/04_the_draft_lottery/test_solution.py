"""Tests for the QPE spectrum reader."""

import pennylane.numpy as np
import pytest

from .submission import read_spectrum


@pytest.mark.parametrize(
    ("phases", "amplitudes", "m", "expected_phases", "expected_weights", "repetitions"),
    [
        (
            [0.1875, 0.6875],
            [0.8, 0.6],
            4,
            [0.1875, 0.6875],
            [0.64, 0.36],
            11,
        ),
        (
            [0.125, 0.375, 0.625, 0.875],
            [0.7, 0.5, 0.5, 0.1],
            3,
            [0.125, 0.375, 0.625, 0.875],
            [0.49, 0.25, 0.25, 0.01],
            459,
        ),
    ],
)
def test_public_spectra(
    phases, amplitudes, m, expected_phases, expected_weights, repetitions
):
    found_phases, found_weights, found_repetitions = read_spectrum(
        phases, amplitudes, m
    )
    assert found_phases == pytest.approx(expected_phases, abs=1e-9)
    assert found_weights == pytest.approx(expected_weights, abs=1e-6)
    assert found_repetitions == repetitions


def test_degenerate_eigenphases_merge_their_weights():
    phases = [0.25, 0.25, 0.5, 0.75]
    amplitudes = np.sqrt([0.1, 0.2, 0.3, 0.4])
    found_phases, found_weights, repetitions = read_spectrum(phases, amplitudes, 2)
    assert found_phases == pytest.approx([0.25, 0.5, 0.75], abs=1e-9)
    assert found_weights == pytest.approx([0.3, 0.3, 0.4], abs=1e-6)
    assert repetitions == 13


def test_zero_weight_phases_are_omitted():
    phases = [0.0, 0.25, 0.5, 0.75]
    amplitudes = [0.6, 0.0, 0.8, 0.0]
    found_phases, found_weights, repetitions = read_spectrum(phases, amplitudes, 2)
    assert found_phases == pytest.approx([0.0, 0.5], abs=1e-9)
    assert found_weights == pytest.approx([0.36, 0.64], abs=1e-6)
    assert repetitions == 11

