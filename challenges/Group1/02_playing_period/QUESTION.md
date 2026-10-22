# Question 2: Playing Period

**Points:** 100pts

## Question

The Quantum Fourier Transform (QFT) is a central subroutine in algorithms such as quantum phase estimation and Shor's factoring algorithm. For an $n$-qubit computational-basis state, it acts as

$$|x\rangle\longmapsto\frac{1}{\sqrt{2^n}}\sum_{y=0}^{2^n-1}e^{2\pi ixy/2^n}|y\rangle.$$

PennyLane provides this transformation as a built-in operation, but this challenge requires constructing the four-qubit QFT directly from elementary gates. Only the following operations may be used:

- `qp.Hadamard`
- `qp.ControlledPhaseShift`
- `qp.SWAP`

### Challenge task

Complete `qft_four_qubits()` so that it applies the QFT to wires `[0, 1, 2, 3]`. The function must not use `qp.QFT`. The standard elementary-gate construction naturally produces the output wires in reverse order, so the circuit must include the appropriate final SWAP gates to agree with PennyLane's QFT convention.

The function applies gates to the active circuit and does not return a value.

### Input

There is no input.

### Output

There is no direct output. The grader reconstructs the unitary matrix of the submitted circuit and compares it with the matrix produced by `qp.QFT(wires=range(4))`. It also checks that the built-in QFT operation does not appear in the circuit.

### Public cases

There are no numerical input/output cases because the submitted object is a circuit transformation. The supplied grader performs the complete matrix comparison with absolute tolerance `1e-3`.
