"""Deterministic ancilla-assisted search when exactly half the states are marked."""

import pennylane as qp


dev = qp.device("default.qubit", wires=3)


@qp.set_shots(1)
@qp.qnode(dev)
def circuit(generator, oracle, diffuser):
    """Return one marked two-qubit state using one oracle and one diffuser."""
    generator()

    qp.Hadamard(wires=2)
    qp.ctrl(oracle, control=2)()
    qp.Hadamard(wires=2)

    qp.ctrl(diffuser, control=2, control_values=0)(generator)
    return qp.counts(wires=[0, 1])

