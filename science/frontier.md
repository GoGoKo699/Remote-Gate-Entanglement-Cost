# The accuracy–entanglement frontier

The finite converse and an explicit construction give a nearly matching cost for implementing a controlled phase gradient with one simultaneous exchange of classical messages. Let $`E_{\mathrm{sim}}(n,\epsilon)`$ be the infimum of the preshared resource's entanglement of formation over the finite protocols in [the model](model.md), with half diamond error at most $`\epsilon`$. The target is $`C_d`$, where $`d=2^n`$.

The principal quantitative statement is

```math
m-\log_2[16(m+1)]-3
\le E_{\mathrm{sim}}(n,\epsilon)
\le m+2,
\qquad
m=\min\left\{n,\frac12\log_2\frac1\epsilon\right\},
\tag{1}
```

for $`n\ge1`$ and $`0<\epsilon\le1/2`$. Nonnegativity may improve the displayed lower bound when $`m`$ is small. The additive gap in (1) is logarithmic in $`m`$; an additive-constant characterization is not established.

This note proves (1), records a uniform small-error consequence, and compares simultaneous messages with two sequential messages. [The converse](converse.md) contains the full lower-bound proof, [the protocols](protocols.md) give the constructions in detail, and [resource accounting](resource_accounting.md) separates preshared entanglement from local implementation costs. The exact endpoint and the interactive construction are inherited results; see [related work](../references/RELATED_WORK.md).

## 1. Explicit finite upper and lower bounds

For $`0<\epsilon\le1/2`$, define

```math
R_\epsilon=\left\lceil\frac{\pi}{2\sqrt\epsilon}\right\rceil.
```

### Theorem 1. Finite bounds

For every $`n\ge1`$,

```math
E_{\mathrm{sim}}(n,\epsilon)
\le\min\{n,\log_2R_\epsilon\}.
\tag{2}
```

For every $`r=2^k`$ with $`1\le k\le n`$ and $`\alpha_r=4r\sqrt\epsilon\le1/2`$,

```math
E_{\mathrm{sim}}(n,\epsilon)
\ge(1-\alpha_r)\log_2r-h_2(\alpha_r).
\tag{3}
```

One may maximize (3) over all eligible $`r`$ and include zero as an additional lower bound.

The lower inequality also holds at $`\epsilon=0`$; only the definition of $`R_\epsilon`$ requires positive error.

**Lower bound.** Equation (3) is Theorem 1 of [the converse](converse.md). The maximization is valid because a protocol for $`C_{2^n}`$ restricts locally to a protocol for every $`C_{2^k}`$ with the same resource and no larger diamond error.

**Upper bound from a tapered resource.** For an integer $`R\ge1`$, use

```math
|\eta_R\rangle
=\sum_{k=0}^{R-1}c_k|k,k\rangle,
\qquad
c_k=\sqrt{\frac2{R+1}}\sin\frac{(k+1)\pi}{R+1}.
\tag{4}
```

The local shift and Fourier-measurement protocol in [protocols](protocols.md) applies to any known binary-controlled unitary $`C(U)`$. Alice shifts her resource label by minus the control value and measures it as $`j\in\{-1,\ldots,R-1\}`$. One spare local level makes this shift a unitary permutation. Bob applies $`U^k`$ controlled by his label, then measures that label in the Fourier basis, with outcome $`q\in\{0,\ldots,R-1\}`$. After exchanging $`j,q`$ simultaneously, Bob applies $`U^{-j}`$ and Alice applies a phase correction to her control.

With $`c_k=0`$ outside the range in (4), the corrected Kraus operator for outcome $`(j,q)`$, up to a global phase, is

```math
K_{jq}
=\frac1{\sqrt R}
  \bigl(\mathrm{diag}(c_j,c_{j+1})\otimes I\bigr)C(U).
\tag{5}
```

Summing the branches preserves both diagonal control blocks and multiplies its off-diagonal blocks by

```math
f_R=\sum_{j=0}^{R-2}c_jc_{j+1}
=\cos\frac{\pi}{R+1}.
\tag{6}
```

For completeness, the last equality follows from the recurrence

```math
c_{j-1}+c_{j+1}
=2\cos\frac\pi{R+1}\,c_j,
\qquad c_{-1}=c_R=0,
```

by multiplying by $`c_j`$, summing, and using $`\sum_jc_j^2=1`$.

Thus the residual channel on the control is

```math
\mathcal D_{f_R}
=\frac{1+f_R}{2}\mathrm{id}
 +\frac{1-f_R}{2}\mathrm{Ad}_{Z_2}.
```

Since the identity and Pauli-$`Z`$ channels have full diamond distance two, the **half** diamond error of the construction is exactly

```math
\epsilon_R
=\frac{1-f_R}{2}
=\sin^2\frac{\pi}{2(R+1)}
\le\frac{\pi^2}{4(R+1)^2}.
\tag{7}
```

The upper bound two on that channel distance follows from the triangle inequality, and the input $`|+\rangle`$ attains it. Tensoring with Bob's system and composing with $`C(U)`$ do not change this value.

The pure resource in (4) has entanglement

```math
E_F(|\eta_R\rangle\langle\eta_R|)
=H(c_0^2,\ldots,c_{R-1}^2)\le\log_2R.
```

Choosing $`R=R_\epsilon`$ in (7) proves the logarithmic branch of (2).

**Exact cyclic upper bound.** For $`U=Z_d`$, use a maximally entangled state of Schmidt rank $`d`$ and replace the shift above by a cyclic shift modulo $`d`$. Because $`Z_d^d=I`$, the wraparound introduces no error. The corrected branch operators are global phases times $`C_d/d`$, so the channel is exactly $`\mathrm{Ad}_{C_d}`$ and the resource has $`n`$ ebits. This is a specialization of the finite-group protocols of [Yu, Griffiths, and Cohen](https://arxiv.org/abs/1109.5013) and [Yu](https://arxiv.org/abs/1112.0307). It proves the other branch of (2). ∎

Equation (2) is an upper bound on preshared entanglement of formation with ideal local operations. Controlled powers, state preparation, Fourier transforms, and their approximation errors must also be charged in an implementation. They are accounted for separately in [resource accounting](resource_accounting.md); no efficient implementation of an arbitrary black-box unitary's powers is assumed by (2).

## 2. Matching the leading scale

### Corollary 2. Leading frontier

For $`n\ge1`$ and $`0<\epsilon\le1/2`$, define

```math
L=\frac12\log_2\frac1\epsilon,
\qquad m=\min\{n,L\}.
```

Then (1) holds. In particular, along any sequence of parameters for which $`m\to\infty`$,

```math
\frac{E_{\mathrm{sim}}(n,\epsilon)}m\longrightarrow1.
\tag{8}
```

**Proof of the upper bound.** From the definition of $`R_\epsilon`$,

```math
R_\epsilon
\le\frac{\pi}{2\sqrt\epsilon}+1
=2^L\left(\frac\pi2+\sqrt\epsilon\right)
<4\,2^L.
```

Therefore (2) gives

```math
E_{\mathrm{sim}}(n,\epsilon)
\le\min\{n,L+2\}\le m+2.
```

**Proof of the lower bound.** Put

```math
k=\left\lfloor m-\log_2[16(m+1)]\right\rfloor.
```

If $`k<1`$, the claimed lower expression is negative, so nonnegativity of $`E_F`$ suffices. Otherwise choose $`r=2^k`$. This is an allowed restriction because $`k\le m\le n`$. Moreover,

```math
r\le\frac{2^m}{16(m+1)},
\qquad
\alpha_r=4r\sqrt\epsilon
\le\frac{2^{m-L}}{4(m+1)}
\le\frac1{4(m+1)}\le\frac12.
```

Equation (3), the bound $`h_2(\alpha_r)\le1`$, and $`\alpha_r k\le1/4`$ now imply

```math
E_{\mathrm{sim}}(n,\epsilon)
\ge k-\frac14-1
\ge m-\log_2[16(m+1)]-\frac94
\ge m-\log_2[16(m+1)]-3.
```

Dividing (1) by $`m`$ and taking $`m\to\infty`$ proves (8). ∎

The logarithmic additive term comes from choosing a cyclic restriction small enough that the error penalty in (3) remains bounded. It is a limitation of these bounds. Equation (8) should not be read as an additive-constant formula.

## 3. A uniform small-error statement

The leading statement concerns growing $`m`$. A uniform order-of-growth statement, including small registers, follows directly from the same finite converse.

### Corollary 3. Uniform constants

For every integer $`n\ge1`$ and every $`0<\epsilon\le2^{-16}`$,

```math
\frac1{16}\min\left\{n,\frac12\log_2\frac1\epsilon\right\}
\le E_{\mathrm{sim}}(n,\epsilon)
\le3\min\left\{n,\frac12\log_2\frac1\epsilon\right\}.
\tag{9}
```

The numerical constants and the cutoff are conservative choices.

**Proof.** Here $`L\ge8`$ and $`m\ge1`$. The upper bound in (1) is at most $`3m`$.

For the lower bound first use $`r=2`$, which is available for every $`n\ge1`$. Its error parameter obeys

```math
\alpha_2=8\sqrt\epsilon\le\frac1{32}.
```

Monotonicity of the lower expression on this interval and (3) give

```math
E_{\mathrm{sim}}(n,\epsilon)
\ge\frac{31}{32}-h_2\!\left(\frac1{32}\right)
>\frac34.
\tag{10}
```

One elementary verification of the last inequality is $`h_2(p)\le p\log_2(1/p)+p/\ln2`$, together with $`1/\ln2<3/2`$. If $`m\le12`$, (10) implies $`E_{\mathrm{sim}}\ge m/16`$.

If $`m\ge12`$, instead choose $`k=\lfloor m/2\rfloor`$ and $`r=2^k`$. Then

```math
\alpha_r
\le4\,2^{m/2-L}
\le4\,2^{-m/2}
\le\frac1{16}.
```

Using $`k\ge m/2-1`$ and $`h_2(\alpha_r)\le1`$ in (3) gives

```math
E_{\mathrm{sim}}(n,\epsilon)
\ge\frac{15}{16}\left(\frac m2-1\right)-1
=\frac{15m}{32}-\frac{31}{16}
\ge\frac m4
\ge\frac m{16},
```

where the penultimate inequality holds for $`m\ge12`$. This proves (9). ∎

Consequently $`E_{\mathrm{sim}}(n,\epsilon)=\Theta(\min\{n,\log_2(1/\epsilon)\})`$ uniformly on the explicit range of (9). No uniform assertion near $`\epsilon=1/2`$ is needed or made.

## 4. Exact implementation and the interactive comparison

### Proposition 4. Exact costs

For every $`n\ge1`$,

```math
E_{\mathrm{sim}}(n,0)=n.
\tag{11}
```

If two sequential directed classical messages are allowed instead, the exact minimum preshared entanglement of formation for $`C_d`$ is one ebit.

**Simultaneous messages.** Setting $`\epsilon=0`$ and $`r=d`$ in (3) gives the lower bound $`n`$. The exact cyclic protocol attains it. This is the known exact separation furnished by [Gonzales–Chitambar](https://arxiv.org/html/1810.00994v2) and the finite-group upper protocols, rather than an additional finite-error result.

**Two sequential messages: upper bound.** Share a Bell pair $`ab`$. Alice CNOTs the input control $`A`$ into $`a`$, measures $`a`$ in the computational basis, and sends the outcome to Bob. After his Pauli correction on $`b`$, an arbitrary pure input $`|0\rangle|\psi_0\rangle+|1\rangle|\psi_1\rangle`$ has become

```math
|0\rangle_A|0\rangle_b|\psi_0\rangle_B
+|1\rangle_A|1\rangle_b|\psi_1\rangle_B.
```

Bob applies controlled-$`Z_d`$ from $`b`$ to $`B`$, measures $`b`$ in the $`X`$ basis, and sends that outcome back. Alice's final Pauli-$`Z`$ correction removes the measurement sign, leaving $`C_d`$ applied to the input. The same calculation permits a reference inside $`|\psi_0\rangle,|\psi_1\rangle`$, so it proves equality of channels. This remote-control construction is standard; see [Eisert, Jacobs, Papadopoulos, and Plenio](https://arxiv.org/abs/quant-ph/0005101) and the discussion in [Gonzales–Chitambar](https://arxiv.org/html/1810.00994v2).

Bob's second message depends on his actions after receiving the first message. The construction therefore uses two sequential directed messages.

**Two sequential messages: lower bound.** Restrict Bob to the two-dimensional subspace spanned by $`|0\rangle`$ and $`|d/2\rangle`$. On that subspace $`Z_d`$ is Pauli $`Z`$, so $`C_d`$ is controlled-$`Z`$. Applying it to the product input $`|+\rangle_A|+\rangle_B`$ creates a maximally entangled two-qubit state. Entanglement of formation cannot increase under local operations and classical communication. Thus any exact implementation, even with additional interactive rounds, requires at least one ebit of preshared entanglement of formation. The Bell-pair protocol attains this bound. ∎

## 5. Consequences and limits

For each fixed $`n`$, the finite converse with $`r=d`$ tends to $`n`$ as $`\epsilon\to0`$, while the exact cyclic upper bound is always $`n`$. Hence

```math
\lim_{\epsilon\downarrow0}E_{\mathrm{sim}}(n,\epsilon)=n.
```

This conclusion allows the resource and workspace dimensions to vary with $`\epsilon`$; the converse does not impose a fixed architecture.

For each fixed nonzero $`\epsilon`$, (2) is bounded independently of $`n`$. Distinct eigenphases alone therefore do not impose an unbounded entanglement cost at that accuracy. When both the required accuracy and the register size increase so that $`m\to\infty`$, (8) shows an unbounded cost for simultaneous classical messages, whereas the two-message interactive construction continues to use one ebit exactly.

The proved result is specific to the phase-gradient family and to the stated resource model. It does not characterize arbitrary spectra, establish optimality of the sine resource among all protocols, or account for free quantum messages. Its upper and lower bounds concern a gate channel and preshared entanglement; local gate counts, state preparation, and precision budgets are separate parts of the [resource analysis](resource_accounting.md).
