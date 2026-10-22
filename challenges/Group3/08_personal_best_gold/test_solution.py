import ast
from pathlib import Path


SUBMISSION = Path(__file__).with_name("submission.py")


def test_complete_submission_contains_synthesis_and_grader_functions():
    source = SUBMISSION.read_text(encoding="utf-8")
    tree = ast.parse(source)
    functions = {node.name for node in tree.body if isinstance(node, ast.FunctionDef)}

    expected = {
        "compile_circuit",
        "tape_cost",
        "circuit_matrix",
        "cs_decomposition",
        "submission_circ",
        "run",
        "check",
    }
    assert expected <= functions


def test_gold_requirement_and_public_cases_are_preserved():
    source = SUBMISSION.read_text(encoding="utf-8")
    assert '"Gold": 60.0' in source
    assert '"required_grade": "Gold"' in source
    assert "[2026, 2]" in source
    assert "[7, 2]" in source
