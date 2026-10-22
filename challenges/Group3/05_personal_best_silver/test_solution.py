import pennylane as qp
import pennylane.numpy as np

from .submission import GATE_COSTS, submission_circ


def test_supplied_submission_queues_the_requested_unitary():
    unitary = np.eye(4, dtype=complex)
    tape = qp.tape.make_qscript(submission_circ)(unitary)

    assert len(tape.operations) == 1
    assert isinstance(tape.operations[0], qp.QubitUnitary)
    assert list(tape.operations[0].wires) == [0, 1]
    assert np.allclose(tape.operations[0].data[0], unitary)


def test_supplied_submission_changes_the_cost_table():
    gates = (qp.RX, qp.RY, qp.RZ, qp.T)
    original = {gate: GATE_COSTS[gate] for gate in gates}
    try:
        submission_circ(np.eye(4, dtype=complex))
        assert all(GATE_COSTS[gate] == 0 for gate in gates)
    finally:
        GATE_COSTS.update(original)
