# Question 5: The Hidden Subgroup Stage

**Points:** 200pts

## Question

Suppose binary training inputs $x\in\mathbb{F}_2^n$ have labels $f(x)$ and a candidate nonzero XOR symmetry $s$. Perfect symmetry means

$$f(x)=f(x\oplus s).$$

For each class label $r$, collect $X_r=\{x_i:f(x_i)=r\}$ and encode

$$|X_r\rangle=\frac{1}{\sqrt{|X_r|}}\sum_{x\in X_r}|x\rangle.$$

After applying $H^{\otimes n}$, complete pairs $\{x,x\oplus s\}$ have support only on strings satisfying $y\cdot s=0$. An ancilla can measure this parity by receiving a CNOT from every position where $s_j=1$. Let

$$p_r(s)=P(y\cdot s=0).$$

The overall compatibility score is the class-size-weighted mean

$$S(s)=\sum_r\frac{|X_r|}{N}p_r(s).$$

### Challenge task

Complete `symmetry_score(data, labels, s)` and return `S(s)` as a float. A circuit implementation is allowed, but the overlap also has an exact analytical reduction based on counting same-label XOR partners. Training inputs are distinct.

### Example

For classes `{000, 110}`, `{001, 111}`, and `{101}` with `s = 110`, the first two classes form complete pairs and score `1`; the singleton scores `1/2`. Hence $S(s)=2/5+2/5+1/10=0.9$.

### Input and output

`data` is an array of equal-length binary strings, `labels` contains their integer classes, and `s` is a binary candidate symmetry of matching width. Return the floating-point symmetry score.

### Public cases

| Data / labels / symmetry | Expected |
|---|---:|
| `[[000],[110],[001],[111],[101]]`, `[0,0,1,1,2]`, `110` | 0.9 |
| `[[000],[110],[001]]`, `[0,0,0]`, `110` | 0.833333333333333 |

The checker uses relative tolerance `1e-3`.
