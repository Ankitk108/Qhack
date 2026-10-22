# QHack Challenge Solutions

This repository contains self-contained, tested QHack challenge solutions.
Every challenge directory includes its full question, implementation, and
additional regression tests.

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

## Challenge structure

Each `challenges/<group>/<challenge>/` directory contains:

- `QUESTION.md`: the complete formatted problem statement;
- `submission.py`: the maintained solution, original public grader, and public cases;
- `test_solution.py`: additional regression and edge-case tests;
- `README.md`: a concise explanation and local run instructions.

## Challenge index

### Group 1

| Challenge | Description | Run |
| --- | --- | --- |
| [Goal or No Goal?](challenges/Group1/01_goal_or_no_goal/QUESTION.md) | Prepare a GHZ state and construct its stabilizer parity checks. | `.\.venv\Scripts\python.exe challenges\Group1\01_goal_or_no_goal\submission.py` |
| [Playing Period](challenges/Group1/02_playing_period/QUESTION.md) | Build the four-qubit quantum Fourier transform from elementary gates. | `.\.venv\Scripts\python.exe challenges\Group1\02_playing_period\submission.py` |
| [Fermionic VQE](challenges/Group1/03_fermionic_vqe/QUESTION.md) | Map a fermionic Hamiltonian to qubits and variationally find its ground energy. | `.\.venv\Scripts\python.exe challenges\Group1\03_fermionic_vqe\submission.py` |
| [The Draft Lottery](challenges/Group1/04_the_draft_lottery/QUESTION.md) | Read all eigenphases in a superposition and price the faintest spectral peak. | `.\.venv\Scripts\python.exe challenges\Group1\04_the_draft_lottery\submission.py` |
| [The Hidden Subgroup Stage](challenges/Group1/05_the_hidden_subgroup_stage/QUESTION.md) | Score how well labeled binary data respects a candidate XOR symmetry. | `.\.venv\Scripts\python.exe challenges\Group1\05_the_hidden_subgroup_stage\submission.py` |
| [Diffuse and Conquer](challenges/Group1/06_diffuse_and_conquer/QUESTION.md) | Approximate one backward-Euler diffusion-reaction step with QSVT matrix inversion. | `.\.venv\Scripts\python.exe challenges\Group1\06_diffuse_and_conquer\submission.py` |
| [Grover's little helper](challenges/Group1/07_grovers_little_helper/QUESTION.md) | Use one ancilla to solve the half-marked two-qubit Grover case exactly. | `.\.venv\Scripts\python.exe challenges\Group1\07_grovers_little_helper\submission.py` |

### Group 2

| Challenge | Description | Run |
| --- | --- | --- |
| [Building a quantum kernel](challenges/Group2/01_building_a_quantum_kernel/QUESTION.md) | Evaluate state-overlap kernels and assemble pairwise kernel matrices. | `.\.venv\Scripts\python.exe challenges\Group2\01_building_a_quantum_kernel\submission.py` |
| [Keep your own score](challenges/Group2/02_keep_your_own_score/QUESTION.md) | Reconstruct Pauli-word expectations from computational-basis probabilities. | `.\.venv\Scripts\python.exe challenges\Group2\02_keep_your_own_score\submission.py` |
| [Nuclear magnetic resonance](challenges/Group2/05_nuclear_magnetic_resonance/QUESTION.md) | Evolve a spin under a time-dependent NMR Hamiltonian. | `.\.venv\Scripts\python.exe challenges\Group2\05_nuclear_magnetic_resonance\submission.py` |
| [The scouting report](challenges/Group2/03_the_scouting_report/QUESTION.md) | Reconstruct one wire's Bloch vector and purity using expectation values only. | `.\.venv\Scripts\python.exe challenges\Group2\03_the_scouting_report\submission.py` |
| [A relay of phases](challenges/Group2/04_a_relay_of_phases/QUESTION.md) | Build an IQP circuit from commuting Pauli-X rotations and optimize its parameters. | `.\.venv\Scripts\python.exe challenges\Group2\04_a_relay_of_phases\submission.py` |
| [Approximation ratio for QAOA](challenges/Group2/07_approximation_ratio_for_qaoa/QUESTION.md) | Compare depth-four QAOA against the exact minimum-vertex-cover ground energy. | `.\.venv\Scripts\python.exe challenges\Group2\07_approximation_ratio_for_qaoa\submission.py` |
| [A basket of options](challenges/Group2/06_a_basket_of_options/QUESTION.md) | Estimate a correlated two-asset basket option with quantum Monte Carlo. | `.\.venv\Scripts\python.exe challenges\Group2\06_a_basket_of_options\submission.py` |

### Group 3

| Challenge | Description | Run |
| --- | --- | --- |
| [My First Quantum Neural Network](challenges/Group3/01_my_first_quantum_neural_network/QUESTION.md) | Build a one-qubit encoding and trainable layer. | `.\.venv\Scripts\python.exe challenges\Group3\01_my_first_quantum_neural_network\submission.py` |
| [Personal Best (Bronze)](challenges/Group3/02_personal_best_bronze/QUESTION.md) | Synthesize arbitrary unitaries below the Shannon cost baseline. | Supplied submission retained with exploit warning |
| [Same Kit, Different Number](challenges/Group3/03_same_kit_different_number/QUESTION.md) | Detect a global phase and expose it through phase kickback. | `.\.venv\Scripts\python.exe challenges\Group3\03_same_kit_different_number\submission.py` |
| [Break the Tie](challenges/Group3/04_break_the_tie/QUESTION.md) | Resolve the mirror-phase ambiguity in amplitude estimation. | `.\.venv\Scripts\python.exe challenges\Group3\04_break_the_tie\submission.py` |
| [Personal Best (Silver)](challenges/Group3/05_personal_best_silver/QUESTION.md) | Meet the Silver target for arbitrary-unitary synthesis cost. | `.\.venv\Scripts\python.exe challenges\Group3\05_personal_best_silver\submission.py` |
| [The Salary Cap](challenges/Group3/06_the_salary_cap/QUESTION.md) | Find the largest affordable QPE precision using symbolic resource estimation. | `.\.venv\Scripts\python.exe challenges\Group3\06_the_salary_cap\submission.py` |
| [Implementing POVMs](challenges/Group3/07_implementing_povms/QUESTION.md) | Realize a three-outcome POVM through a two-qubit unitary dilation. | `.\.venv\Scripts\python.exe challenges\Group3\07_implementing_povms\submission.py` |
| [Personal Best (Gold)](challenges/Group3/08_personal_best_gold/QUESTION.md) | Meet the Gold target for arbitrary-unitary synthesis cost. | `.\.venv\Scripts\python.exe challenges\Group3\08_personal_best_gold\submission.py` |
| [Pulse Optimization](challenges/Group3/09_pulse_optimization/QUESTION.md) | Optimize a parametrized pulse Hamiltonian for a target state. | `.\.venv\Scripts\python.exe challenges\Group3\09_pulse_optimization\submission.py` |

## Adding another challenge

Create `challenges/<group>/<descriptive_name>/` containing `QUESTION.md`,
`submission.py`, `test_solution.py`, and a concise `README.md`. Shared
dependencies belong in the root requirement files. Add a challenge-local
requirements file only when the challenge needs dependencies not shared by the
rest of the repository.

