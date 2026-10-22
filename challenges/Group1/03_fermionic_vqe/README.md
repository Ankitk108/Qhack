# Fermionic Hamiltonian VQE

## Problem

Construct the fermionic Hamiltonian

$$
H = \sum_{p=0}^{2} c_p\,a_p a_p^\dagger
$$

with PennyLane `FermiWord` objects, map it to qubits using the Jordan–Wigner
transformation, and use a variational circuit to estimate its ground energy.
The device has six wires, although this Hamiltonian acts nontrivially only on
the first three orbitals.

For one orbital, the Jordan–Wigner mapping gives

$$
a_p a_p^\dagger = 1-a_p^\dagger a_p = \frac{I+Z_p}{2}.
$$

Therefore each negative coefficient is minimized by placing its qubit in
`|0>` and each positive coefficient by placing its qubit in `|1>`. The exact
ground energy is consequently

$$
E_0 = \sum_{p=0}^{2}\min(c_p,0).
$$

The solution still performs VQE rather than returning this analytical result.
Three independent RY rotations can represent every required computational
basis state, and an Adam optimizer minimizes the measured Hamiltonian energy.

## Local validation and submission

From the repository root, run:

```powershell
.\.venv\Scripts\python.exe challenges\Group1\03_fermionic_vqe\submission.py
.\.venv\Scripts\python.exe -m pytest challenges\Group1\03_fermionic_vqe\test_solution.py -v
```

The submission harness should report `Correct!` for both public cases. Submit
the contents of `submission.py`, which preserves the supplied code order.

