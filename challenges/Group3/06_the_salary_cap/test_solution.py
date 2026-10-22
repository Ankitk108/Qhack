import ast
from pathlib import Path


SUBMISSION = Path(__file__).with_name("submission.py")


def test_complete_submission_contains_resource_estimation_pipeline():
    source = SUBMISSION.read_text(encoding="utf-8")
    tree = ast.parse(source)
    functions = {node.name for node in tree.body if isinstance(node, ast.FunctionDef)}

    assert {"affordable_precision", "run", "check"} <= functions
    assert "qre.estimate" in source
    assert "qre.QPE" in source
    assert "qre.ResourceConfig" in source


def test_public_cases_are_preserved():
    source = SUBMISSION.read_text(encoding="utf-8")
    assert "684108" in source
    assert "42252" in source
