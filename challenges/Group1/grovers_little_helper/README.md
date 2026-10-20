# Grover's Little Helper

## Why ordinary Grover search fails here

Let `|M>` and `|U>` denote normalized uniform superpositions over the two
marked and two unmarked states. The initial two-qubit state is

$$
|\psi\rangle=\frac{|M\rangle+|U\rangle}{\sqrt2}.
$$

The oracle produces

$$
O|\psi\rangle=\frac{-|M\rangle+|U\rangle}{\sqrt2}.
$$

Because marked and unmarked states already have equal total probability, an
ordinary Grover iteration cannot amplify the marked half.

## Ancilla construction

Prepare the ancilla in `|+>` and apply the oracle only when it is `|1>`. A
second Hadamard on the ancilla produces

$$
\frac{|0\rangle(|\psi\rangle+O|\psi\rangle)
      +|1\rangle(|\psi\rangle-O|\psi\rangle)}{2}
=\frac{|0\rangle|U\rangle+|1\rangle|M\rangle}{\sqrt2}.
$$

The ancilla now tells us whether the search register is unmarked or marked.
For a half-marked database, reflection about `|psi>` swaps `|U>` and `|M>` up
to an irrelevant phase. Applying the diffuser only when the ancilla is zero
therefore maps both branches into the marked subspace. Measuring the first two
wires returns a solution with probability one.

## Human-run validation

From the repository root:

```powershell
.\.venv\Scripts\python.exe challenges\grovers_little_helper\submission.py
.\.venv\Scripts\python.exe -m pytest challenges\grovers_little_helper\test_solution.py -v
```

The supplied harness performs 1000 one-shot executions and may take longer
than earlier challenges. Submit the contents of `submission.py`.

