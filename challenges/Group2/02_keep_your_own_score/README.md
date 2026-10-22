# Keep Your Own Score

## Goal

Measure a three-qubit Pauli word without using `expval`. The implementation
prepares the supplied state, rotates each non-Z Pauli measurement into the
computational basis, obtains all eight probabilities, and performs the parity
sum classically.

## Basis changes

| Factor | Label | Gates before measurement |
| --- | --- | --- |
| `I` | `none` | none |
| `Z` | `none` | none |
| `X` | `H` | Hadamard |
| `Y` | `SH` | adjoint-S, then Hadamard |

The basis label alone does not decide parity participation: `Z` participates
even though it requires no gate, while `I` is skipped.

## Classical parity

For outcome index `b`, wire `w` contains

$$
\operatorname{bit}(b,w)=\left(b\mathbin{\gg}(2-w)\right)\mathbin{\&}1.
$$

If `W` is the set of non-identity wires, the sign is

$$
s_b=(-1)^{\sum_{w\in W}\operatorname{bit}(b,w)}.
$$

The expectation value is reconstructed as

$$
\langle P\rangle=\sum_{b=0}^{7}p_b s_b.
$$

## Human-run validation

From the repository root:

```powershell
.\.venv\Scripts\python.exe challenges\Group2\02_keep_your_own_score\submission.py
.\.venv\Scripts\python.exe -m pytest challenges\Group2\02_keep_your_own_score\test_solution.py -v
```

The first command should report `Correct!` for both public cases. Submit the
contents of `submission.py`.

