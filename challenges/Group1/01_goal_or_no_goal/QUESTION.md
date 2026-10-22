# Question 1: Goal or No Goal?

**Points:** 100pts

## Question

A GHZ state is the many-qubit generalization of a Bell pair:

$$|\mathrm{GHZ}_n\rangle=\frac{|00\cdots0\rangle+|11\cdots1\rangle}{\sqrt2}. $$

Measuring in the computational basis is not enough to certify this state. The classical mixture

$$\rho_{\mathrm{mix}}=\tfrac12|00\cdots0\rangle\langle00\cdots0|+\tfrac12|11\cdots1\rangle\langle11\cdots1|$$

has the same Z-basis histogram, but it has no coherence between the two branches. The global X-parity observable

$$\Pi_X=X_0X_1\cdots X_{n-1}$$

detects that coherence: its expectation is `+1` for the GHZ state and `0` for the classical mixture. However, X parity alone is also insufficient because the unentangled state $|+\rangle^{\otimes n}$ has the same `+1` parity.

Together, the global X parity and the neighbouring checks $Z_iZ_{i+1}$ uniquely certify the GHZ state. Report their mean:

$$s_n=\frac1n\left(\langle\Pi_X\rangle+\sum_{i=0}^{n-2}\langle Z_iZ_{i+1}\rangle\right).$$

### Challenge task

Complete `prepare_and_build_checks(n)`. Inside the supplied QNode it must:

1. Prepare $|\mathrm{GHZ}_n\rangle$.
2. Return exactly `n` observables: one global X product and `n-1` adjacent ZZ products.
3. Use plain Pauli products with coefficient `1`; identities and duplicate checks are invalid.

### Input

A single integer `n >= 2`.

### Output

A float equal to the mean parity score. A correct construction returns `1.0` within absolute tolerance `1e-5`.

### Public cases

| `n` | Expected output |
|---:|---:|
| 3 | 1.0 |
| 5 | 1.0 |
