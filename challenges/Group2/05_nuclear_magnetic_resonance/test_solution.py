"""Tests for time-dependent NMR evolution."""

import jax.numpy as jnp
import pytest

from .submission import nmr_evolve


@pytest.mark.parametrize(
    ("parameters", "expected"),
    [
        ((1.0, 2.0, 0.5, 0.3), [0.6962061524391174, 0.3037952184677124]),
        ((1.0, 1.0, 0.25, 0.6), [0.7278291583061218, 0.272170752286911]),
    ],
)
def test_public_probabilities(parameters, expected):
    probabilities = nmr_evolve(*parameters)
    assert probabilities == pytest.approx(expected, abs=0.03)


def test_probabilities_are_real_normalized_and_nonnegative():
    probabilities = nmr_evolve(0.7, 1.4, 0.9, 0.45)
    assert jnp.all(jnp.isreal(probabilities))
    assert jnp.all(probabilities >= 0.0)
    assert jnp.sum(probabilities) == pytest.approx(1.0, abs=5e-6)


def test_zero_time_leaves_initial_state_unchanged():
    probabilities = nmr_evolve(3.0, 4.0, 2.0, 0.0)
    assert probabilities == pytest.approx([1.0, 0.0], abs=1e-8)

