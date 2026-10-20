"""Time evolution under a driven one-qubit NMR Hamiltonian."""

import jax.numpy as jnp
import pennylane as qp


dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def nmr_evolve(B0: float, B1: float, omega: float, time: float) -> "jnp.ndarray":
    """Evolve |0> under the NMR Hamiltonian and return basis probabilities."""
    coeffs = [
        B0,
        lambda parameter, t: parameter * jnp.cos(omega * t),
        lambda parameter, t: -parameter * jnp.sin(omega * t),
    ]
    ops = [qp.PauliZ(0), qp.PauliX(0), qp.PauliY(0)]
    hamiltonian = qp.dot(coeffs, ops)

    qp.evolve(hamiltonian)([B1, B1], t=[0.0, time])
    return qp.probs(wires=0)

