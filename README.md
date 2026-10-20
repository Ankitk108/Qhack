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

### Group 1

| Challenge | Description | Run |
| --- | --- | --- |
| [GHZ verification](challenges/Group1/ghz_verification/README.md) | Prepare a GHZ state and construct its stabilizer parity checks. | `.\.venv\Scripts\python.exe challenges\Group1\ghz_verification\solution.py 3` |
| [Four-qubit QFT](challenges/Group1/qft_four_qubits/README.md) | Build the four-qubit quantum Fourier transform from elementary gates. | `.\.venv\Scripts\python.exe challenges\Group1\qft_four_qubits\submission.py` |
| [Fermionic VQE](challenges/Group1/fermionic_vqe/README.md) | Map a fermionic Hamiltonian to qubits and variationally find its ground energy. | `.\.venv\Scripts\python.exe challenges\Group1\fermionic_vqe\submission.py` |
| [QPE spectrum reader](challenges/Group1/qpe_spectrum/README.md) | Read all eigenphases in a superposition and price the faintest spectral peak. | `.\.venv\Scripts\python.exe challenges\Group1\qpe_spectrum\submission.py` |
| [Hidden-subgroup symmetry score](challenges/Group1/hsp_symmetry_score/README.md) | Score how well labeled binary data respects a candidate XOR symmetry. | `.\.venv\Scripts\python.exe challenges\Group1\hsp_symmetry_score\submission.py` |
| [QSVT diffusion solver](challenges/Group1/qsvt_diffusion/README.md) | Approximate one backward-Euler diffusion-reaction step with QSVT matrix inversion. | `.\.venv\Scripts\python.exe challenges\Group1\qsvt_diffusion\submission.py` |
| [Grover's little helper](challenges/Group1/grovers_little_helper/README.md) | Use one ancilla to solve the half-marked two-qubit Grover case exactly. | `.\.venv\Scripts\python.exe challenges\Group1\grovers_little_helper\submission.py` |

### Group 2

| Challenge | Description | Run |
| --- | --- | --- |
| [Building a quantum kernel](challenges/Group2/quantum_kernel/README.md) | Evaluate state-overlap kernels and assemble pairwise kernel matrices. | `.\.venv\Scripts\python.exe challenges\Group2\quantum_kernel\submission.py` |
| [Keep your own score](challenges/Group2/pauli_from_probabilities/README.md) | Reconstruct Pauli-word expectations from computational-basis probabilities. | `.\.venv\Scripts\python.exe challenges\Group2\pauli_from_probabilities\submission.py` |
| [Nuclear magnetic resonance](challenges/Group2/nmr_evolution/README.md) | Evolve a spin under a time-dependent NMR Hamiltonian. | `.\.venv\Scripts\python.exe challenges\Group2\nmr_evolution\submission.py` |

## Adding another challenge

Create `challenges/<group>/<descriptive_name>/` containing a `solution.py`, a
README, and `test_solution.py`. Shared dependencies belong in the root
requirement files. Add a challenge-local requirements file only when the
challenge needs dependencies that are not shared by the rest of the repository.

