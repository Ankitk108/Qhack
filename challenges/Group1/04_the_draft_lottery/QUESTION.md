# Question 4: The Draft Lottery

**Points:** 200pts

## Question

Quantum phase estimation (QPE) is often introduced with an eigenvector as its input. In practice, the target state is usually a superposition

$$|\psi\rangle=\sum_k c_k|u_k\rangle,$$

where $U|u_k\rangle=e^{2\pi i\theta_k}|u_k\rangle$. By linearity, QPE with $m$ estimation wires produces

$$|\psi\rangle|0\rangle^{\otimes m}\longmapsto\sum_k c_k|u_k\rangle|\widetilde{\theta}_k\rangle.$$

Measuring only the estimation register therefore samples phase $\theta_k$ with weight $|c_k|^2$. Eigenvectors sharing a phase contribute to the same probability bin. Bin `j` represents phase $j/2^m$.

A faint phase with total weight $w$ may require many repetitions. To observe it at least once with probability at least 99%, choose

$$r=\left\lceil\frac{\ln(0.01)}{\ln(1-w)}\right\rceil.$$

### Challenge task

Implement `read_spectrum(phases, amplitudes, m)`. Build a device with the target wires first and `m` estimation wires afterward, prepare the supplied real normalized amplitudes, apply QPE to the diagonal unitary from `unitary_matrix(phases)`, and measure the estimation-register probabilities. All test phases are exact multiples of $1/2^m$, so spectral leakage is absent.

### Inputs

- `phases`: one phase in `[0, 1)` per target basis state; its length is a power of two.
- `amplitudes`: normalized real amplitudes aligned with `phases`.
- `m`: number of estimation wires.

### Output

Return `(eigenphases, weights, repetitions)`, where phases are distinct and ascending, bins are retained only when their probability exceeds `1e-9`, and `repetitions` is determined by the faintest retained weight.

### Public cases

```python
read_spectrum([0.1875, 0.6875], [0.8, 0.6], 4)
# ([0.1875, 0.6875], [0.64, 0.36], 11)

read_spectrum([0.125, 0.375, 0.625, 0.875],
              [0.7, 0.5, 0.5, 0.1], 3)
# ([0.125, 0.375, 0.625, 0.875], [0.49, 0.25, 0.25, 0.01], 459)
```

Phases use absolute tolerance `1e-9`, weights `1e-6`, and the repetition count must match exactly.
