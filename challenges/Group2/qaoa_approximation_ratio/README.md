# Approximation Ratio for QAOA

This challenge applies a four-layer Quantum Approximate Optimization Algorithm
(QAOA) circuit to the minimum vertex-cover Hamiltonian

$$
H_{\mathrm{cost}} = \frac{3}{4}\sum_{(i,j)\in E}
(Z_iZ_j + Z_i + Z_j) - \sum_{i\in V} Z_i.
$$

The mixer is $H_{\mathrm{mixer}}=\sum_{i\in V}X_i$. Every qubit begins in
$|+\rangle$, and each of the four layers applies the cost evolution followed by
the mixer evolution.

After a deterministic gradient-descent optimization, the result is compared
with the exact smallest eigenvalue:

$$
r^* = \frac{\langle H_{\mathrm{cost}}\rangle_{\mathrm{QAOA}}}
{\lambda_{\min}(H_{\mathrm{cost}})}.
$$

Both energies are normally negative here, so the ratio approaches `1.0` as the
variational energy approaches the exact ground energy.

## Human-run validation

From the repository root:

```powershell
.\.venv\Scripts\python.exe challenges\Group2\qaoa_approximation_ratio\submission.py
.\.venv\Scripts\python.exe -m pytest challenges\Group2\qaoa_approximation_ratio
```

The challenge's checker compares against a particular finite optimization
trajectory rather than accepting every better ratio. The fixed initialization,
step size, and iteration count therefore make the result reproducible.
