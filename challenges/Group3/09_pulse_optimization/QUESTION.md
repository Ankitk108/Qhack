Pulse Optimization
Complete
400pts
Instructions
Submissions
Resources
Challenge statement
Pulse programming is used as a method of controlling quantum operations in quantum systems. Essentially, a time-dependent electromagnetic field is applied to the quantum degrees of freedom, the state of whom are governed by time-dependent SchrÃ¶dinger equation:

âˆ‚
âˆ‚
t
âˆ£
Ïˆ
âŸ©
=
âˆ’
i
H
(
t
)
âˆ£
Ïˆ
âŸ©
,
âˆ‚t
âˆ‚
â€‹
 âˆ£ÏˆâŸ©=âˆ’iH(t)âˆ£ÏˆâŸ©,
where 
H
H is the Hamiltonian that describes the system interacting with its environment.

In this challenge, we're going to give you a Hamiltonian with tunable parameters (akin to tuning the electromagnetic field) and ask you to turn the knobs, let a quantum state evolve for some time, and generate a desired output state. You'll want to have the documentation for qp.pulse handy if you're not familiar with it already!

Ok, so here's the deal. You're in the lab with a one-qubit pulse-programmable quantum computer. The Hamiltonian governing your system is this:

H
(
t
)
=
p
0
t
X
+
p
1
t
2
Y
+
p
2
t
3
Z
,
H(t)=p 
0
â€‹
 tX+p 
1
â€‹
 t 
2
 Y+p 
2
â€‹
 t 
3
 Z,
where 
t
=
2
t=2 â€” this is hard-coded â€” and 
p
i
p 
i
â€‹
  are tunable parameters. Your job is to evolve the 
âˆ£
0
âŸ©
âˆ£0âŸ© state for the given time and obtain a given target state, 
âˆ£
Ïˆ
âŸ©
âˆ£ÏˆâŸ©:

exp
â¡
(
âˆ’
i
H
(
t
)
t
)
âˆ£
0
âŸ©
=
âˆ£
Ïˆ
âŸ©
.
exp(âˆ’iH(t)t)âˆ£0âŸ©=âˆ£ÏˆâŸ©.
To do this, you have to turn some knobs and figure out what the optimal values of 
p
i
p 
i
â€‹
  are by maximizing the fidelity between 
âˆ£
Ïˆ
âŸ©
âˆ£ÏˆâŸ© and 
exp
â¡
(
âˆ’
i
H
(
t
)
t
)
âˆ£
0
âŸ©
exp(âˆ’iH(t)t)âˆ£0âŸ© (or, equivalently, minimizing the negative of the fidelity) with respect to the parameters 
p
i
p 
i
â€‹
 :

F
=
âˆ£
âŸ¨
Ïˆ
âˆ£
exp
â¡
(
âˆ’
i
H
(
t
)
t
)
âˆ£
0
âŸ©
 
âˆ£
2
.
F=âˆ£âŸ¨Ïˆâˆ£exp(âˆ’iH(t)t)âˆ£0âŸ© âˆ£ 
2
 .
The maximum value of 
F
F is 
1
1.

Challenge code
In the code below you must complete the following functions:

hamiltonian: this function creates the time-dependent Hamiltonian provided in the description above. Create it similarly to what's outlined in the qp.pulse documentation.
circuit: this is a QNode that will only have one operation: an instance of qp.evolve that requires the Hamiltonian from the hamiltonian function. This QNode returns qp.state().
cost: this function takes the output of circuit and target_state and calculates the fidelity. Check out the qp.math.fidelity_statevector function in PennyLane's documentation.
Input
As input to this challenge, you are given the target state (list(float)) that circuit must produce.

Output
Your code will output the parameters 
p
i
p 
i
â€‹
  (list(float)) such that 
exp
â¡
(
âˆ’
i
H
(
t
)
t
)
âˆ£
0
âŸ©
=
âˆ£
Ïˆ
âŸ©
exp(âˆ’iH(t)t)âˆ£0âŸ©=âˆ£ÏˆâŸ©.

Test cases
The following public test cases are available to you. Note that there are additional hidden test cases that we use to verify that your code is valid in full generality.

test_input: [0.11775969, 0.99304212]
expected_output: [0.0, 0.062368193925808904, 0.0]
test_input: [0.7071067812, 0.7071067812]
sample_output:, [0.0, 0.26666667860250887, 0.0], 
Your circuit QNode must only contain 1 operation (an instance of qp.evolve). If your solution matches the correct one within the 1e-4 relative error tolerance, the output will be "Success!". Otherwise, you will receive an "Incorrect" prompt.

Good luck!
