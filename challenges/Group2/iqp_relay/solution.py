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
    weights = np.full(len(pattern), 0.3, requires_grad=True)
    optimizer = qp.AdamOptimizer(stepsize=0.1)

    for _ in range(120):
        weights = optimizer.step(
            lambda current: iqp_circuit(current, pattern, observable),
            weights,
        )

    return weights

