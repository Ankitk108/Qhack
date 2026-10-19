# Quantum Phase-Estimation Spectrum Reader

## Problem

Prepare a target-register superposition, apply quantum phase estimation to a
diagonal unitary, and read the complete probability distribution of the
estimation register. If

$$
|\psi\rangle=\sum_k c_k|u_k\rangle,
$$

then QPE reports eigenphase $\theta_k$ with weight $|c_k|^2$. Equal phases
share one measurement bin, so their weights add automatically.

With `m` estimation wires, probability-bin `k` represents

$$
\theta=\frac{k}{2^m}.
$$

Only bins with probability greater than `1e-9` are retained. If the faintest
retained peak has weight `w`, the required number of independent runs for a
99-percent chance of seeing it is

$$
r=\left\lceil\frac{\ln(0.01)}{\ln(1-w)}\right\rceil.
$$

## Implementation outline

1. Compute the target-register width from `len(phases)`.
2. Place target wires first and estimation wires after them.
3. Prepare `amplitudes` with `StatePrep`.
4. Apply `QuantumPhaseEstimation` using `unitary_matrix(phases)`.
5. Return `probs` on only the estimation register and read its nonzero peaks.

## Human-run validation

From the repository root:

```powershell
.\.venv\Scripts\python.exe challenges\qpe_spectrum\submission.py
.\.venv\Scripts\python.exe -m pytest challenges\qpe_spectrum\test_solution.py -v
```

The submission harness should report `Correct!` for both public cases. Submit
the contents of `submission.py`, which preserves the challenge template order.

