Break the Tie
Complete
200pts
Instructions
Submissions
Resources
You have a discrete random variable 
X
X for which outcome 
i
i occurs with probability 
p
i
p 
i
â€‹
 , and a non-negative quantity 
f
(
X
)
f(X) defined on its outcomes. You want its average/expectation value,

E
[
f
(
X
)
]
=
âˆ‘
i
p
i
â€‰
f
i
.
E[f(X)]= 
i
âˆ‘
â€‹
 p 
i
â€‹
 f 
i
â€‹
 .
Classically, we can estimate this by sampling: draw 
N
N outcomes, evaluate 
f
f on each, and average. Amplitude estimation performs the same task with an error that falls quadratically faster in the number of times the circuit is applied. That quadratic improvement is one of the attractive characteristics of quantum Monte Carlo. Part of the price for it is that the answer comes back ambiguous, and this challenge is about that ambiguity.

Putting an average into an amplitude
In quantum Monte Carlo, there are two important steps. First, a unitary 
A
A loads the distribution onto 
m
m data wires so that the squared amplitudes reproduce the probabilities:

A
âˆ£
0
âŸ©
âŠ—
m
=
âˆ‘
i
p
i
â€‰
âˆ£
i
âŸ©
.
Aâˆ£0âŸ© 
âŠ—m
 = 
i
âˆ‘
â€‹
  
p 
i
â€‹
 
â€‹
 âˆ£iâŸ©.
Second, we add one objective wire, and a unitary 
R
R rotates it controlled on the data wires, so that the outcome 
âˆ£
i
âŸ©
âˆ£iâŸ© puts amplitude 
f
~
i
f
~
â€‹
  
i
â€‹
 
â€‹
  on 
âˆ£
1
âŸ©
âˆ£1âŸ©:

âˆ‘
i
p
i
â€‰
âˆ£
i
âŸ©
(
1
âˆ’
f
~
i
â€‰
âˆ£
0
âŸ©
+
f
~
i
â€‰
âˆ£
1
âŸ©
)
.
i
âˆ‘
â€‹
  
p 
i
â€‹
 
â€‹
 âˆ£iâŸ©( 
1âˆ’ 
f
~
â€‹
  
i
â€‹
 
â€‹
 âˆ£0âŸ©+ 
f
~
â€‹
  
i
â€‹
 
â€‹
 âˆ£1âŸ©).
Amplitudes cannot exceed a value of 
1
1, so 
f
f has to be rescaled into the 
[
0
,
1
]
[0,1] interval first. Dividing by 
f
max
â¡
=
max
â¡
i
f
i
f 
max
â€‹
 =max 
i
â€‹
 f 
i
â€‹
  achieves this, giving 
f
~
i
=
f
i
/
f
max
â¡
f
~
â€‹
  
i
â€‹
 =f 
i
â€‹
 /f 
max
â€‹
 .

If we then read the objective wire, we get

Pr
â¡
[
1
]
â€…â€Š
=
â€…â€Š
âˆ‘
i
p
i
f
~
i
â€…â€Š
=
â€…â€Š
E
[
f
(
X
)
]
f
max
â¡
â€…â€Š
â‰¡
â€…â€Š
a
.
Pr[1]= 
i
âˆ‘
â€‹
 p 
i
â€‹
  
f
~
â€‹
  
i
â€‹
 = 
f 
max
â€‹
 
E[f(X)]
â€‹
 â‰¡a.
The desired average is now encoded in a single probability amplitude, and multiplication by 
f
max
â¡
f 
max
â€‹
  at the end recovers it.

Why two answers come back
Amplitude estimation runs phase estimation on a Grover-like operator 
Q
Q built from that state. 
Q
Q acts as a rotation inside a two-dimensional invariant subspace, and a rotation has a conjugate pair of eigenvalues 
e
Â±
2
Ï€
i
Î¸
e 
Â±2Ï€iÎ¸
 . The circuit above prepares an equal superposition of the two corresponding eigenvectors. These have equal overlap, and therefore equal peak height.

With 
n
n estimation wires the register reports a phase 
Î¸
=
k
/
2
n
Î¸=k/2 
n
  for an integer bin 
k
k, from which

a
=
1
âˆ’
cos
â¡
(
Ï€
Î¸
)
2
.
a= 
2
1âˆ’cos(Ï€Î¸)
â€‹
 .
Because both eigenvectors are present in equal measure, the register shows two peaks of exactly equal height: one at bin 
k
k, one at bin 
2
n
âˆ’
k
2 
n
 âˆ’k. The mirror bin corresponds to the phase 
1
âˆ’
Î¸
1âˆ’Î¸, and 
cos
â¡
(
Ï€
(
1
âˆ’
Î¸
)
)
=
âˆ’
cos
â¡
(
Ï€
Î¸
)
cos(Ï€(1âˆ’Î¸))=âˆ’cos(Ï€Î¸), so the two bins map to

1
âˆ’
cos
â¡
(
Ï€
Î¸
)
2
and
1
+
cos
â¡
(
Ï€
Î¸
)
2
,
2
1âˆ’cos(Ï€Î¸)
â€‹
 and 
2
1+cos(Ï€Î¸)
â€‹
 ,
which are 
a
a and 
1
âˆ’
a
1âˆ’a. Both are perfectly consistent with everything the algorithm measured. No amount of extra estimation wires will separate them, because sharpening the peaks sharpens both, so the ambiguity is structural to the algorithm rather than a matter of resolution.

It is worth having the relation in the forward direction as well, so that you can predict your own readout before running anything:

Î¸
=
arccos
â¡
(
1
âˆ’
2
a
)
Ï€
,
k
=
r
o
u
n
d
â€‰â£
(
2
n
Î¸
)
.
Î¸= 
Ï€
arccos(1âˆ’2a)
â€‹
 ,k=round(2 
n
 Î¸).
A warning about the template's documentation
The worked example in the qp.QuantumMonteCarlo docstring resolves the ambiguity silently, with

phase_estimated = np.argmax(circuit()[:int(N / 2)]) / N
The slice searches only the lower half of the estimation register, which amounts to always taking the smaller of the two candidates. That is right for the example it appears in but wrong in general. Note that following this procedure will fail on three of this challenge's test cases (one of which is public)

The same docstring also gives the relation twice: as 
Î¼
=
(
1
+
cos
â¡
(
Ï€
Î¸
)
)
/
2
Î¼=(1+cos(Ï€Î¸))/2 in its algorithm summary, and as 
Î¼
=
(
1
âˆ’
cos
â¡
(
Ï€
Î¸
)
)
/
2
Î¼=(1âˆ’cos(Ï€Î¸))/2 in its example. Those are not a typo. They are the two candidates, and which one applies depends on information the estimation register does not contain. Supplying that information is the work this challenge is asking for.

Breaking the tie
Resolving the ambiguity requires information from outside the estimation. Any independent estimate of 
a
a will do, provided it is accurate to better than half the distance between the two candidates. The candidates are 
a
a and 
1
âˆ’
a
1âˆ’a, so that distance is 
âˆ£
1
âˆ’
2
a
âˆ£
âˆ£1âˆ’2aâˆ£ and the requirement is an error below 
âˆ£
0.5
âˆ’
a
âˆ£
âˆ£0.5âˆ’aâˆ£. The estimate does not need to be precise, only unambiguous. In this challenge's test cases the two candidates are between 
0.13
0.13 and 
0.81
0.81 apart.

As 
a
a approaches 
0.5
0.5 the two candidates merge. That edge case is also why the mirror bin is taken modulo 
2
n
2 
n
 : at 
a
=
0
a=0 the peak sits at 
k
=
0
k=0, which is its own mirror.

There is a method that allows you to readily perform this estimate: build the encoding directly on 
m
+
1
m+1 wires and measure the objective wire. That gives 
a
a outright, with no estimation register at all.

If that seems like cheating (if you can measure 
a
a directly, why estimate it?), note what is actually being traded. Both circuits contain the same encoding, one controlled rotation per outcome, 
2
m
2 
m
  of them. The direct circuit applies it once and reads 
Pr
â¡
[
1
]
Pr[1], which is ordinary sampling and so costs 
1
/
Îµ
2
1/Îµ 
2
  shots to reach accuracy 
Îµ
Îµ. Amplitude estimation applies that same encoding inside 
Q
Q roughly 
2
n
2 
n
  times, in one deep circuit, and reaches 
1
/
Îµ
1/Îµ. Shots are traded for depth, not gates. The direct circuit is the cheap, shallow, coarse instrument you use to point the sharp one in the right direction, and the number you report at the end is the estimated one.

One thing this challenge deliberately does not exercise: the tests run on an exact simulator with no shots, so there is no sampling noise anywhere in it. The gap between your estimate and the true average comes purely from discretisation, because 
2
n
Î¸
2 
n
 Î¸ has to be rounded to an integer bin. That is why the tolerance can be as tight as 
10
âˆ’
9
10 
âˆ’9
 , and why reporting 
âˆ‘
i
p
i
f
i
âˆ‘ 
i
â€‹
 p 
i
â€‹
 f 
i
â€‹
  instead of the estimate would fail.

Symbols
The names below follow the qp.QuantumMonteCarlo documentation, so that the challenge and the docs can be read side by side.

m
m -- data wires; the distribution has 
2
m
2 
m
  entries.
objective wire -- one further wire, the last of target_wires, carrying 
f
~
i
f
~
â€‹
  
i
â€‹
 
â€‹
 .
target_wires -- the 
m
m data wires and the objective wire together, 
m
+
1
m+1 in all. This is the single easiest argument to get wrong.
n
n -- estimation wires, which hold the phase readout.
N
N -- applications of 
Q
Q, or classical samples: the currency in which the two methods are compared.
Îµ
Îµ -- absolute error on 
E
[
f
(
X
)
]
E[f(X)]. The matching error on 
a
a is 
Î´
=
Îµ
/
f
max
â¡
Î´=Îµ/f 
max
â€‹
 .
a
a -- the amplitude, equal to 
E
[
f
(
X
)
]
/
f
max
â¡
E[f(X)]/f 
max
â€‹
 .
A
A, 
R
R, 
Q
Q -- load the distribution, rotate the objective wire, and the Grover-like operator built from the two.
Two differences from the docstring are worth noting here:

It calls the estimated quantity 
Î¼
Î¼, which is exactly this challenge's 
a
a.
Its 
f
f is already rescaled into 
[
0
,
1
]
[0,1], so it is this challenge's 
f
~
i
f
~
â€‹
  
i
â€‹
  and not the raw values. 
f
max
â¡
f 
max
â€‹
  has to be divided out before the function is handed to the template.
Challenge code
Write

estimate_mean(probabilities, values, n)
Your solution builds and runs two circuits, which you define first and then run using the run_circuit(num_wires, circuit) helper function:

The amplitude-estimation circuit, on 
m
+
1
+
n
m+1+n wires. Call qp.QuantumMonteCarlo with target_wires=range(m + 1) (the 
m
m data wires plus the objective wire) and the 
n
n estimation wires after them, and measure the estimation register. This is the circuit that produces the two-peak readout, so it is where the two candidates come from. It cannot say which of them is correct.

The tie-breaker circuit, on 
m
+
1
m+1 wires. Build the same encoding by hand: qp.StatePrep for the distribution on the data wires, then one multi-controlled qp.RY per outcome, and measure the objective wire. This gives 
a
a outright, with no estimation register involved. That number is what tells you which candidate to keep, but it is not the number you report.

The Challenge Template gives you two helpers and you have to write the two circuit bodies described above. rotation_angle(fraction) is the angle that puts amplitude 
fraction
fraction
â€‹
  on 
âˆ£
1
âŸ©
âˆ£1âŸ©. run_circuit(num_wires, circuit) builds an analytic simulator of num_wires wires, turns your circuit function into a QNode, runs it, and hands back the measurement as a list of floats.

Inputs
Your function is called with three arguments:

probabilities -- a list of float, the probability of each outcome. They sum to 
1
1, and the length is a power of two: length 8 means 
m
=
3
m=3 data wires.
values -- a list of float, all non-negative, the value of the quantity at each outcome. Same length as probabilities.
n -- an int, the number of estimation wires.
Note that 
m
m is not passed in. You derive it from the length of probabilities, with m = int(round(np.log2(len(probabilities)))).

A concrete call, which is the second public test case:

estimate_mean([0.125] * 8,
              [0.6, 0.7, 0.8, 0.9, 1.0, 1.0, 1.0, 1.0],
              8)
Here len(probabilities) == 8, so 
m
=
3
m=3. Your circuits therefore need 
m
=
3
m=3 data wires, 
1
1 objective wire and 
n
=
8
n=8 estimation wires. 12 wires for the estimation, and 4 for the direct encoding.

Outputs
Return a single float: the estimated average of the quantity. It is 
f
max
â¡
f 
max
â€‹
  times whichever of the two candidate amplitudes your direct encoding identifies as the right one.

For the call above, the correct return is

0.8745681972617296
Because this is the estimate, it will not agree exactly with 
âˆ‘
i
p
i
f
i
âˆ‘ 
i
â€‹
 p 
i
â€‹
 f 
i
â€‹
 , which is 
0.875
0.875 here. The graded value is checked to an absolute tolerance of 
10
âˆ’
9
10 
âˆ’9
 , so returning the exact average instead of the estimate fails.

Rules
Within the two circuits the layout is free. The order of the data wires does not matter, the objective wire may sit before them rather than after, and any loading route works as long as the squared amplitudes are the probabilities, so qp.MottonenStatePreparation is accepted in place of qp.StatePrep.

Checking your pipeline by hand
Every stage of the second public test case can be checked with a calculator, before any circuit runs. The distribution is uniform on 8 outcomes and the quantity sits close to its maximum of 
1
1, so 
a
=
E
[
f
(
X
)
]
a=E[f(X)] exactly:

f_max                                  1.0
a = E[f] / f_max                       0.875
theta = arccos(1 - 2a) / pi            0.769947
2**n * theta,  n = 8                 197.106
tallest bin k = round(2**n * theta)  197
mirror bin 2**n - k                   59
the two candidates                     0.125432  and  0.874568
reported mean, f_max * the right one   0.874568
exact sum(p_i f_i), for comparison     0.875
The register can only report the integer 
197
197, not 
197.106
197.106. That rounding is the entire difference between 
0.874568
0.874568 and 
0.875
0.875: the estimate is not noisy, it is quantised. Both of those peaks are 
0.4817
0.4817 tall, and between them they hold 
96
%
96% of the probability in the register.

Public test cases
input: [[0.4008104395612045, 0.24310382032676792, 0.14744992052145606, 0.0894328975684541, 0.054243794362206846, 0.03290052437982574, 0.019955176756987287, 0.012103426523097706], [0.0, 0.25, 1.0, 2.25, 4.0, 6.25, 9.0, 12.25], 8] expected output: 1.160949660702857

input: [[0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125], [0.6, 0.7, 0.8, 0.9, 1.0, 1.0, 1.0, 1.0], 8] expected output: 0.8745681972617296

The first case is a decaying distribution and a squared quantity, and the answer is the smaller candidate. The second is the one traced above, where the answer is the larger. There is no way to tell which from the readout alone. Note that the recipe in the template's own documentation would return 
0.125432
0.125432 for the second case.
