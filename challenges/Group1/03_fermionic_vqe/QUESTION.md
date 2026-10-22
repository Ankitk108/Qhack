# Question 3: Fermionic VQE

**Points:** 200pts

## Question

The Variational Quantum Eigensolver (VQE) estimates the ground-state energy of a system by preparing a parameterized trial state, measuring the expectation value of its Hamiltonian, and optimizing the circuit parameters to minimize that energy. This makes VQE particularly useful for molecular and spin systems on near-term quantum devices.

Here the fermionic Hamiltonian is

$$H=c_0a_0a_0^\dagger+c_1a_1a_1^\dagger+c_2a_2a_2^\dagger=\sum_{p=0}^{2}c_pa_pa_p^\dagger,$$

where `coeffs = [c0, c1, c2]` is supplied as input. Construct the fermionic expression using PennyLane `FermiWord`/`FermiSentence` objects and map it to a six-qubit Pauli Hamiltonian with the Jordan-Wigner transformation. Although the mapping may return complex-valued coefficients, this Hamiltonian is Hermitian; remove the zero imaginary components before constructing the observable.

### Challenge task

Complete three components:

1. `build_hamiltonian(coeffs)` builds and returns the real-coefficient qubit Hamiltonian.
2. `vqe_circuit(params, coeffs)` prepares the variational state and returns its trial energy.
3. `optimization(coeffs)` trains the parameters and returns the final ground-state energy.

### Input

A list of three floating-point coefficients `coeffs`.

### Output

A PennyLane NumPy tensor containing the minimum energy found by VQE.

### Public cases

| `coeffs` | Expected energy |
|---|---:|
| `[-2, 2, 5]` | -2 |
| `[7, 6, -6]` | -6 |
