"""Read a weighted eigenphase spectrum with quantum phase estimation."""

import pennylane as qp
import pennylane.numpy as np


def unitary_matrix(phases):
    """Return a diagonal unitary with the supplied eigenphases."""
    return np.diag(np.array([np.exp(2j * np.pi * phase) for phase in phases]))


def read_spectrum(phases, amplitudes, m):
    """Return present eigenphases, their weights, and the 99% repetition cost."""
    target_count = int(np.log2(len(phases)))
    target_wires = list(range(target_count))
    estimation_wires = list(range(target_count, target_count + m))
    device = qp.device("default.qubit", wires=target_count + m)

    @qp.qnode(device)
    def spectrum_circuit():
        qp.StatePrep(amplitudes, wires=target_wires)
        qp.QuantumPhaseEstimation(
            unitary_matrix(phases),
            target_wires=target_wires,
            estimation_wires=estimation_wires,
        )
        return qp.probs(wires=estimation_wires)

    distribution = spectrum_circuit()
    peaks = [
        (index / 2**m, float(weight))
        for index, weight in enumerate(distribution)
        if weight > 1e-9
    ]
    eigenphases = [phase for phase, _ in peaks]
    weights = [weight for _, weight in peaks]

    faintest = min(weights)
    repetitions = int(np.ceil(np.log(0.01) / np.log(1.0 - faintest)))
    return eigenphases, weights, repetitions

