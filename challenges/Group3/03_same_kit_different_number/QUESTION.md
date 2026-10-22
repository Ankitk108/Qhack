Same Kit, Different Number
Complete
100pts
Instructions
Submissions
Resources
Two different matrices can be the same gate.

If 
V
=
e
i
Î±
U
V=e 
iÎ±
 U for some real 
Î±
Î±, then 
U
U and 
V
V act identically on every state, and no measurement performed on that qubit can tell them apart. The reason is that measurement probabilities are built from squared magnitudes: for any state 
âˆ£
Ïˆ
âŸ©
âˆ£ÏˆâŸ© and any observable, the phase 
e
i
Î±
e 
iÎ±
  appears once in the amplitude and once, conjugated, in its complex conjugate, so it cancels:

âˆ£
âŸ¨
Ï•
âˆ£
V
âˆ£
Ïˆ
âŸ©
âˆ£
2
=
âˆ£
e
i
Î±
âˆ£
2
âˆ£
âŸ¨
Ï•
âˆ£
U
âˆ£
Ïˆ
âŸ©
âˆ£
2
=
âˆ£
âŸ¨
Ï•
âˆ£
U
âˆ£
Ïˆ
âŸ©
âˆ£
2
.
âˆ£âŸ¨Ï•âˆ£Vâˆ£ÏˆâŸ©âˆ£ 
2
 = 
â€‹
 e 
iÎ±
  
â€‹
  
2
 âˆ£âŸ¨Ï•âˆ£Uâˆ£ÏˆâŸ©âˆ£ 
2
 =âˆ£âŸ¨Ï•âˆ£Uâˆ£ÏˆâŸ©âˆ£ 
2
 .
This is why 
âˆ’
H
âˆ’H and 
H
H are the same gate, and why qp.matrix returning a matrix that differs from yours by a sign may not be an error.

Turning a global phase into a relative phase
A global phase multiplies the whole state, so it drops out in the measurement process. A relative phase between two branches of a superposition does not. This is effectively what gives rise to interference effects in the measurement process at the end of a quantum computation. Controlling a gate converts the former into the latter.

Suppose 
M
=
e
i
Î±
I
M=e 
iÎ±
 I and put the control wire in 
âˆ£
+
âŸ©
âˆ£+âŸ© with the target in 
âˆ£
0
âŸ©
âˆ£0âŸ©. The controlled operation acts on the 
âˆ£
1
âŸ©
âˆ£1âŸ© branch only:

c
t
r
l
(
M
)
â€‰
âˆ£
0
âŸ©
+
âˆ£
1
âŸ©
2
âŠ—
âˆ£
0
âŸ©
=
âˆ£
0
âŸ©
+
e
i
Î±
âˆ£
1
âŸ©
2
âŠ—
âˆ£
0
âŸ©
.
ctrl(M) 
2
â€‹
 
âˆ£0âŸ©+âˆ£1âŸ©
â€‹
 âŠ—âˆ£0âŸ©= 
2
â€‹
 
âˆ£0âŸ©+e 
iÎ±
 âˆ£1âŸ©
â€‹
 âŠ—âˆ£0âŸ©.
The target remains untouched, but the control now carries a relative phase 
Î±
Î±. A second Hadamard turns that phase into an observable measure of population,

H
â€‰
âˆ£
0
âŸ©
+
e
i
Î±
âˆ£
1
âŸ©
2
=
cos
â¡
(
Î±
2
)
e
i
Î±
/
2
âˆ£
0
âŸ©
âˆ’
i
sin
â¡
(
Î±
2
)
e
i
Î±
/
2
âˆ£
1
âŸ©
,
H 
2
â€‹
 
âˆ£0âŸ©+e 
iÎ±
 âˆ£1âŸ©
â€‹
 =cos( 
2
Î±
â€‹
 )e 
iÎ±/2
 âˆ£0âŸ©âˆ’isin( 
2
Î±
â€‹
 )e 
iÎ±/2
 âˆ£1âŸ©,
so the probability of reading 
1
1 on the control is

P
(
1
)
=
sin
â¡
2
(
Î±
2
)
.
P(1)=sin 
2
 ( 
2
Î±
â€‹
 ).
This is the mechanism behind phase kickback, and behind quantum algorithms that read an eigenvalue out of a controlled unitary.

Challenge statement
You are handed two 
2
Ã—
2
2Ã—2 unitaries, 
U
U and 
V
V. You will need to construct the quantity

M
=
V
U
â€ 
,
M=VU 
â€ 
 ,
and answer the following three questions.

Is 
V
V the same gate as 
U
U up to a global phase?
If so, what is that phase 
Î±
Î±, folded into the range 
[
0
,
2
Ï€
)
[0,2Ï€)? If not, report 0.0.
Implement the phase kickback circuit described above with the control and target wires initialised as |0>. What is the probability of measuring 1 on the control wire?
control: 
âˆ£
0
âŸ©
âŸ¶
H
âŸ¶
âˆ™
âŸ¶
H
âŸ¶
measure
control: âˆ£0âŸ©âŸ¶HâŸ¶âˆ™âŸ¶HâŸ¶measure
target: 
âˆ£
0
âŸ©
âŸ¶
M
target: âˆ£0âŸ©âŸ¶M
Challenge code
You must complete this function:

same_gate_and_phase: returns the verdict, the phase, and the control probability. Its arguments are:

u_matrix (np.ndarray): a 
2
Ã—
2
2Ã—2 complex unitary.
v_matrix (np.ndarray): a 
2
Ã—
2
2Ã—2 complex unitary.
Input
Each test case is a Python dict with two keys, "u" and "v". Each matrix is written as a list of 2 rows, each row a list of 2 entries, and each entry a [real, imaginary] pair of floats. The second public test case, 
U
=
X
U=X and 
V
=
Z
V=Z, looks like this:

{
    "u": [[[0.0, 0.0], [1.0, 0.0]],
          [[1.0, 0.0], [0.0, 0.0]]],
    "v": [[[1.0, 0.0], [0.0, 0.0]],
          [[0.0, 0.0], [-1.0, 0.0]]],
}
You never handle that pair format yourself. The grading code converts both matrices into single complex np.ndarrays before calling your function, so u_matrix and v_matrix arrive as ordinary 
2
Ã—
2
2Ã—2 arrays of complex numbers.

The two public test cases are 
U
=
H
U=H with 
V
=
âˆ’
H
V=âˆ’H (the same gate, with 
Î±
=
Ï€
Î±=Ï€), and 
U
=
X
U=X with 
V
=
Z
V=Z (not the same gate). The remaining cases are hidden.

Output
Return a tuple of three plain Python values:

(same_gate, alpha, p_one)
same_gate (bool): whether 
V
V is 
U
U up to a global phase.
alpha (float): the phase in 
[
0
,
2
Ï€
)
[0,2Ï€), or 0.0 when same_gate is False.
p_one (float): the probability of measuring 
1
1 on the control wire.
The two floats are compared to within a tolerance of 1e-5.

Good luck!
