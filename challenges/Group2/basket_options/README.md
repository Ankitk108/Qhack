# A Basket of Options

This challenge prices a European call on a weighted basket of two correlated
assets. It discretizes a correlated bivariate normal distribution on an
$8\times8$ grid, loads the resulting 64 probabilities, and encodes each
scenario's normalized basket payoff with PennyLane's `QuantumMonteCarlo`
template.

The target register uses six scenario wires and one payoff ancilla. Ten phase
estimation wires follow them as the last wires on the device. If the dominant
estimated phase is $\theta$, the normalized mean payoff is recovered as

$$
\mu = \frac{1-\cos(\pi\theta)}{2}.
$$

The grader restores the payoff scale and discounts it to the present:

$$
V_0=e^{-rT}g_{\max}\mu.
$$

## Argument order

Although one part of the statement lists `(K, w, rho, T)`, the executable
template and public cases use `(rho, w, T, K)`. The solution preserves the
executable order required by the grader.

## Human-run validation

The full circuit acts on 17 wires and may take appreciable time and memory. Run
it yourself from the repository root:

```powershell
.\.venv\Scripts\python.exe challenges\Group2\basket_options\submission.py
.\.venv\Scripts\python.exe -m pytest challenges\Group2\basket_options
```
