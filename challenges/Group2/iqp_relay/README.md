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

The number of trainable parameters is `len(pattern)`. Adam begins from a fixed
nonzero vector, avoiding the stationary point that can occur when every
rotation begins at zero, and minimizes the QNode expectation value directly.

## Human-run validation

From the repository root:

```powershell
.\.venv\Scripts\python.exe challenges\Group2\iqp_relay\submission.py
.\.venv\Scripts\python.exe -m pytest challenges\Group2\iqp_relay\test_solution.py -v
```

The first command should report `Correct!` for both public cases. Submit the
contents of `submission.py`.

