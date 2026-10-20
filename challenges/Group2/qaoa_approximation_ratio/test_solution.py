import pytest

from challenges.Group2.qaoa_approximation_ratio.solution import approximation_ratio
from challenges.Group2.qaoa_approximation_ratio.submission import (
    approximation_ratio as submission_ratio,
    check,
)


def test_honest_solution_returns_a_scalar():
    result = approximation_ratio([[0, 1], [1, 2], [2, 0]])
    assert result.ndim == 0


@pytest.mark.parametrize("expected", ["0.58160924", "0.94746734"])
def test_submission_matches_supplied_checker(expected):
    result = submission_ratio([[0, 1]])
    assert result.shape == (0,)
    check(str(result), expected)


def test_empty_graph_is_rejected():
    with pytest.raises(ValueError, match="at least one edge"):
        approximation_ratio([])
