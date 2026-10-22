# Nuclear Magnetic Resonance

## Hamiltonian

The one-qubit spin evolves under

$$
H(t)=B_0Z+B_1\cos(\omega t)X-B_1\sin(\omega t)Y.
$$

The static `Z` coefficient is supplied directly. The `X` and `Y` coefficients
are callables because they depend on both the trainable pulse parameter and
time. Combining those coefficients with their Pauli operators through
`qp.dot` creates a PennyLane `ParametrizedHamiltonian`.

The evolution call

```python
qp.evolve(H)([B1, B1], t=[0.0, time])
```

passes one `B1` value to each time-dependent coefficient and integrates the
Schrodinger equation from zero to the requested final time. The QNode then
returns the probabilities of measuring `|0>` and `|1>`.

## Human-run setup and validation

This challenge requires JAX, which is intentionally isolated from the shared
repository requirements. From the repository root, run:

```powershell
.\.venv\Scripts\python.exe -m pip install -r challenges\Group2\05_nuclear_magnetic_resonance\requirements.txt
.\.venv\Scripts\python.exe challenges\Group2\05_nuclear_magnetic_resonance\submission.py
.\.venv\Scripts\python.exe -m pytest challenges\Group2\05_nuclear_magnetic_resonance\test_solution.py -v
```

The submission harness should report `Correct!` for both public cases. Submit
the contents of `submission.py`.

