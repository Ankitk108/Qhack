"""Reconstruct a target wire's Bloch vector using expectation values only."""

import pennylane as qp


def bloch_and_purity(prep, num_wires, target_wire):
    """Return the target wire's Bloch vector and reduced-state purity."""
    dev = qp.device("default.qubit", wires=num_wires)

    def expectation_circuit(observable):
        @qp.qnode(dev)
        def circuit():
            prep()
            return qp.expval(observable(target_wire))

        return circuit

    measure_x = expectation_circuit(qp.PauliX)
    measure_y = expectation_circuit(qp.PauliY)
    measure_z = expectation_circuit(qp.PauliZ)

    bloch = [float(measure_x()), float(measure_y()), float(measure_z())]
    purity = float(0.5 * (1.0 + sum(component**2 for component in bloch)))
    return bloch, purity

