# The Scouting Report

## Single-wire tomography

The reduced state of any one qubit can be written as

$$
\rho=\frac12(I+r_xX+r_yY+r_zZ),
$$

where each Bloch component is an experimentally accessible expectation value:

$$
r_x=\langle X\rangle,\qquad
r_y=\langle Y\rangle,\qquad
r_z=\langle Z\rangle.
$$

The implementation builds three QNodes on the supplied `dev`. Each QNode calls
the same opaque `prep()` and returns one `qp.expval` on `target_wire`. It never
reads the simulator state or assumes that the target is wire zero.

The purity follows entirely from the reconstructed Bloch vector:

$$
\operatorname{Tr}(\rho^2)
=\frac12\left(1+r_x^2+r_y^2+r_z^2\right).
$$

A pure local state has purity one. A maximally entangled qubit has a maximally
mixed reduced state, zero Bloch vector, and purity one half.

## Human-run validation

From the repository root:

```powershell
.\.venv\Scripts\python.exe challenges\Group2\scouting_report\submission.py
.\.venv\Scripts\python.exe -m pytest challenges\Group2\scouting_report\test_solution.py -v
```

The first command should report `Correct!` for both public cases. Submit the
contents of `submission.py`.

