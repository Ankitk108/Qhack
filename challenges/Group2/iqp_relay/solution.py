"""Construct and optimize commuting Pauli-X IQP circuits."""

import pennylane as qp
import pennylane.numpy as np


n_qubits = 4
dev = qp.device("default.qubit", wires=n_qubits)


@qp.qnode(dev)
def iqp_circuit(weights, pattern, observable):
    """Return the requested Pauli-Z-word expectation for an IQP circuit."""
    for parameter_index, rotation_group in enumerate(pattern):
        for wires in rotation_group:
            qp.PauliRot(
                weights[parameter_index],
                "X" * len(wires),
                wires=wires,
            )

    measured_wires = [wire for wire, bit in enumerate(observable) if bit]
    if measured_wires:
        measured_observable = qp.prod(
            *(qp.PauliZ(wire) for wire in measured_wires)
        )
    else:
        measured_observable = qp.Identity(0)
    return qp.expval(measured_observable)


def optimize_iqp(pattern, observable):
    """Optimize and return one shared weight per rotation group."""
    if not any(observable):
        return np.zeros(len(pattern), requires_grad=True)

    for parameter_index, rotation_group in enumerate(pattern):
        anticommuting_factors = sum(
            observable[wire] for wires in rotation_group for wire in wires
        )
        if anticommuting_factors % 2 == 1:
            exact_weights = [0.0] * len(pattern)
            exact_weights[parameter_index] = np.pi
            return np.array(exact_weights, requires_grad=True)

    best_weights = None
    best_cost = float("inf")
    for initial_value in (0.3, 0.7, 1.1):
        weights = np.full(len(pattern), initial_value, requires_grad=True)
        optimizer = qp.AdamOptimizer(stepsize=0.1)
        for _ in range(200):
            weights = optimizer.step(
                lambda current: iqp_circuit(current, pattern, observable),
                weights,
            )
        cost = float(iqp_circuit(weights, pattern, observable))
        if cost < best_cost:
            best_cost = cost
            best_weights = weights

    return best_weights

