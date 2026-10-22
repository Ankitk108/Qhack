Implementing POVMs
Complete
400pts
Instructions
Submissions
Resources
Challenge Statement
In introductory courses on quantum theory, we quickly get acquainted with the concept of a projective measurement. To get on the same page, let's quickly review the topic.

When we measure an observable 
B
B acting on a quantum system 
S
S, the possible outcomes are its eigenstates 
{
âˆ£
b
0
âŸ©
,
âˆ£
b
1
âŸ©
,
â€¦
,
âˆ£
b
N
âŸ©
}
,
{âˆ£b 
0
â€‹
 âŸ©,âˆ£b 
1
â€‹
 âŸ©,â€¦,âˆ£b 
N
â€‹
 âŸ©}, which form an orthonormal basis of the Hilbert space that represents 
S
S. Bohr's rule postulates that the probability of observing the eigenstate 
âˆ£
b
i
âŸ©
âˆ£b 
i
â€‹
 âŸ© when the quantum system is in the state 
âˆ£
Ïˆ
âŸ©
âˆ£ÏˆâŸ© is

p
(
i
)
=
âˆ£
âŸ¨
b
i
âˆ£
Ïˆ
âŸ©
âˆ£
2
.
p(i)=âˆ£âŸ¨b 
i
â€‹
 âˆ£ÏˆâŸ©âˆ£ 
2
 .
Alternatively, defining 
P
i
=
âˆ£
b
i
âŸ©
âŸ¨
b
i
âˆ£
P 
i
â€‹
 =âˆ£b 
i
â€‹
 âŸ©âŸ¨b 
i
â€‹
 âˆ£, we can express

p
(
i
)
=
âŸ¨
Ïˆ
âˆ£
P
i
âˆ£
Ïˆ
âŸ©
.
p(i)=âŸ¨Ïˆâˆ£P 
i
â€‹
 âˆ£ÏˆâŸ©.
Note that the operators 
P
i
P 
i
â€‹
  are orthogonal projections, that is, they are Hermitian operators that satisfy

P
i
2
=
P
i
,
P 
i
2
â€‹
 =P 
i
â€‹
 ,
P
i
P
j
=
0
P 
i
â€‹
 P 
j
â€‹
 =0 when 
i
â‰ 
j
,
i
î€ 
=j,
âˆ‘
i
=
0
N
P
i
=
I
.
âˆ‘ 
i=0
N
â€‹
 P 
i
â€‹
 =I.
We can model this type of measurement on 
S
S by specifying the set 
{
P
i
}
{P 
i
â€‹
 } of projectors. This set is known as a projection-valued measure.

In more advanced courses in quantum theory, we learn that there are more general measurements we can perform, some of which can be modelled through a positive operator-valued measure, or POVM for short. Generalizing the above, the measurement is specified via a set 
{
E
i
}
i
=
0
N
{E 
i
â€‹
 } 
i=0
N
â€‹
  of positive hermitian operators such that

âˆ‘
i
=
0
N
E
i
=
I
.
i=0
âˆ‘
N
â€‹
 E 
i
â€‹
 =I.
The probabilities associated to the 
i
i-th measurement outcome are given by

p
(
i
)
=
âŸ¨
Ïˆ
âˆ£
E
i
âˆ£
Ïˆ
âŸ©
.
p(i)=âŸ¨Ïˆâˆ£E 
i
â€‹
 âˆ£ÏˆâŸ©.

In this challenge, we will construct a protocol that implements the measurement given by the POVM

E
0
=
Î±
âˆ£
1
âŸ©
âŸ¨
1
âˆ£
,
E
1
=
Î²
âˆ£
âˆ’
âŸ©
âŸ¨
âˆ’
âˆ£
,
E
2
=
I
âˆ’
E
0
âˆ’
E
1
,
E 
0
â€‹
 
E 
1
â€‹
 
E 
2
â€‹
 
â€‹
  
=Î±âˆ£1âŸ©âŸ¨1âˆ£,
=Î²âˆ£âˆ’âŸ©âŸ¨âˆ’âˆ£,
=Iâˆ’E 
0
â€‹
 âˆ’E 
1
â€‹
 ,
â€‹
 
on one qubit. Here, 
Î±
Î± and 
Î²
Î² are real numbers between 
0
0 and 
1
1.

The protocol consists of coupling the qubit to an auxiliary qubit, evolving the two-qubit joint system, and finally measuring the joint system in the computational basis, as shown in the figure below.



Denoting the probability of measuring the basis state 
âˆ£
i
âŸ©
âˆ£
j
âŸ©
âˆ£iâŸ©âˆ£jâŸ© by 
p
i
j
p 
ij
â€‹
  and the initial state of the qubit by 
âˆ£
Ïˆ
âŸ©
,
âˆ£ÏˆâŸ©, the circuit should be such that

p
00
=
âŸ¨
Ïˆ
âˆ£
E
0
âˆ£
Ïˆ
âŸ©
,
p
01
=
âŸ¨
Ïˆ
âˆ£
E
1
âˆ£
Ïˆ
âŸ©
,
p
10
+
p
11
=
âŸ¨
Ïˆ
âˆ£
E
2
âˆ£
Ïˆ
âŸ©
.
p 
00
â€‹
 
p 
01
â€‹
 
p 
10
â€‹
 +p 
11
â€‹
 
â€‹
  
=âŸ¨Ïˆâˆ£E 
0
â€‹
 âˆ£ÏˆâŸ©,
=âŸ¨Ïˆâˆ£E 
1
â€‹
 âˆ£ÏˆâŸ©,
=âŸ¨Ïˆâˆ£E 
2
â€‹
 âˆ£ÏˆâŸ©.
â€‹
 
Can you find the unitary that accomplishes this?

Challenge code
In the code template shown, you must complete the circuit implement_POVM, which applies the unitary that implements the alpha and beta-dependent POVM. In implement_POVM, wire 0 must be the auxiliary qubit and wire 1 must be the system qubit.

You are also given some space to code any helper functions you may need.

Input
As input to this problem, you are given:

alpha (float): Coefficient between 
0
0 and 
1
1 associated with the POVM element 
E
0
E 
0
â€‹
 
beta (float): Coefficient between 
0
0 and 
1
1 associated with the POVM element 
E
1
E 
1
â€‹
 
Output
Your circuit will be fed into a quantum device that measures the probabilities in the computational basis. This is done through the function povm_circuit, which is given for you in the challenge code. Then, it will be run with ten random quantum states in order to verify that the output probabilities match the POVM probabilities. If they all match, the output will be "Correct circuit". The relative error tolerance in the probabilities is 1e-4.

Test cases
The following public test cases are available to you. Note that there are additional hidden test cases that we use to verify that your code is valid in full generality.

test_input: 0.25, 0.25
expected_output: "Correct circuit"

test_input: 0.2, 0.4
expected_output: "Correct circuit"
Good luck!
