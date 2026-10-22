import pennylane.numpy as np

from .submission import same_gate_and_phase


def test_identity_and_global_phase_are_the_same_gate():
    alpha = 0.73
    identity = np.eye(2, dtype=complex)
    phased = np.exp(1j * alpha) * identity

    same_gate, measured_alpha, p_one = same_gate_and_phase(identity, phased)

    assert same_gate is True
    assert np.isclose(measured_alpha, alpha, atol=1e-7)
    assert np.isclose(p_one, np.sin(alpha / 2) ** 2, atol=1e-7)


def test_distinct_gates_are_rejected():
    same_gate, alpha, p_one = same_gate_and_phase(
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )

    assert same_gate is False
    assert alpha == 0.0
    assert np.isclose(p_one, 0.5, atol=1e-7)
