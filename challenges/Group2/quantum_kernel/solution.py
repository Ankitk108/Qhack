"""Quantum feature-state overlap kernel and pairwise kernel matrices."""

import pennylane as qp
import pennylane.numpy as np


WIRES = tuple(range(4))
dev = qp.device("default.qubit", wires=WIRES)


@qp.qnode(dev)
def quantum_kernel(x1, x2):
    """Return the squared overlap between two angle-embedded datapoints."""
    qp.AngleEmbedding(x1, wires=WIRES)
    qp.adjoint(qp.AngleEmbedding)(x2, wires=WIRES)
    return qp.expval(qp.Projector([0, 0, 0, 0], wires=WIRES))


def kernel_matrix(X1, X2):
    """Return all pairwise quantum-kernel values for two datasets."""
    values = np.array(
        [[quantum_kernel(x1, x2) for x2 in X2] for x1 in X1]
    )
    return values.reshape((len(X1), len(X2)))

