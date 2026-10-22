# Question 4: A Relay of Phases

**Points:** 200pts

## Question

An IQP circuit is built from mutually commuting Pauli-X rotations

$$U(\theta)=\prod_j\exp\!\left(-\frac{i\theta_j}{2}X_{S_j}\right),\qquad X_{S_j}=\prod_{k\in S_j}X_k.$$

`pattern[j]` lists every wire subset using the shared parameter `weights[j]`. For example, `[[[0],[1]], [[1,2]]]` applies the first angle to separate X rotations on wires 0 and 1 and the second to an XX rotation on wires 1 and 2. The binary observable vector $a$ represents $Z^a=\prod_k Z_k^{a_k}$.

### Challenge task

Construct the four-qubit QNode `iqp_circuit(weights, pattern, observable)` using PennyLane operations but not the built-in `qp.IQP` template. Return the requested Pauli-Z-word expectation. Then implement `optimize_iqp(pattern, observable)` and return one optimized parameter per pattern group so the expectation is minimized.

### Input and output

Input is `[pattern, observable]`; output is an array of optimized weights. The grader also evaluates the circuit at fixed weights to check its construction.

### Public cases

The two supplied patterns must produce fixed-weight expectations `0.7306816499355087` and `0.9362933635841989`, respectively, and optimized cost `-1` within absolute tolerance `2e-2`.
