# From Watrous to the remote-gate entanglement bound

[Repository overview](../README.md) · [Milestone map](MILESTONES.md) · [Model](../science/model.md) · [Converse](../science/converse.md) · [Protocols](../science/protocols.md)

The educational anchor is John Watrous, *The Theory of Quantum Information* (Cambridge University Press, April 2018). The [official author page](https://cs.uwaterloo.ca/~watrous/TQI/) supplies an [author manuscript](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf) and errata. The section and equation numbers below refer to that manuscript. This repository links to the book; it does not redistribute it.

The project asks how much preshared entanglement is needed to implement a known controlled phase gradient when Alice and Bob can exchange classical messages only once, simultaneously. Watrous supplies the language of states, channels, norms, and entanglement. The additional steps are a communication-model argument, a fixed-environment continuity theorem, and a conditional entropy estimate that remains useful with arbitrarily large local memories.

This page develops those connections and a complete finite example. The [milestone map](MILESTONES.md) gives the more granular M01–M30 dependency structure. The proofs of the general bounds remain in the science notes.

<a id="conventions"></a>

## Conventions and notation

| Watrous notation or concept | Repository notation | Meaning in this project |
|---|---|---|
| A vector $`u`$ and adjoint $`u^*`$ | $`\lvert u\rangle`$, $`\langle u\rvert`$ | The same finite-dimensional vector and its adjoint. |
| $`uv^*`$, $`E_{a,b}`$ | $`\lvert u\rangle\langle v\rvert`$, $`\lvert a\rangle\langle b\rvert`$ | Rank-one operators and computational-basis matrix units. |
| $`\mathrm D(\mathcal X)`$ | Density operators $`\rho_X`$ | Positive operators of trace one; subscripts specify registers. |
| $`\mathrm C(\mathcal X,\mathcal Y)`$ | CPTP maps $`\Lambda:X\to Y`$ | Completely positive, trace-preserving maps, including discarding and measurements with retained records. |
| Operator norm and trace norm | $`\lVert T\rVert_\infty`$, $`\lVert T\rVert_1`$ | The largest singular value and the sum of singular values. |
| Completely bounded trace norm, written with triple bars and subscript one | $`\lVert\Phi\rVert_\diamond`$ | The same channel norm; an untouched quantum reference is included. |
| Full norms in displayed inequalities | $`\epsilon=\tfrac12\lVert\Lambda-\mathcal C_d\rVert_\diamond`$ | The repository's channel error is **half** the full diamond distance. State trace distance is likewise $`\tfrac12\lVert\rho-\sigma\rVert_1`$. |
| Quantum entropy $`H(\rho)`$ | $`S(\rho)=-\mathrm{Tr}(\rho\log_2\rho)`$ | Entropy in bits; $`H(p)`$ denotes classical Shannon entropy here. |
| $`E_F(X:Y)`$ | $`E_F(\rho_{A'B'})`$ | Entanglement of formation across the two resource holders. |
| Entanglement cost in a many-copy setting | $`E_{\mathrm{sim}}(n,\epsilon)`$ | The project instead minimizes $`E_F`$ over resources for one admissible implementation. |

The target dimension is $`d=2^n`$, and $`\mathcal C_d=\mathrm{Ad}_{C_d}`$ denotes its controlled phase-gradient channel. A restricted target has dimension $`r=2^k\le d`$; the tapered resource has Schmidt rank $`R`$. These are different parameters. The letters $`A,B`$ denote computational inputs and outputs, $`A',B'`$ denote resource shares, and $`K_A,K_B`$ denote retained local workspaces. In the converse, $`F`$ is a dilation of the entire implemented channel, $`C`$ is its mathematical record register, and $`\lambda`$ labels a pure-state ensemble used in the proof.

<a id="reading-route"></a>

## Focused reading route

The entries below identify the background used at each stage. They are source locators, not additional assumptions or a substitute for the linked project arguments.

| Watrous manuscript location | Connection to the project | Milestones |
|---|---|---|
| §§1.1.1–1.1.3; 2.1.1–2.1.3 | Tensor factors, reduced states, pure-state spectra, and purification registers. | [M01](MILESTONES.md#m01)–[M03](MILESTONES.md#m03) |
| §6.4, Exercise 6.3, equation (6.437) | Exact locator of the convex-roof definition of $`E_F`$; cited here as a definition. §6.2.2 gives the distinct asymptotic-cost context. | [M04](MILESTONES.md#m04) |
| §§2.2.1–2.2.2; §2.3.2, equations (2.258)–(2.262) | CPTP descriptions, isometric dilations, instruments, and classical records. | [M05](MILESTONES.md#m05)–[M07](MILESTONES.md#m07) |
| §§3.3.1–3.3.3; Definition 3.43 | Worst-case channel comparison with an untouched reference. The fixed-environment estimate is supplied separately below. | [M08](MILESTONES.md#m08)–[M09](MILESTONES.md#m09) |
| §§2.2.2, 6.1.2 | Locality and the distinction between an allowed LOCC operation and the narrower simultaneous-exchange schedule. | [M10](MILESTONES.md#m10), [M13](MILESTONES.md#m13) |
| §§1.1.1–1.1.3; 4.1.1 | Finite Fourier sums and averaging unitary conjugations. The phase-gradient twirl is derived in the converse. | [M11](MILESTONES.md#m11), [M14](MILESTONES.md#m14), [M23](MILESTONES.md#m23) |
| §§5.1.1–5.1.2, 5.2.1–5.2.3 | Entropy, concavity, classical flags, and continuity. The workspace-independent replacement is derived below. | [M12](MILESTONES.md#m12), [M24](MILESTONES.md#m24)–[M26](MILESTONES.md#m26) |
| §§6.2.1–6.2.2, 6.3.1 | Entanglement transformations, resource costs, and teleportation; linked here to the concrete distributed constructions. | [M15](MILESTONES.md#m15)–[M20](MILESTONES.md#m20), [M28](MILESTONES.md#m28) |

The remaining bridge is project specific: an arbitrary mixed-resource protocol in [M21](MILESTONES.md#m21)–[M22](MILESTONES.md#m22), the finite and leading-order bounds in [M27](MILESTONES.md#m27), and model comparison and synthesis in [M29](MILESTONES.md#m29)–[M30](MILESTONES.md#m30).

<a id="worked-example"></a>

## Worked example: a rank-two resource for controlled $`Z_4`$

Let Alice hold a qubit and Bob hold a four-dimensional target. Define

```math
Z_4=\mathrm{diag}(1,i,-1,-i),
\qquad
C_4=|0\rangle\langle0|\otimes I_4
    +|1\rangle\langle1|\otimes Z_4.
```

This example specializes the [noncyclic protocol](../science/protocols.md). Its role is to connect resource entropy, Kraus branches, and diamond error in one calculation. It establishes an achievable point, not optimality among all simultaneous-exchange protocols.

### Resource and message timing

For $`R=2`$, the sine coefficients are

```math
c_k=\sqrt{\frac2{R+1}}\sin\frac{(k+1)\pi}{R+1},
\qquad
(c_0,c_1)=\left(\frac1{\sqrt2},\frac1{\sqrt2}\right).
```

The shared state is one Bell pair,

```math
|\eta_2\rangle_{ab}=\frac{|0,0\rangle+|1,1\rangle}{\sqrt2}.
```

Each reduced state is $`I_2/2`$, so its entropy, and hence this pure resource's entanglement, is exactly one ebit. The equal coefficients are the $`R=2`$ instance of the sine profile; larger ranks need not be maximally entangled.

Before receiving any message, Alice subtracts her control value from her resource label:

```math
|x\rangle_A|k\rangle_a\longmapsto
|x\rangle_A|k-x\rangle_a,
\qquad x,k\in\{0,1\}.
```

Her possible labels are $`-1,0,1`$. A spare local level makes this map part of a unitary permutation; it is not subtraction modulo two. She measures the label and records $`j`$.

Independently, Bob applies $`Z_4^k`$ controlled by his resource qubit, then measures that qubit in the basis

```math
|f_q\rangle=\frac{|0\rangle+(-1)^q|1\rangle}{\sqrt2},
\qquad q\in\{0,1\}.
```

They exchange $`j,q`$ simultaneously. Afterward, Bob applies $`Z_4^{-j}`$ and Alice applies $`Z_2^q`$, where $`Z_2=\mathrm{diag}(1,-1)`$. In particular, $`j=-1`$ calls for the ordinary operation $`Z_4`$. All six outcome pairs are retained.

### The six branches

Put $`c_k=0`$ outside $`k=0,1`$. For each $`q`$, the corrected branch is

```math
K_{j,q}=\frac{(-1)^{qj}}{\sqrt2}
\left[\mathrm{diag}(c_j,c_{j+1})\otimes I_4\right]C_4.
```

The factor $`(-1)^{qj}`$ is an overall phase of that branch and drops out of its channel contribution. Let $`P_x=|x\rangle\langle x|\otimes I_4`$.

| Alice's outcome $`j`$ | Corrected operator for each $`q`$, up to that phase | Sum of $`K_{j,q}^\dagger K_{j,q}`$ over the two $`q`$ values |
|---|---|---|
| $`-1`$ | $`\tfrac12P_1C_4`$ | $`\tfrac12P_1`$ |
| $`0`$ | $`\tfrac12C_4`$ | $`\tfrac12I_{AB}`$ |
| $`1`$ | $`\tfrac12P_0C_4`$ | $`\tfrac12P_0`$ |

The final column sums to $`I_{AB}`$, which verifies trace preservation. Dropping the endpoint branches would change this to a postselected process and would not implement the claimed unconditional channel.

For $`\sigma=C_4\rho C_4^\dagger`$, summing every branch gives

```math
\Lambda(\rho)
=\frac12\sigma
 +\frac12(P_0\sigma P_0+P_1\sigma P_1)
=\frac34\sigma
 +\frac14(Z_2\otimes I_4)\sigma(Z_2\otimes I_4).
```

Equivalently, the two diagonal blocks of the control are unchanged, while each off-diagonal block is multiplied by

```math
f=c_0c_1=\frac12
=\cos\frac{\pi}{3}.
```

The boundary information therefore appears as control dephasing. It does not require a measurement of Bob's unknown target.

### Exact half diamond error

Unitary composition preserves the diamond norm, so the comparison with $`C_4`$ reduces to comparing control dephasing with the identity. The channel difference is one quarter of $`\mathrm{Ad}_{Z_2}-\mathrm{Id}`$. Its full diamond norm is at most $`2/4`$, because two channels have full diamond distance at most two. The input $`|+\rangle_A|0\rangle_B`$ attains the bound: $`C_4`$ acts trivially on this input, whereas the realized output is

```math
\left(\frac34|+\rangle\langle+|
      +\frac14|-\rangle\langle-|\right)_A
\otimes|0\rangle\langle0|_B.
```

Its trace distance from the ideal output is $`1/4`$. Therefore

```math
\frac12\|\Lambda-\mathrm{Ad}_{C_4}\|_\diamond
=\frac{1-f}{2}=\frac14,
\qquad E_F(|\eta_2\rangle\langle\eta_2|)=1.
```

The upper bound already includes arbitrary external references, while the displayed product input witnesses equality. The finite converse's small-error condition is not satisfied at this example's error, so it does not certify that one ebit is necessary here. For comparison, the inherited exact cyclic construction uses two ebits for $`C_4`$, whereas the exact interactive construction uses one ebit and two ordered messages. Their different schedules are described in [protocols](../science/protocols.md).

<a id="hidden-ensemble"></a>

## A mixed resource and its formal ensemble flag

An arbitrary resource can be represented as

```math
\rho_{A'B'}=\sum_\lambda p_\lambda
|\eta_\lambda\rangle\langle\eta_\lambda|,
\qquad
E_F(\rho)=\inf_{\{p_\lambda,\eta_\lambda\}}
\sum_\lambda p_\lambda S(\eta_{\lambda,B'}).
```

This is the convex-roof quantity of [Bennett, DiVincenzo, Smolin, and Wootters](https://arxiv.org/abs/quant-ph/9604024v2). A mathematical decomposition of a density operator is not a physical classical record delivered to Alice or Bob. Different decompositions represent the same input resource, and the actual local operations are fixed independently of $`\lambda`$.

For the proof, one may purify the resource by attaching an inaccessible register with basis $`|\lambda\rangle`$. Local instruments can likewise retain their Kraus indices in local environments. Their outgoing classical outcomes remain only $`a,b`$. General final CPTP decoders are dilated and padded to unitaries $`W_{ab},V_{ab}`$ on common finite spaces. Padding adds local pure registers; it does not add entanglement or a message.

These choices give one full-protocol isometry,

```math
F|\psi\rangle
=\sum_{\lambda,a,b}\sqrt{p_\lambda}
 |\lambda,a,b\rangle_C
 (W_{ab}\otimes V_{ab})(A_a\otimes B_b)
 \bigl(|\psi\rangle\otimes|\eta_\lambda\rangle\bigr).
```

Tracing out $`C`$ and the local environments returns the original implemented channel. This construction permits a comparison of all branches at once. Correctness of that average channel does not imply the same diamond-error guarantee for every pure ensemble component separately. For example, a mixture that uses the ideal channel with probability $`1-p`$ and an arbitrarily inaccurate channel with probability $`p`$ has half diamond error at most $`p`$. Its exceptional component can still have order-one error.

<a id="unitary-continuity"></a>

## The continuity step imported from a primary paper

The existence and freedom of Stinespring representations are background for this argument. The numerical estimate used here is a further input: [vom Ende, Theorem 1, equation (13)](https://arxiv.org/html/2308.15389v3), for arbitrary dilations into the same environment when one channel has Kraus rank one. It builds on the continuity theory of [Kretschmann, Schlingemann, and Werner](https://doi.org/10.1109/TIT.2008.917696). It is not being attributed to a Watrous section or assumed as an unproved general conjecture.

For half diamond error $`\epsilon`$, the theorem supplies a normalized vector $`|\gamma\rangle`$ in the fixed full-protocol environment such that

```math
\|F-C_d\otimes|\gamma\rangle\|_\infty
\le\sqrt{2\|\Lambda-\mathrm{Ad}_{C_d}\|_\diamond}
\le2\sqrt\epsilon=:\kappa.
```

The ideal environment vector may be entangled across local environment factors. Its record weights need not equal the actual ensemble or measurement probabilities. Neither factorization nor equality of those weights is needed.

The same vector works for the complete controlled unitary, including coherent superpositions of Alice's control. Choosing unrelated ideal environments for control zero and control one would lose precisely the compatibility needed later. This is why a statement about two basis inputs, or about their average output fidelities, is insufficient.

An operator-norm isometry estimate becomes a channel estimate before any environment is discarded. With $`G=C_d\otimes|\gamma\rangle`$,

```math
FXF^\dagger-GXG^\dagger
=(F-G)XF^\dagger+GX(F-G)^\dagger,
```

so the trace-norm ideal property gives full diamond distance at most $`2\kappa`$. Tensoring with an untouched reference preserves the estimate. Any common CPTP postprocessing preserves this upper bound as well.

## From simultaneous timing to a flat comparison state

The converse applies a common mathematical postprocessing to the actual and ideal dilations: dephase the record, undo Bob's padded decoder, and discard Alice's systems and her outcome. This is a proof operation on an enlarged state, not a new capability assigned to Bob. In particular, he is not given the ensemble flag or access to the ideal environment.

For the actual dilation, the resulting Bob channel $`\mathcal R`$ is independent of Alice's input bit. Alice's local instrument is trace preserving when its outcome is summed, so it cannot change Bob's reduced pre-message state. The one simultaneous exchange is what allows this recovered state to be identified with a stage before Bob has used Alice's message.

For the ideal dilation, the two choices of Alice's bit instead give $`\mathcal T`$ and $`\mathcal T\circ\mathrm{Ad}_{Z_d}`$, using one common $`\mathcal T`$. The previous estimate therefore yields

```math
\|\mathcal R-\mathcal T\|_\diamond\le2\kappa,
\qquad
\|\mathcal R-\mathcal T\circ\mathrm{Ad}_{Z_d}\|_\diamond
\le2\kappa,
```

and hence $`\|\mathcal T-\mathcal T\circ\mathrm{Ad}_{Z_d}\|_\diamond\le4\kappa`$.

The cyclic average

```math
\mathcal D_d=\frac1d\sum_{j=0}^{d-1}\mathrm{Ad}_{Z_d^j}
```

removes all computational-basis off-diagonal entries: on $`|s\rangle\langle t|`$, the multiplier is the finite geometric sum $`d^{-1}\sum_j e^{2\pi i j(s-t)/d}`$. Telescoping the preceding approximate invariance through the powers of $`Z_d`$ gives

```math
\|\mathcal R-\mathcal T\mathcal D_d\|_\diamond\le2d\kappa.
```

The target dimension enters here; no local-memory dimension has appeared. Fourier input states become $`I_d/d`$ after $`\mathcal D_d`$. Applying Bob's original instrument to these inputs constructs actual conditional states and comparison states whose normalized blocks have maximum eigenvalue at most $`1/d`$. The proof retains Bob's decoder environment and uses a unitary on his full padded workspace. Each comparison block arises from $`I_d/d`$ tensored with a subnormalized environment state; bounding that state's largest eigenvalue by its trace and summing Alice's outcomes gives the stated ceiling. [Converse, Sections 4–6](../science/converse.md) gives the explicit block operators and the complete local extraction instrument. The exact extraction strategy descends from [Gonzales and Chitambar, Section V-C](https://arxiv.org/html/1810.00994v2).

<a id="entropy-without-workspace"></a>

## Conditional entropy without a workspace-dimension penalty

A direct entropy-continuity bound proportional to $`\log\dim K_B`$ would be unsuitable: the protocol class permits arbitrarily large finite $`K_B`$. The proof instead uses the comparison state's eigenvalue ceiling. The following argument explains both that replacement and the handling of different branch probabilities.

Suppose normalized states $`\tau,\sigma`$ satisfy $`\sigma\le I/r`$, and let $`t=\tfrac12\|\tau-\sigma\|_1`$. Dephasing $`\sigma`$ in an eigenbasis of $`\tau`$ gives distributions $`u,v`$ with $`v_i\le1/r`$ and total variation distance $`t'\le t`$. Their common part $`a_i=\min(u_i,v_i)`$ has mass $`c=1-t'`$. When $`c>0`$, the normalized common distribution has largest probability at most $`1/(rc)`$. Concavity and the elementary bound $`H(w)\ge-\log_2\max_i w_i`$ give

```math
S(\tau)=H(u)\ge c\log_2(rc)
\ge (1-t')\log_2r-h_2(t').
```

The function $`g_r(t)=(1-t)\log_2r-h_2(t)`$ decreases until $`r/(r+1)`$ and is nonpositive thereafter. Using $`t'\le t`$ in the decreasing range, and entropy nonnegativity otherwise, proves

```math
S(\tau)\ge g_r(t).
```

When the common mass is zero, entropy nonnegativity supplies the endpoint directly. Only $`r`$ enters this expression; the matrices may act on a much larger space.

Now retain the outcome labels and write the actual and ideal comparison states as

```math
\omega=\bigoplus_\ell p_\ell\tau_\ell,
\qquad
\sigma=\bigoplus_\ell q_\ell\sigma_\ell,
\qquad
\sigma_\ell\le I/r,
\qquad
\delta=\frac12\|\omega-\sigma\|_1.
```

The distributions $`p,q`$ need not agree. With $`t_\ell=\tfrac12\|\tau_\ell-\sigma_\ell\|_1`$, the triangle inequality gives

```math
\sum_\ell p_\ell t_\ell
\le\delta+\frac12\sum_\ell|p_\ell-q_\ell|
\le2\delta.
```

For zero-weight ideal blocks, any normalized state obeying the same eigenvalue ceiling can serve as the unused comparison block. Zero-weight actual blocks contribute nothing.

The function $`g_r`$ is convex. Jensen's inequality, followed by its decrease on $`[0,1/2]`$, shows that if $`2\delta\le\alpha\le1/2`$, then

```math
S(K_B\mid L)_\omega
=\sum_\ell p_\ell S(\tau_\ell)
\ge(1-\alpha)\log_2r-h_2(\alpha).
```

This controls quantum entropy conditioned on the classical record. An arbitrarily long record cannot supply the claimed entanglement by having a large classical entropy: its entropy is removed by conditioning. Neither the number of outcomes nor the workspace dimension occurs in the bound.

For each fixed pure resource component, Bob's extraction instrument has pure conditional outputs on $`A'K_B`$. Their two marginal entropies agree. Averaging the Alice marginals recovers her original marginal, so entropy concavity bounds their average entropy by $`S(\eta_{\lambda,A'})`$. The extraction instrument is independent of $`\lambda`$. Averaging this inequality over an arbitrary ensemble and then taking the convex-roof infimum yields a bound on the actual mixed resource's $`E_F`$.

Here the proof has $`\delta\le r\kappa`$, so the parameter is $`\alpha=2r\kappa=4r\sqrt\epsilon`$. The finite conclusion is

```math
E_F(\rho)\ge
(1-4r\sqrt\epsilon)\log_2r-h_2(4r\sqrt\epsilon),
\qquad 4r\sqrt\epsilon\le\frac12.
```

For $`r<d`$, a local encoding into the appropriate phase-gradient subspace and a CPTP decoder that also accounts for leaked population transfer the same argument to $`C_r`$. Merely projecting and conditioning on no leakage would change the channel task. The [converse](../science/converse.md) proves this restriction, and the [frontier note](../science/frontier.md) optimizes over $`r`$.

<a id="timing-and-resources"></a>

## What the bound counts, and what implementation still costs

The leading law is

```math
m-O(\log(m+1))\le E_{\mathrm{sim}}(n,\epsilon)\le m+O(1),
\qquad
m=\min\left\{n,\frac12\log_2\frac1\epsilon\right\},
\qquad 0<\epsilon\le\frac12.
```

It compares entanglement of formation across finite protocols with one simultaneous classical exchange. It does not close the finite additive gap or require growth with $`n`$ at fixed positive error. Entanglement entropy, Schmidt rank, and an integer Bell-pair supply are related but different quantities: the ideal sine state has entropy $`H(c^2)\le\log_2R`$, whereas exact deterministic preparation from Bell pairs requires $`\lceil\log_2R\rceil`$ of them.

The [implementation account](../science/resource_accounting.md) charges offline preparation, finite registers, messages, powers of the known target unitary, and synthesis precision. For $`Z_{2^n}`$ and $`R=2^w`$, it gives explicit short local circuits and a finite error budget. Offline heralding prepares the resource before unknown inputs arrive; a capped schedule includes its failure event in the unconditional error. It is distinct from accepting only favorable online gate outcomes.

For a general known $`V`$, writing a controlled $`V^k`$ does not provide it at unit cost. An inverse must come from a specified implementation, and the phase convention of $`V`$ matters because a global phase of $`V`$ becomes a relative phase in $`C(V)`$. Generic powers can require work proportional to $`R`$. The efficient phase-gradient implementation uses its explicit binary structure rather than a promise of free spectral data or a forward-only black box.

One ebit with two ordered messages can implement the same controlled gate exactly. The second party's intermediate action depends on the first message, so that protocol does not satisfy the simultaneous schedule. Conversely, allowing uncharged simultaneous quantum messages changes the resource model. A bound on classical-message entanglement cost cannot simply be relabeled as an entanglement-only bound in that broader model.

<a id="attribution"></a>

## Attribution of the ingredients

The book is the single educational anchor; the specialized claims retain their primary research citations.

- [Gonzales–Chitambar](https://arxiv.org/html/1810.00994v2), Theorem 3 and Section V-C, supply the exact distinct-eigenphase bound, mixed-resource formulation, and Fourier-extraction precedent.
- [Yu–Griffiths–Cohen](https://arxiv.org/abs/1109.5013v2) and [Yu](https://arxiv.org/html/1112.0307v3) supply finite-group fast protocols. The cyclic construction and the exact endpoint retain that attribution. [Randomized spectral rounding](../science/randomized_rounding.md) already recovers the same leading upper accuracy coefficient from a cyclic protocol.
- [Eisert and collaborators](https://arxiv.org/abs/quant-ph/0005101v2) supply the interactive remote-control comparison.
- [Berry–Wiseman](https://arxiv.org/html/quant-ph/0009117v2) and [Yang–Renner–Chiribella](https://arxiv.org/html/2007.10363v3) give sine-profile antecedents in phase estimation and unitary programming. The profile's optimization inside this shift construction is not an all-protocol entanglement optimality theorem.
- The fixed-environment unitary-target continuity estimate is the [vom Ende theorem](https://arxiv.org/html/2308.15389v3) identified above. The unconditional mixed-resource argument and its unequal-weight entropy estimate are developed explicitly in the [converse](../science/converse.md).

[Related work](../references/RELATED_WORK.md) compares the current Cleve–May criteria in both orientations and distinguishes Folkertsma and collaborators' exact impossibility results from this finite-error family. [Bibliographic records](../references/references.bib) identify the versions used. The project's quantitative content is the robust mixed-resource converse for the phase gradient, paired with constructions matching its leading accuracy dependence.
