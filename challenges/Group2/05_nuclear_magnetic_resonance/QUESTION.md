# Question 5: Nuclear Magnetic Resonance

**Points:** 200pts

## Question

A Hamiltonian determines time evolution through the time-ordered unitary $U(t)=\mathcal{T}\exp(-iHt)$. For a spin in an oscillating magnetic field, the NMR Hamiltonian is

$$H_{\mathrm{NMR}}(t)=B_0Z+B_1\bigl(\cos(\omega t)X-\sin(\omega t)Y\bigr).$$

$B_0$ and $B_1$ are the parallel and transverse field components and $\omega$ is the driving frequency.

### Challenge task

Complete the QNode `nmr_evolve(B0, B1, omega, time)`. Build the time-dependent `ParametrizedHamiltonian`, evolve the initial state $|0\rangle$ with `qp.evolve`, and return the computational-basis probabilities.

### Input and output

Input is `[B0, B1, omega, time]`; output is the two real measurement probabilities.

### Public cases

- `[1,2,0.5,0.3]` produces `[0.6962061524391174, 0.3037952184677124]`.
- `[1,1,0.25,0.6]` produces `[0.7278291583061218, 0.272170752286911]`.

The checker uses absolute tolerance `3e-2`.
