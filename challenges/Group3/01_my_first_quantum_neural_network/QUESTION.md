# Question 1: My First Quantum Neural Network

**Points:** 100pts

## Question

A single layer of a quantum neural network combines a data-encoding block
$S(x)$ with a trainable block $A(\vec\theta)$. In this single-qubit challenge,
the encoding is an RX rotation and the trainable block is an Euler-angle
sequence of RZ, RY, and RZ rotations.

### Challenge task

Complete three quantum functions:

1. `encoding_circuit(x)` applies $S(x)=R_X(x)$ on wire 0.
2. `training_circuit(theta_vec)` applies
   $A(\vec\theta)=R_Z(\theta_1)R_Y(\theta_2)R_Z(\theta_3)$ on wire 0.
3. `quantum_neural_network(x, theta_vec)` applies the encoding followed by the
   trainable block and returns $\langle Z\rangle$.

The two circuit-building functions queue gates and return nothing. The main
function is a QNode on a one-wire `default.qubit` device.

### Input

The serialized input is `[x, theta_1, theta_2, theta_3]`, where all entries are
floating-point values.

### Output

A PennyLane NumPy tensor containing the Pauli-Z expectation value.

### Public cases

| Input | Expected output |
|---|---:|
| `[0.4859371, 1.32682562, -1.06015833, -4.41959946]` | `0.827549` |
| `[-0.72318627, -4.91395046, -5.0609724, 0.1125593]` | `0.865457` |

The checker uses relative tolerance `1e-4`.
