"""Prepare a GHZ state and build its complete stabilizer check set."""

from __future__ import annotations

import argparse

import pennylane as qml


def prepare_and_build_checks(n: int) -> list[qml.operation.Operator]:
    """Prepare ``|GHZ_n>`` and return its global-X and adjacent-Z checks.

    This function is intended to run inside a PennyLane QNode. Consequently,
    the preparation gates are added directly to the active quantum circuit.

    Args:
        n: Number of device wires. Must be at least two.

    Returns:
        Exactly ``n`` unweighted Pauli-product observables.

    Raises:
        ValueError: If fewer than two qubits are requested.
    """
    if n < 2:
        raise ValueError("n must be at least 2")

    qml.Hadamard(wires=0)
    for target in range(1, n):
        qml.CNOT(wires=[0, target])

    global_x = qml.prod(*(qml.PauliX(wire) for wire in range(n)))
    adjacent_z = [
        qml.prod(qml.PauliZ(wire), qml.PauliZ(wire + 1))
        for wire in range(n - 1)
    ]
    return [global_x, *adjacent_z]


def wrapper(n: int) -> float:
    """Execute the challenge circuit and return the mean parity score."""
    if n < 2:
        raise ValueError("n must be at least 2")

    device = qml.device("default.qubit", wires=n)

    @qml.qnode(device)
    def parities():
        checks = prepare_and_build_checks(n)
        return [qml.expval(check) for check in checks]

    return float(qml.math.mean(parities()))


def main() -> None:
    """Parse the qubit count and print the GHZ verification score."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int, help="number of qubits (at least 2)")
    args = parser.parse_args()
    print(wrapper(args.n))


if __name__ == "__main__":
    main()

