"""Tests for the GHZ verification challenge."""

import pennylane as qml
import pytest

from solution import prepare_and_build_checks, wrapper


@pytest.mark.parametrize("n", [2, 3, 5, 8])
def test_correct_ghz_scores_one(n):
    assert wrapper(n) == pytest.approx(1.0, abs=1e-5)


@pytest.mark.parametrize("n", [2, 3, 5, 8])
def test_returns_exact_required_pauli_products(n):
    with qml.queuing.AnnotatedQueue():
        checks = prepare_and_build_checks(n)

    assert len(checks) == n
    assert all(isinstance(check, qml.ops.op_math.Prod) for check in checks)
    assert all(check.arithmetic_depth == 1 for check in checks)

    pauli_words = {
        qml.pauli.pauli_word_to_string(check, wire_map={wire: wire for wire in range(n)})
        for check in checks
    }
    expected = {"X" * n}
    expected.update(
        "I" * wire + "ZZ" + "I" * (n - wire - 2)
        for wire in range(n - 1)
    )
    assert pauli_words == expected

    for check in checks:
        assert all(
            isinstance(factor, (qml.PauliX, qml.PauliZ))
            for factor in check.operands
        )


@pytest.mark.parametrize("function", [prepare_and_build_checks, wrapper])
@pytest.mark.parametrize("n", [-1, 0, 1])
def test_rejects_too_few_qubits(function, n):
    with pytest.raises(ValueError, match="at least 2"):
        function(n)

