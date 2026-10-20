# GHZ State Verification

## Task

Prepare the `n`-qubit GHZ state

$$
|\mathrm{GHZ}_n\rangle = \frac{|0\ldots0\rangle + |1\ldots1\rangle}{\sqrt{2}}
$$

and return the `n` stabilizer checks that certify it:

$$
X_0X_1\cdots X_{n-1}, \qquad Z_iZ_{i+1}\quad (i=0,\ldots,n-2).
$$

The adjacent Z parities constrain the populations to the all-zero and all-one
branches. The global X parity tests the coherence and relative phase between
those branches. Their mean is `1.0` for the correctly prepared GHZ state.

## Run

From the repository root:

```powershell
.\.venv\Scripts\python.exe challenges\ghz_verification\solution.py 3
```

Expected output:

```text
1.0
```

The public examples use `n=3` and `n=5`; both produce `1.0` within floating
point tolerance.

## Submission

Use `submission.py` for the challenge platform. It preserves the supplied
wrapper, solution function, audit code, and public-test order. The only filled
section is `prepare_and_build_checks`, as required by the challenge template.

