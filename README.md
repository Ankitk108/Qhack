# QHack Challenge Solutions

This repository contains independent, tested solutions to QHack challenges. Each
challenge lives in its own directory with its implementation, explanation, and
tests.

## Setup (Windows PowerShell)

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

## Run all tests

```powershell
.\.venv\Scripts\python.exe -m pytest
```

## Challenges

| Challenge | Description | Run |
| --- | --- | --- |
| [GHZ verification](challenges/ghz_verification/README.md) | Prepare a GHZ state and construct its stabilizer parity checks. | `.\.venv\Scripts\python.exe challenges\ghz_verification\solution.py 3` |
| [Four-qubit QFT](challenges/qft_four_qubits/README.md) | Build the four-qubit quantum Fourier transform from elementary gates. | `.\.venv\Scripts\python.exe challenges\qft_four_qubits\submission.py` |
| [Fermionic VQE](challenges/fermionic_vqe/README.md) | Map a fermionic Hamiltonian to qubits and variationally find its ground energy. | `.\.venv\Scripts\python.exe challenges\fermionic_vqe\submission.py` |
| [QPE spectrum reader](challenges/qpe_spectrum/README.md) | Read all eigenphases in a superposition and price the faintest spectral peak. | `.\.venv\Scripts\python.exe challenges\qpe_spectrum\submission.py` |
| [Hidden-subgroup symmetry score](challenges/hsp_symmetry_score/README.md) | Score how well labeled binary data respects a candidate XOR symmetry. | `.\.venv\Scripts\python.exe challenges\hsp_symmetry_score\submission.py` |
| [QSVT diffusion solver](challenges/qsvt_diffusion/README.md) | Approximate one backward-Euler diffusion-reaction step with QSVT matrix inversion. | `.\.venv\Scripts\python.exe challenges\qsvt_diffusion\submission.py` |
| [Grover's little helper](challenges/grovers_little_helper/README.md) | Use one ancilla to solve the half-marked two-qubit Grover case exactly. | `.\.venv\Scripts\python.exe challenges\grovers_little_helper\submission.py` |

## Adding another challenge

Create `challenges/<descriptive_name>/` containing a `solution.py`, a README,
and `test_solution.py`. Shared dependencies belong in the root requirement
files. Add a challenge-local requirements file only when the challenge needs
dependencies that are not shared by the rest of the repository.

