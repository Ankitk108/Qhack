# Question 7: Grover's Little Helper

**Points:** 400pts

## Question

Grover search normally prepares a uniform superposition, applies a phase oracle, and uses a diffusion operator to amplify marked states. Its familiar quadratic advantage breaks down in the special case where exactly half of the database is marked: ordinary Grover iterations do not increase the total marked probability.

This challenge considers a two-qubit search register with basis states

$$|00\rangle,|01\rangle,|10\rangle,|11\rangle,$$

exactly two of which are marked by an unknown supplied oracle. One auxiliary qubit is sufficient to separate the marked and unmarked branches coherently and turn both into marked states.

### Challenge task

Complete the QNode `circuit(generator, oracle, diffuser)`. It must:

- use only one auxiliary qubit;
- call the oracle once;
- call the diffuser once;
- use one measurement shot; and
- return `qp.counts` for the first two wires, always producing a marked state.

`generator()` prepares the uniform state, `oracle()` marks the two solutions, and `diffuser(generator)` reflects about the initial state. All three supplied callables act on the first two wires.

### Input

There is no serialized input; the three circuit-building functions are supplied directly.

### Output

A counts dictionary for wires `[0, 1]` containing the single measured bit string.

### Evaluation

The grader generates 1000 oracle instances and checks that every one-shot measurement is a valid marked state. There are no separate public and private numerical cases.
