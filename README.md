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

## Adding another challenge

Create `challenges/<descriptive_name>/` containing a `solution.py`, a README,
and `test_solution.py`. Shared dependencies belong in the root requirement
files. Add a challenge-local requirements file only when the challenge needs
dependencies that are not shared by the rest of the repository.

