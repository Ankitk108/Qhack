# My First Quantum Neural Network

The model first encodes the scalar input with `RX(x)`, then applies the
trainable Euler-angle block `RZ-RY-RZ`, and finally measures Pauli Z.

Run from the repository root:

```powershell
.\.venv\Scripts\python.exe challenges\Group3\01_my_first_quantum_neural_network\submission.py
.\.venv\Scripts\python.exe -m pytest challenges\Group3\01_my_first_quantum_neural_network -q
```
