# A Relay of Phases

## Circuit construction

Each subset `S` in `pattern[j]` represents

$$
\exp\left(-\frac{i\theta_j}{2}\prod_{k\in S}X_k\right).
$$

PennyLane's `PauliRot` implements this operation directly. A subset of length
`m` uses the Pauli word `"X" * m`, its listed wires, and the shared parameter
`weights[j]`. All generators contain only Pauli-X factors, so every rotation
commutes even when subsets overlap.

The binary observable is translated into the product

$$
Z^a=\prod_{k:a_k=1}Z_k.
$$

The QNode returns its expectation value on the state produced from `|0000>`.
The built-in `IQP` template is never used.

## Optimization

The number of trainable parameters is `len(pattern)`. When the net Pauli-X
product of a parameter group anticommutes with the measured Pauli-Z word,
setting that shared parameter to $\pi$ and all others to zero prepares an exact
`-1` eigenstate. The optimizer detects and uses this deterministic global
minimum. If no individual group provides that construction, it falls back to
Adam from several nonzero starting points rather than trusting one local run.

## Human-run validation

From the repository root:

```powershell
.\.venv\Scripts\python.exe challenges\Group2\04_a_relay_of_phases\submission.py
.\.venv\Scripts\python.exe -m pytest challenges\Group2\04_a_relay_of_phases\test_solution.py -v
```

The first command should report `Correct!` for both public cases. Submit the
contents of `submission.py`.

