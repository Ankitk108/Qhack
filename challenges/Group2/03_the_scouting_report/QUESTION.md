# Question 3: The Scouting Report

**Points:** 100pts

## Question

A single-qubit state is determined by its Bloch vector:

$$\rho=\tfrac12(I+r_xX+r_yY+r_zZ),\qquad r_i=\operatorname{Tr}(\rho\sigma_i)=\langle\sigma_i\rangle.$$

Its purity is

$$\operatorname{Tr}(\rho^2)=\tfrac12(1+r_x^2+r_y^2+r_z^2).$$

A pure reduced state has purity `1`; a maximally mixed qubit has zero Bloch vector and purity `1/2`. A qubit belonging to an entangled pair may therefore be locally mixed even when the global state is pure.

### Challenge task

Complete `bloch_and_purity(prep, num_wires, target_wire)`. Treat `prep` as a black box, measure X, Y, and Z expectation values on the requested wire, and return the Bloch vector followed by its purity. The target is not necessarily wire 0 and the register may contain more than two wires.

Only `qp.expval` measurements are allowed. State, density-matrix, probability, and built-in purity measurements are forbidden.

### Input and output

The platform converts a gate-description dictionary into `prep`, infers the register width, and passes the requested target wire. Return `([r_x,r_y,r_z], purity)` with absolute tolerance `1e-5`.
