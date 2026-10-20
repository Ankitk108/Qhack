import json
import pennylane as qp
import pennylane.numpy as np

# Write any helper functions you need here


def symmetry_score(data, labels, s):
    """Return the data's symmetry score for a candidate XOR symmetry."""
    labeled_points = {
        tuple(int(bit) for bit in point): int(label)
        for point, label in zip(data, labels)
    }

    compatible = 0
    for point, label in zip(data, labels):
        partner = tuple(int(bit) ^ int(shift) for bit, shift in zip(point, s))
        if labeled_points.get(partner) == int(label):
            compatible += 1

    return float(0.5 + compatible / (2 * len(data)))


# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    data, labels, s = json.loads(test_case_input)
    data = np.array(data)
    labels = np.array(labels)
    s = np.array(s)
    out = symmetry_score(data, labels, s)
    return str(out)


def check(solution_output: str, expected_output: str) -> None:
    solution_output = json.loads(solution_output)
    expected_output = json.loads(expected_output)
    assert np.isclose(solution_output, expected_output, rtol=1e-3)


# These are the public test cases
test_cases = [
    (
        "[[[0, 0, 0], [1, 1, 0], [0, 0, 1], [1, 1, 1], [1, 0, 1]], "
        "[0, 0, 1, 1, 2], [1,1,0]]",
        "0.9",
    ),
    (
        "[[[0, 0, 0], [1, 1, 0], [0, 0, 1]], [0, 0, 0], [1,1,0]]",
        "0.833333333333333",
    ),
]

# This will run the public test cases locally
for i, (input_, expected_output) in enumerate(test_cases):
    print(f"Running test case {i} with input '{input_}'...")

    try:
        output = run(input_)

    except Exception as exc:
        print(f"Runtime Error. {exc}")

    else:
        if message := check(output, expected_output):
            print(f"Wrong Answer. Have: '{output}'. Want: '{expected_output}'.")

        else:
            print("Correct!")

