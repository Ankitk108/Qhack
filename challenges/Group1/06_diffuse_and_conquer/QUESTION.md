# Question 6: Diffuse and Conquer

**Points:** 400pts

## Question

A one-dimensional concentration field obeys the diffusion-reaction equation

$$\frac{\partial\phi}{\partial t}=\nu\frac{\partial^2\phi}{\partial x^2}-k\phi+s(x,t),$$

where $\nu$ is the diffusion coefficient, $k$ the reaction rate, and $s$ a source. Discretize the fluid at four interior points separated by $h=0.2$, with

$$D_2=\frac1{h^2}\begin{pmatrix}-2&1&0&0\\1&-2&1&0\\0&1&-2&1\\0&0&1&-2\end{pmatrix}.$$

A backward-Euler step of size $\Delta t=0.01$ gives

$$A\phi_{\mathrm{new}}=b,\qquad A=(1+k\Delta t)I-\nu\Delta tD_2,\qquad b=\phi_{\mathrm{old}}+\Delta t\,s.$$

The initial concentration, source, grid spacing, and timestep are fixed in the starter code; only `nu` and `k` vary. Instead of calculating $A^{-1}b$ classically, use Quantum Singular Value Transformation (QSVT) to approximate the inverse.

### Challenge task

Complete `qsvt_diffusion(nu, k)`. The solution must construct `A`, normalize and block-encode it, specify a constant `C` and QSVT phase angles that approximate $C/x$, and apply the transformation to the normalized source vector. The grader rescales the selected output branch using `C`.

### Input

A pair `[nu, k]` containing the diffusion coefficient and reaction rate.

### Output

A floating-point array representing the normalized concentration after one step. The result must have fidelity greater than `0.99` with the analytical solution.

### Public cases

| `[nu, k]` | Expected concentration |
|---|---|
| `[0.2, 0.5]` | `[0.27959746, 0.42869397, 0.56892447, 0.64371709]` |
| `[1.0, 1.2]` | `[0.28550356, 0.45957210, 0.59350887, 0.59584262]` |
