# QSVT Diffusion-Reaction Solver

## Discrete problem

Backward Euler turns one time step of the diffusion-reaction equation into

$$
A\phi_{\mathrm{new}}=b,
\qquad
A=(1+k\Delta t)I-\nu\Delta tD_2,
$$

with

$$
b=\phi+\Delta t\,s.
$$

For `h = 0.2` and `dt = 0.01`, `A` is a real symmetric positive-definite
tridiagonal matrix. Classically, the desired vector is `solve(A, b)`.

## QSVT construction

The implementation divides `A` by its spectral norm and block-encodes the
normalized matrix. Over all nonnegative diffusion and reaction parameters, its
smallest normalized eigenvalue stays above approximately `0.1056`. The fixed
degree-41 odd polynomial therefore approximates

$$
P(x)\approx\frac{0.05}{x}
$$

on `0.1 <= |x| <= 1`.

QSVT places `P(A)` in the block-encoding's top-left block. The selected phase
convention also produces an irrelevant imaginary component, so an additional
Hadamard-test ancilla combines the QSVT unitary with its adjoint and extracts

$$
\frac{U_{\mathrm{QSVT}}+U_{\mathrm{QSVT}}^\dagger}{2}.
$$

The first four returned amplitudes are consequently proportional to
`0.05 * solve(A, b) / norm(b)`, which is the branch consumed by the supplied
grader.

## Wire layout

- Wire `0`: Hermitian-part selection ancilla.
- Wire `1`: `BlockEncode` ancilla.
- Wires `2, 3`: four-dimensional concentration register.

## Human-run validation

From the repository root:

```powershell
.\.venv\Scripts\python.exe challenges\qsvt_diffusion\submission.py
.\.venv\Scripts\python.exe -m pytest challenges\qsvt_diffusion\test_solution.py -v
```

The first command should report `Correct!` for both public cases. The QSVT
circuit is substantially deeper than the earlier challenges, so execution can
take longer. Submit the contents of `submission.py`.

