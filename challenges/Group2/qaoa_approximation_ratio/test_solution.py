import pennylane.numpy as np
import pytest

from challenges.Group2.qaoa_approximation_ratio.solution import approximation_ratio


@pytest.mark.parametrize(
    ("edges", "expected"),
    [
        ([[0, 1], [1, 2], [0, 2], [2, 3]], 0.58160924),
        ([[0, 1], [1, 2], [2, 3], [3, 0]], 0.94746734),
    ],
)
def test_public_cases(edges, expected):
    assert np.allclose(approximation_ratio(edges), expected, rtol=5e-2)


def test_empty_graph_is_rejected():
    with pytest.raises(ValueError, match="at least one edge"):
        approximation_ratio([])
