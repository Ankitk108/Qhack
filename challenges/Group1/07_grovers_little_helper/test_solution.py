"""Tests for deterministic ancilla-assisted Grover search."""

import pennylane as qp
import pytest

from .submission import circuit


@qp.prod
def generator():
    qp.Hadamard(0)
    qp.Hadamard(1)


def diffuser(state_generator):
    qp.Reflection(state_generator())


def mark_wire_zero_one():
    qp.PauliZ(wires=0)


def mark_wire_zero_zero():
    qp.PauliX(wires=0)
    qp.PauliZ(wires=0)
    qp.PauliX(wires=0)


def mark_wire_one_one():
    qp.PauliZ(wires=1)


def mark_wire_one_zero():
    qp.PauliX(wires=1)
    qp.PauliZ(wires=1)
    qp.PauliX(wires=1)


@pytest.mark.parametrize(
    ("oracle", "allowed"),
    [
        (mark_wire_zero_one, {"10", "11"}),
        (mark_wire_zero_zero, {"00", "01"}),
        (mark_wire_one_one, {"01", "11"}),
        (mark_wire_one_zero, {"00", "10"}),
    ],
)
def test_every_one_shot_result_is_marked(oracle, allowed):
    for _ in range(25):
        counts = circuit(generator, oracle, diffuser)
        assert sum(counts.values()) == 1
        assert set(counts) <= allowed

