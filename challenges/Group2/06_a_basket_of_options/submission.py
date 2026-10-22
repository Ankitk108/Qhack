"""Price a two-asset basket option with quantum Monte Carlo."""

import pennylane as qp
import pennylane.numpy as np


M = 64

S10 = 100.0
S20 = 100.0

sigma1 = 0.20
sigma2 = 0.30

r = 0.05


def scenarios():
    """Return the flattened 8 by 8 grid of normal variates."""
    z = np.linspace(-3.0, 3.0, 8)
    z1, z2 = np.meshgrid(z, z, indexing="ij")
    return z1.flatten(), z2.flatten()


def probabilities(rho):
    """Return normalized bivariate-normal weights on the scenario grid."""
    z1, z2 = scenarios()
    density = np.exp(
        -(z1**2 - 2 * rho * z1 * z2 + z2**2)
        / (2 * (1 - rho**2))
    )
    density = density / (2 * np.pi * np.sqrt(1 - rho**2))
    return density / np.sum(density)


def payoff(i, w, T, K):
    """Return the basket-call payoff in scenario ``i``."""
    z1, z2 = scenarios()
    S1 = S10 * np.exp(
        (r - sigma1**2 / 2) * T + sigma1 * np.sqrt(T) * z1[i]
    )
    S2 = S20 * np.exp(
        (r - sigma2**2 / 2) * T + sigma2 * np.sqrt(T) * z2[i]
    )
    basket = w * S1 + (1 - w) * S2
    return np.maximum(basket - K, 0.0)


n = 10
N = 2**n
m = int(np.log2(M))
target_wires = range(m + 1)
estimation_wires = range(m + 1, n + m + 1)

dev = qp.device("default.qubit", wires=(n + m + 1))


@qp.qnode(dev)
def quantum_montecarlo(rho, w, T, K):
    """Return phase-estimation probabilities for the normalized expected payoff."""
    p = probabilities(rho)
    payoffs = np.array([payoff(i, w, T, K) for i in range(M)])
    payoff_max = np.max(payoffs)

    if payoff_max > 0:
        normalized_payoffs = payoffs / payoff_max
    else:
        normalized_payoffs = np.zeros(M)

    def func(i):
        return normalized_payoffs[i]

    qp.templates.QuantumMonteCarlo(
        probs=p,
        func=func,
        target_wires=target_wires,
        estimation_wires=estimation_wires,
    )
    return qp.probs(estimation_wires)

# Imports used by the original challenge grader.
import json
import pennylane as qp
import pennylane.numpy as np

# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    ins = json.loads(test_case_input)
    phase_estimated = np.argmax(quantum_montecarlo(*ins)[:int(N / 2)]) / N
    payoffs = np.array([
        payoff(i, ins[1], ins[2], ins[3]) for i in range(M)
    ])

    payoff_max = np.max(payoffs)
    output = (1 - np.cos(np.pi * phase_estimated)) / 2 * payoff_max * np.exp(-r * ins[2])

    return str(output)


def check(solution_output: str, expected_output: str) -> None:
    solution_output = json.loads(solution_output)
    expected_output = json.loads(expected_output)
    assert np.allclose(
        solution_output, expected_output, atol=1e-3
    ), "Your circuit doesn't look quite right "


test_cases = [
    ('[0.3, 1.0, 1.0, 100]', '10.556134590137553'),
    ('[0.4, 0.5, 1.0, 110]', '6.487093067342844'),
]


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
