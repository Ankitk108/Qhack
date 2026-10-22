import json
import pennylane as qp
import pennylane.numpy as np

def positive_sqrt(matrix):
    """Returns the positive-semidefinite square root of a Hermitian matrix."""

    eigenvalues, eigenvectors = np.linalg.eigh(matrix)

    # Remove tiny negative values caused by floating-point error.
    eigenvalues = np.maximum(eigenvalues, 0.0)

    return (
        eigenvectors
        * np.sqrt(eigenvalues)
    ) @ np.conj(eigenvectors).T


def implement_POVM(alpha,beta):
    """Quantum function that implements the protocol for the POVM

    args:
    - alpha (float): coefficient between 0 and 1 associated with the E_0 element
    - beta (float): coefficient between 0 and 1 associated with the E_1 element

    returns:
    - This function is a quantum function (a list of gates to be applied) and must not return anything
    """


    # E0 = alpha |1><1|
    e0 = np.array(
        [
            [0.0, 0.0],
            [0.0, alpha],
        ],
        dtype=complex,
    )

    # E1 = beta |-><-|
    e1 = beta / 2.0 * np.array(
        [
            [1.0, -1.0],
            [-1.0, 1.0],
        ],
        dtype=complex,
    )

    # E2 = I - E0 - E1
    e2 = np.eye(2, dtype=complex) - e0 - e1
    sqrt_e2 = positive_sqrt(e2)

    # The first row produces:
    # |<00|U|0,psi>|^2 = alpha |<1|psi>|^2.
    outcome_0_row = np.array(
        [[0.0, np.sqrt(alpha)]],
        dtype=complex,
    )

    # The second row produces:
    # |<01|U|0,psi>|^2 = beta |<-|psi>|^2.
    outcome_1_row = np.array(
        [[
            np.sqrt(beta / 2.0),
            -np.sqrt(beta / 2.0),
        ]],
        dtype=complex,
    )

    # These four rows define the action of U on inputs whose auxiliary
    # qubit is |0>, namely the first two columns of the full unitary.
    isometry = np.vstack(
        [
            outcome_0_row,
            outcome_1_row,
            sqrt_e2,
        ]
    )

    # Find an orthonormal basis for the complement of the isometry's
    # column space. The last two right-singular vectors span its null space.
    _, _, vh = np.linalg.svd(
        np.conj(isometry).T,
        full_matrices=True,
    )

    complement = np.conj(vh).T[:, 2:]

    # Preserve the isometry exactly as the first two columns.
    unitary = np.column_stack(
        [
            isometry,
            complement,
        ]
    )

    qp.QubitUnitary(
        unitary,
        wires=[0, 1],
    )

dev = qp.device("default.qubit", wires = [0,1])

@qp.qnode(dev)
def povm_circuit(values, state):
    """
    This circuit will apply your POVM to some initial state in the first wire and will be used to 
    verify that we obtain the right probabilities

    args:
    - values: An array [alpha, beta], containing the coefficients that define the POVM
    - state: A (not normalized) vector specifying the initial joint state for the circuit

    returns:
    - np.array: The probabilities on both wires to verify that your unitary gives the right output.
    
    """

    vec = np.array([state[0],state[1],0,0])
    vec = vec/np.linalg.norm(vec)

    qp.StatePrep(vec, wires = [0,1])

    implement_POVM(*values)

    return qp.probs(wires = [0,1])


# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:

    ins = json.loads(test_case_input)
    alpha = ins[0]
    beta = ins[1]
    def e0_probs(alpha, vec):

        vec = vec/np.linalg.norm(vec)
        e0 = np.kron([0,1],[[0],[1]])
        return alpha * (vec@e0@vec)

    def e1_probs(beta, vec):

        vec = vec/np.linalg.norm(vec)
        e1 = 1/2 * np.kron([1,-1],[[1],[-1]])
        return beta * (vec@e1@vec)

    for i in range(10):
        v = np.random.rand(1,2)[0]
        v = v/np.linalg.norm(v)
        if not np.allclose(povm_circuit(ins,v)[:2], [e0_probs(alpha,v), e1_probs(beta,v)]):
            return "Incorrect circuit"

    return "Correct circuit"

def check(solution_output: str, expected_output: str) -> None:
    solution_output = solution_output
    expected_output = expected_output

    assert solution_output == expected_output, "Not the correct POVM implementation."


# These are the public test cases
test_cases = [
    ('[0.25,0.25]', 'Correct circuit'),
    ('[0.2,0.4]', 'Correct circuit')
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
