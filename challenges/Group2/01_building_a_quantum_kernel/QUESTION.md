# Question 1: Building a Quantum Kernel

**Points:** 100pts

## Question

Kernel methods compare data through inner products in a feature space. In a support vector machine, mapping $x$ to $\phi(x)$ replaces the original inner product with

$$k(x_i,x_j)=\langle\phi(x_i),\phi(x_j)\rangle.$$

A quantum computer can represent the feature map as a state $|\phi(x)\rangle=S(x)|0\rangle$. The corresponding quantum kernel is the squared state overlap

$$k(x_i,x_j)=|\langle\phi(x_i)|\phi(x_j)\rangle|^2.$$

### Challenge task

Complete `quantum_kernel(x1, x2)`, a QNode returning this overlap kernel, and `kernel_matrix(X1, X2)`, which evaluates every pair and returns a matrix with entry $K_{ij}=k(X1_i,X2_j)$. Each datapoint has four real features encoded on four qubits.

### Input and output

The input is `[X1, X2]`, two possibly different-length collections of four-feature datapoints. Return a floating-point array of shape `(len(X1), len(X2))`.

### Public cases

The first case compares the same three-point dataset with itself and must return

```text
[[1.00000000, 0.76528062, 0.87759179],
 [0.76528062, 1.00000000, 0.77075905],
 [0.87759179, 0.77075905, 1.00000000]]
```

The second compares two different two-point datasets and must return

```text
[[0.71461545, 0.85406897],
 [0.89085434, 0.81902278]]
```

The checker uses relative tolerance `1e-4`.
