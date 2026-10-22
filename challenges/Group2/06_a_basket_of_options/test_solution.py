import pennylane.numpy as np
import pytest

from .submission import (
    M,
    estimation_wires,
    payoff,
    probabilities,
    quantum_montecarlo,
    scenarios,
)


def test_scenario_grid_has_64_points():
    z1, z2 = scenarios()
    assert len(z1) == len(z2) == M
    assert np.isclose(z1[0], -3.0)
    assert np.isclose(z2[-1], 3.0)


@pytest.mark.parametrize("rho", [-0.5, 0.0, 0.4, 0.8])
def test_probabilities_are_normalized(rho):
    distribution = probabilities(rho)
    assert distribution.shape == (M,)
    assert np.all(distribution >= 0)
    assert np.isclose(np.sum(distribution), 1.0)


def test_payoff_is_nonnegative():
    values = np.array([payoff(i, 0.5, 1.0, 110.0) for i in range(M)])
    assert np.all(values >= 0)


def test_estimation_register_is_last_and_has_ten_wires():
    assert list(estimation_wires) == list(range(7, 17))


@pytest.mark.slow
@pytest.mark.parametrize(
    ("inputs", "expected"),
    [
        ((0.3, 1.0, 1.0, 100.0), 10.556134590137553),
        ((0.4, 0.5, 1.0, 110.0), 6.487093067342844),
    ],
)
def test_public_option_values(inputs, expected):
    rho, w, maturity, strike = inputs
    probabilities_out = quantum_montecarlo(rho, w, maturity, strike)
    phase = np.argmax(probabilities_out[:512]) / 1024
    payoffs = np.array([payoff(i, w, maturity, strike) for i in range(M)])
    value = (
        (1 - np.cos(np.pi * phase))
        / 2
        * np.max(payoffs)
        * np.exp(-0.05 * maturity)
    )
    assert np.allclose(value, expected, atol=1e-3)
