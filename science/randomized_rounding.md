# An alternative upper bound from randomized spectral rounding

[Model](model.md) · [Cyclic and tapered protocols](protocols.md) · [Resource accounting](resource_accounting.md) · [Related work](../references/RELATED_WORK.md)

The tapered protocol has a particularly simple exact error channel. The leading one-half logarithmic precision cost can also be obtained by combining unbiased spectral rounding with the inherited cyclic-group protocol. This alternative is useful for attribution: the upper coefficient alone should not be interpreted as the central new result. The general lower bound is in the [converse](converse.md).

## Unbiased rounding of a known spectrum

Let $`V=\sum_j e^{i\theta_j}|v_j\rangle\langle v_j|`$ be known. Choose an integer $`D\ge2`$ and let $`h=2\pi/D`$. Write $`\theta_j/h=a_j+b_j`$, with integer $`a_j`$ and $`0\le b_j<1`$. For one shared random threshold $`t\in[0,1)`$, define

```math
\widetilde\theta_j(t)=h\bigl(a_j+\mathbf{1}_{t\lt b_j}\bigr),
\quad
\Delta_j(t)=\widetilde\theta_j(t)-\theta_j.
```

The errors obey $`|\Delta_j(t)|\le h`$ and $`\mathbb E_t\Delta_j(t)=0`$ for every eigenvalue. A phase that crosses $`2\pi`$ is represented by its unwrapped value in this equation; its unitary action is still periodic.

Put $`\widetilde V_t=\sum_j e^{i\widetilde\theta_j(t)}|v_j\rangle\langle v_j|`$. Each rounded unitary satisfies $`\widetilde V_t^D=I`$, so the known cyclic protocol implements $`C(\widetilde V_t)`$ exactly with a maximally entangled rank-$`D`$ resource and one simultaneous classical exchange. The parties use the same threshold, chosen offline and independent of the quantum input.

Only finitely many rounded gates occur: the threshold intervals are cut by the finitely many values $`b_j`$. Thus the ideal construction can be written with a finite classical alphabet and prescribed probabilities. It does not require an infinite-dimensional classical register. For an arbitrary known spectrum, obtaining and implementing this description may be expensive; no efficient diagonalization claim is made.

## Why the averaged error is quadratic

Define the Hermitian phase-error operator on the joint input,

```math
H_t=|1\rangle\langle1|\otimes
\sum_j\Delta_j(t)|v_j\rangle\langle v_j|.
```

Then $`\|H_t\|_\infty\le h`$, $`\mathbb E_tH_t=0`$, and
$`C(\widetilde V_t)=C(V)e^{iH_t}`$. Let $`\mathcal L_t(X)=i[H_t,X]`$. Its diamond norm is at most $`2h`$. The integral remainder for the channel exponential is

```math
e^{\mathcal L_t}-I-\mathcal L_t
=\int_0^1(1-s)e^{s\mathcal L_t}\mathcal L_t^2\,ds.
```

Conjugation by $`e^{isH_t}`$ is a channel of diamond norm one. Therefore

```math
\|e^{\mathcal L_t}-I-\mathcal L_t\|_\diamond
\le\frac12(2h)^2=2h^2.
```

Averaging cancels the linear term exactly. If $`\overline\Lambda`$ is the channel obtained after forgetting the threshold record, unitary invariance and convexity give

```math
\frac12\|\overline\Lambda-\mathrm{Ad}_{C(V)}\|_\diamond
\le h^2=\frac{4\pi^2}{D^2}.
```

This bound is independent of Bob's dimension. It concerns the averaged channel: the error of an individual rounded unitary need only be of order $`1/D`$. The resource model explicitly allows shared randomness, so averaging is an admissible protocol. The record is not supplied as an additional output demanded by the ideal target.

Choosing $`D=O(1/\sqrt\epsilon)`$ gives an entanglement upper bound $`\tfrac12\log_2(1/\epsilon)+O(1)`$. Constants here are looser than the tapered construction. Neither this comparison nor the path-eigenvector optimization asserts that a particular resource state is optimal among all admissible protocols.

## Explicit finite randomness for the phase-gradient family

For $`d=2^n`$, choose $`D=2^q`$ with $`q\le n`$ and set $`M=2^{n-q}`$. Express Bob's label as $`j=aM+b`$, where $`0\le b<M`$. A shared uniform integer $`t\in\{0,\ldots,M-1\}`$ gives

```math
\widetilde Z_{d,t}|aM+b\rangle
=\exp\!\left[\frac{2\pi i}{D}
\bigl(a+\mathbf{1}_{t\lt b}\bigr)\right]|aM+b\rangle.
```

The probability of rounding upward is exactly $`b/M`$, so the same cancellation holds without real-valued random data. The threshold requires $`n-q`$ shared random bits, obtained offline. For $`q=n`$, there is no rounding and the exact $`n`$-ebit protocol is recovered.

This rounded gate also has an explicit local implementation. A reversible comparison computes $`c=\mathbf{1}_{t\lt b}`$ from the low bits into a local flag, using $`O(n-q)`$ Toffoli gates and work bits with a straightforward reversible comparator. The phase on $`a`$ is a product of known single-qubit phase rotations; the flag adds one more known phase. For a quantum power index $`k`$ of $`q`$ bits, the phase is

```math
\exp\!\left(\frac{2\pi i k a}{D}\right)
\exp\!\left(\frac{2\pi i k c}{D}\right).
```

Bit expansion implements these factors with $`O(q^2)`$ controlled phase rotations, followed by uncomputation of the comparison flag. Classical outcome-dependent corrections use the same comparison and at most $`O(q)`$ phase rotations. The cyclic register shift and Fourier transform cost polynomially many additional local gates. This supplies a concrete polynomial implementation in $`n`$ and the number of accuracy bits, without spectral data loading or QRAM. Individual rotation synthesis errors must still be budgeted as described in [resource accounting](resource_accounting.md).

## Relation to the main construction

The randomized cyclic construction uses a maximally entangled resource and a random mixture of rounded gates. The tapered construction uses a nonuniform resource and gives the desired controlled gate followed exactly by dephasing of Alice's control. Both explain why a squared error law is attainable. The [finite converse](converse.md) applies to both, as well as every other admissible protocol, and is what establishes the matching leading entanglement requirement.
