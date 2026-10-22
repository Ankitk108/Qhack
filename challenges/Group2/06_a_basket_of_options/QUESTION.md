# Question 6: A Basket of Options

**Points:** 400pts

## Question

Two asset prices follow correlated geometric Brownian motions,

$$S_{i,T}=S_{i,0}\exp\!\left[\left(r-\frac{\sigma_i^2}{2}\right)T+\sigma_i\sqrt{T}Z_i\right],$$

where $(Z_1,Z_2)$ is bivariate normal with correlation $\rho$. A basket with weight $w$ has value $B_T=wS_{1,T}+(1-w)S_{2,T}$ and European-call payoff $g=\max(B_T-K,0)$. Its fair value is

$$V_0=e^{-rT}\,\mathbb{E}[g].$$

Use fixed values $S_{1,0}=S_{2,0}=100$, $\sigma_1=0.20$, $\sigma_2=0.30$, and $r=0.05$. Discretize each normal variable at eight equally spaced points on `[-3,3]`, creating 64 scenarios. Evaluate and normalize the correlated density, compute each payoff, and normalize payoffs by $g_{\max}$ so $f(i)=g_i/g_{\max}\in[0,1]$.

### Challenge task

Complete `quantum_montecarlo` using PennyLane's quantum Monte Carlo template. Use six scenario wires, one payoff wire, and ten estimation wires placed last. The circuit estimates $\mu\approx\mathbb{E}[f]$; the grader recovers $V_0=e^{-rT}g_{\max}\mu$.

### Input and output

The executable template uses `(rho, w, T, K)` despite inconsistent prose ordering in the original statement. The QNode returns phase-estimation probabilities; the grader converts them to the option value.

### Public cases

- `(0.3,1.0,1.0,100)` gives `10.556134590137553`.
- `(0.4,0.5,1.0,110)` gives `6.487093067342844`.

The option value uses absolute tolerance `1e-3`.
