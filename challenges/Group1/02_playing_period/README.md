# Four-Qubit Quantum Fourier Transform

## Task

Implement the four-qubit QFT on wires `[0, 1, 2, 3]` using only Hadamard,
controlled phase-shift, and SWAP gates. PennyLane's built-in `QFT` operation is
not allowed.

The target transformation is

$$
|x\rangle \longmapsto \frac{1}{\sqrt{2^n}}
\sum_{y=0}^{2^n-1} e^{2\pi ixy/2^n}|y\rangle,
$$

with `n = 4`. The final SWAP gates correct the reversed wire order produced by
the standard elementary-gate construction.

## Circuit

For each target wire from `0` through `3`, apply a Hadamard and then controlled
phase shifts from every higher-numbered wire. A control at distance `d` uses
the angle

$$
\theta_d = \frac{\pi}{2^d}.
$$

Finally swap wires `(0, 3)` and `(1, 2)`.

## Local validation and submission

Run the supplied-style grader harness from the repository root:

```powershell
.\.venv\Scripts\python.exe challenges\Group1\02_playing_period\submission.py
```

Expected result:

```text
Running test case 0 with input 'No input'...
Correct!
```

Submit the contents of `submission.py`. It preserves the challenge's required
function and grader order.

