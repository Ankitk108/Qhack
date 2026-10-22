import pennylane as qp
import pytest

from .submission import quantum_neural_network


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([0.4859371, 1.32682562, -1.06015833, -4.41959946], 0.827549),
        ([-0.72318627, -4.91395046, -5.0609724, 0.1125593], 0.865457),
    ],
)
def test_public_cases(values, expected):
    assert quantum_neural_network(values[0], values[1:]) == pytest.approx(
        expected, rel=1e-4
    )


def test_zero_angles_reduce_to_encoded_rx_expectation():
    assert quantum_neural_network(0.37, [0.0, 0.0, 0.0]) == pytest.approx(
        qp.math.cos(0.37), abs=1e-10
    )


def test_circuit_has_expected_gate_order():
    tape = qp.tape.make_qscript(
        lambda: quantum_neural_network.func(0.2, [0.3, 0.4, 0.5])
    )()
    assert [op.name for op in tape.operations] == ["RX", "RZ", "RY", "RZ"]
    assert tape.measurements[0].obs.name == "PauliZ"
