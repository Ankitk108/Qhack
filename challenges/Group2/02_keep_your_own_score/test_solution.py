"""Tests for reconstructing Pauli expectations from probabilities."""

from itertools import product

import pennylane as qp
import pennylane.numpy as np
import pytest

from .submission import measure_pauli_word, prepare


PUBLIC_CASES = [
    (
        "ZIZ",
        [0.79, 2.75, 2.89, 0.33],
        ["none", "none", "none"],
        [1, -1, 1, -1, -1, 1, -1, 1],
        0.931986472711103,
    ),
    (
        "XYI",
        [1.45, 0.22, 1.72, 1.4],
        ["H", "SH", "none"],
        [1, 1, -1, -1, -1, -1, 1, 1],
        0.9673999542626387,
    ),
]


@pytest.mark.parametrize(("word", "angles", "basis", "signs", "value"), PUBLIC_CASES)
def test_public_cases(word, angles, basis, signs, value):
    found_basis, found_signs, found_value = measure_pauli_word(word, angles)
    assert found_basis == basis
    assert found_signs == signs
    assert found_value == pytest.approx(value, abs=1e-6)


def test_identity_has_unit_expectation_and_positive_signs():
    basis, signs, value = measure_pauli_word("III", [0.2, 0.4, 0.6, 0.8])
    assert basis == ["none", "none", "none"]
    assert signs == [1] * 8
    assert value == pytest.approx(1.0, abs=1e-10)


def reference_expectation(word, angles):
    device = qp.device("default.qubit", wires=3)
    paulis = {"I": qp.Identity, "X": qp.PauliX, "Y": qp.PauliY, "Z": qp.PauliZ}
    observable = qp.prod(*(paulis[letter](wire) for wire, letter in enumerate(word)))

    @qp.qnode(device)
    def reference_circuit():
        prepare(angles)
        return qp.expval(observable)

    return float(reference_circuit())


def test_all_pauli_words_match_reference_expectations():
    angles = [0.37, 1.11, 2.04, 0.63]
    for letters in product("IXYZ", repeat=3):
        word = "".join(letters)
        _, _, value = measure_pauli_word(word, angles)
        assert value == pytest.approx(reference_expectation(word, angles), abs=1e-9)

