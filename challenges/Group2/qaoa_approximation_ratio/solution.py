"""Depth-four QAOA approximation ratio for minimum vertex cover."""

import pennylane as qp
import pennylane.numpy as np


QAOA_DEPTH = 4
OPTIMIZATION_STEPS = 70


def _vertices(edges):
    """Return the consecutively labelled vertices occurring in ``edges``."""
    if not edges:
        raise ValueError("edges must contain at least one edge")
    return range(max(max(edge) for edge in edges) + 1)


def _cost_hamiltonian(edges):
    """Build the minimum-vertex-cover cost Hamiltonian."""
    coefficients = []
    operators = []

    for first, second in edges:
        coefficients.extend((0.75, 0.75, 0.75))
        operators.extend(
            (
                qp.PauliZ(first) @ qp.PauliZ(second),
                qp.PauliZ(first),
                qp.PauliZ(second),
            )
        )

    for wire in _vertices(edges):
        coefficients.append(-1.0)
        operators.append(qp.PauliZ(wire))

    return qp.Hamiltonian(coefficients, operators)


def _mixer_hamiltonian(edges):
    """Build the transverse-field mixer Hamiltonian."""
    vertices = list(_vertices(edges))
    return qp.Hamiltonian(
        [1.0] * len(vertices),
        [qp.PauliX(wire) for wire in vertices],
    )


def approximation_ratio(edges):
    """Return the depth-four QAOA energy divided by the exact ground energy."""
    vertices = list(_vertices(edges))
    cost = _cost_hamiltonian(edges)
    mixer = _mixer_hamiltonian(edges)
    device = qp.device("default.qubit", wires=len(vertices))

    @qp.qnode(device)
    def qaoa_energy(parameters):
        for wire in vertices:
            qp.Hadamard(wires=wire)

        for layer in range(QAOA_DEPTH):
            qp.qaoa.cost_layer(parameters[0, layer], cost)
            qp.qaoa.mixer_layer(parameters[1, layer], mixer)

        return qp.expval(cost)

    parameters = np.full((2, QAOA_DEPTH), 0.5, requires_grad=True)
    optimizer = qp.GradientDescentOptimizer(stepsize=0.1)
    for _ in range(OPTIMIZATION_STEPS):
        parameters = optimizer.step(qaoa_energy, parameters)

    exact_energy = np.min(qp.eigvals(cost))
    return np.real(qaoa_energy(parameters) / exact_energy)
