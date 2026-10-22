# Question 2: Personal Best (Bronze)

**Points:** 100pts

## Question

Synthesize arbitrary Haar-random unitaries on 2, 3, 4, and 5 data qubits
using a Clifford+T-style cost model. After PennyLane decomposition, arbitrary
RX, RY, or RZ rotations cost 44 T-equivalents, a T gate costs 1, and Clifford
gates plus global phase cost zero. Each auxiliary wire doubles the full cost:

$$C=(44N_{\mathrm{rot}}+N_T)2^{N_{\mathrm{aux}}}.$$

The Shannon-decomposition baseline is

$$C_{\mathrm{base}}(n)=44\left(\frac{21}{16}4^n-3\,2^{n-1}\right),$$

which is 13,728 at four qubits. A Bronze result must implement every tested
unitary, including global phase, with entrywise error at most `1e-8`, stay at or
below the baseline at every size, have a saving that never shrinks as the
system grows, and save at least 5% at five qubits.

### Resource constraints

- The target gate set is RX, RY, RZ, T, S, H, X, Y, Z, CNOT, and GlobalPhase.
- At most eight total wires may be used.
- Auxiliary wires start and finish in $|0\rangle$.
- The decomposed circuit may contain at most 100,000 gates.
- `submission_circ` must use exact construction rather than fitting the public matrices.

### Challenge task

Complete `submission_circ(u_mat)`. It must queue a circuit implementing the
given $2^n\times2^n$ unitary on wires `0` through `n-1` and return `None`.

### Input and output

The harness input is `[seed, num_samples]`. It tests `num_samples` Haar-random
unitaries at each size using the specified seed and reports grade, savings by
size, cost, baseline, maximum error, and auxiliary-wire usage.

### Public cases

The public inputs are `[2026, 2]` and `[7, 2]`. A valid Bronze solution must
reach at least 5% saving at five qubits on both without depending on the seed.
