import ast
from pathlib import Path


SUBMISSION = Path(__file__).with_name("submission.py")


def test_complete_submission_contains_povm_implementation_and_grader():
    source = SUBMISSION.read_text(encoding="utf-8")
    tree = ast.parse(source)
    functions = {node.name for node in tree.body if isinstance(node, ast.FunctionDef)}

    assert {"positive_sqrt", "implement_POVM", "povm_circuit", "run", "check"} <= functions
    assert "qp.QubitUnitary" in source
    assert "qp.probs" in source


def test_public_cases_are_preserved():
    source = SUBMISSION.read_text(encoding="utf-8")
    assert "[0.25,0.25]" in source
    assert "[0.2,0.4]" in source
