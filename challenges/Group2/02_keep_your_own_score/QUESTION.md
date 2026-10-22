# Question 2: Keep Your Own Score

**Points:** 100pts

## Question

Quantum hardware measures computational-basis bits. Expectation values are reconstructed afterward. To measure a Pauli factor, rotate its eigenbasis to the Z basis: use no gate for `I` or `Z`, `H` for `X`, and $S^\dagger$ followed by `H` for `Y`.

For a three-qubit Pauli word, one probability circuit produces probabilities $p_b$ for outcomes $b=0,\ldots,7$. Its expectation is

$$\langle P\rangle=\sum_b s_b p_b,$$

where $s_b=(-1)^q$ and $q$ is the number of `1` bits on non-identity wires. Identity wires do not enter the parity; Z wires do enter even though they require no basis-change gate.

### Challenge task

Implement `measure_pauli_word(word, angles)` without using `expval`, state, or density-matrix measurements. Prepare the supplied three-qubit state, apply the basis changes, return `qp.probs(wires=[0,1,2])`, construct all eight parity signs using wire 0 as the most significant bit, and compute the expectation.

### Input and output

`word` is a three-character string over `I`, `X`, `Y`, `Z`; `angles` contains four floats. Return `(basis, signs, value)`. The identity word must return three `"none"` entries, eight `+1` signs, and value `1.0`.

### Public cases

- `ZIZ` with `[0.79, 2.75, 2.89, 0.33]` gives basis `['none','none','none']`, signs `[1,-1,1,-1,-1,1,-1,1]`, and value `0.931986472711103`.
- `XYI` with `[1.45,0.22,1.72,1.4]` gives basis `['H','SH','none']`, signs `[1,1,-1,-1,-1,-1,1,1]`, and value `0.9673999542626387`.

Values use absolute tolerance `1e-6`; basis and signs must match exactly.
