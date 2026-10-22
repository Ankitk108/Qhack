# Question 7: Approximation Ratio for QAOA

**Points:** 400pts

## Question

The Minimum Vertex Cover problem asks for the smallest set of vertices touching every edge. For a graph with edge set $E$, use

$$H_{\mathrm{cost}}=\frac34\sum_{(i,j)\in E}(Z_iZ_j+Z_i+Z_j)-\sum_{i\in V}Z_i,$$

and mixer $H_{\mathrm{mixer}}=\sum_{i\in V}X_i$. Prepare $|+\rangle$ on every vertex and apply four alternating cost and mixer layers.

After optimizing the QAOA parameters, compare its minimum expected cost with the exact smallest eigenvalue:

$$r^*=\frac{\langle H_{\mathrm{cost}}\rangle_{\mathrm{QAOA}}}{\lambda_{\min}(H_{\mathrm{cost}})}.$$

### Challenge task

Implement `approximation_ratio(edges)`. Build both Hamiltonians, create and optimize the depth-four QAOA circuit, calculate the exact ground energy, and return one real PennyLane NumPy tensor containing the ratio.

### Input and output

`edges` is a list of integer vertex pairs. Vertices are consecutively labelled. Return the scalar approximation ratio.

### Public cases

- `[[0,1],[1,2],[0,2],[2,3]]` expects `0.58160924`.
- `[[0,1],[1,2],[2,3],[3,0]]` expects `0.94746734`.

The original checker uses relative tolerance `5e-2`, but it is tied to a particular finite optimization trajectory; this limitation is discussed alongside the solution.
