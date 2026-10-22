# Building a Quantum Kernel

## Feature-state overlap

Four real features are encoded as rotations on four qubits:

$$
|\phi(x)\rangle=S(x)|0000\rangle.
$$

The quantum kernel is the squared state overlap

$$
k(x_1,x_2)=|\langle\phi(x_2)|\phi(x_1)\rangle|^2.
$$

The circuit applies `S(x1)` followed by `S(x2)` in reverse:

$$
S^\dagger(x_2)S(x_1)|0000\rangle.
$$

The probability of returning to `|0000>` is exactly the desired kernel. An
expectation value of the all-zero projector returns that scalar directly.

For PennyLane's independent angle embedding, this kernel also has the closed
form

$$
k(x_1,x_2)=\prod_{j=0}^{3}
\cos^2\left(\frac{x_{1,j}-x_{2,j}}{2}\right).
$$

The implementation nevertheless evaluates it using the requested quantum
circuit.

## Kernel matrix

For datasets `X1` and `X2`, entry `(i, j)` is

$$
K_{ij}=k(X1_i,X2_j).
$$

The output shape is therefore `(len(X1), len(X2))`; the two datasets need not
have equal lengths.

## Human-run validation

From the repository root:

```powershell
.\.venv\Scripts\python.exe challenges\Group2\01_building_a_quantum_kernel\submission.py
.\.venv\Scripts\python.exe -m pytest challenges\Group2\01_building_a_quantum_kernel\test_solution.py -v
```

The first command should report `Correct!` for both public cases. Submit the
contents of `submission.py`.

