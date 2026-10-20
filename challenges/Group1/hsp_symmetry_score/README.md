# Hidden-Subgroup Symmetry Score

## Problem

For labeled binary data, test whether XOR by a nonzero string `s` preserves
the class label:

$$
f(x)=f(x\oplus s).
$$

For each label `r`, the challenge prepares the uniform state over that class,
applies Hadamards, computes the parity $y\cdot s$ into an ancilla, and defines
$p_r(s)$ as the probability of measuring that ancilla in zero. The final score
is the class-size-weighted average of these probabilities.

## Analytical reduction

Let $M_r=|X_r|$ and let $C_r$ count the members `x` of class `r` whose partner
$x\oplus s$ is also in class `r`. Projecting the Hadamard-transformed state
onto even parity is equivalent to applying the projector

$$
\frac{I+T_s}{2},
$$

where $T_s|x\rangle=|x\oplus s\rangle$. Therefore,

$$
p_r(s)=\frac12\left(1+\frac{C_r}{M_r}\right).
$$

After weighting by class size, the complete score simplifies to

$$
S(s)=\frac12+\frac{1}{2N}\sum_r C_r.
$$

Thus the implementation only needs to count data points whose XOR partners
exist with the same label. A complete pair contributes twice—once from each
member—which is exactly what the overlap formula requires.

## Human-run validation

From the repository root:

```powershell
.\.venv\Scripts\python.exe challenges\hsp_symmetry_score\submission.py
.\.venv\Scripts\python.exe -m pytest challenges\hsp_symmetry_score\test_solution.py -v
```

The submission harness should report `Correct!` for both public cases. Submit
the contents of `submission.py`.

