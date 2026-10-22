import ast
from pathlib import Path


SUBMISSION = Path(__file__).with_name("submission.py")


def test_complete_submission_contains_pulse_pipeline():
    source = SUBMISSION.read_text(encoding="utf-8")
    tree = ast.parse(source)
    functions = {node.name for node in tree.body if isinstance(node, ast.FunctionDef)}

    assert {"target_state", "hamiltonian", "circuit", "optimal_parameters", "run", "check"} <= functions
    assert "qp.pulse.ParametrizedHamiltonian" in source
    assert "qp.evolve(hamiltonian())" in source


def test_public_cases_are_preserved():
    source = SUBMISSION.read_text(encoding="utf-8")
    assert "0.062368193925808904" in source
    assert "0.26666667860250887" in source
