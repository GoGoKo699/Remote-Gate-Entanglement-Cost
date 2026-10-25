# Relation to previous work

The result developed here is a quantitative entanglement lower bound for a controlled phase-gradient gate when the parties have one simultaneous exchange of **classical** messages. It permits arbitrary finite mixed resource states and local quantum memories. Its proof extends the exact Fourier-extraction argument of Gonzales and Chitambar using continuity of unitary dilations and an entropy estimate that does not depend on workspace dimension.

Write $`d=2^n`$, $`Z_d=\sum_{j=0}^{d-1}e^{2\pi i j/d}|j\rangle\langle j|`$, and $`C_d=|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes Z_d`$. Throughout this repository, accuracy means $`\tfrac12\|\Lambda-\mathrm{Ad}_{C_d}\|_\diamond\le\epsilon`$, and entanglement of formation $`E_F`$ is measured in bits. This is the convex-roof measure introduced by [Bennett, DiVincenzo, Smolin, and Wootters](https://arxiv.org/abs/quant-ph/9604024v2), not an identification of every mixed state's one-shot preparation cost with its entanglement of formation. The [finite converse](../science/converse.md) has the form

```math
E_F(\rho)\ge (1-\alpha_r)\log_2 r-h_2(\alpha_r),
\qquad \alpha_r=4r\sqrt{\epsilon}\le\tfrac12,
```

for every power of two $`r\le d`$. Together with explicit protocols, it determines the [leading dependence](../science/frontier.md), for $`0<\epsilon\le1/2`$, on

```math
m=\min\!\left\{n,\frac12\log_2\frac1\epsilon\right\}:
\qquad m-O(\log(m+1))\le E_{\mathrm{sim}}(n,\epsilon)\le m+O(1).
```

The remaining additive gap matters: this is a leading-order characterization, not a constant-additive formula for every finite error. The model and theorem also do not assert growth with $`n`$ at a fixed nonzero accuracy. The foundational measure reference has bibliography key `BennettDiVincenzoSmolinWootters1996`.

## Exact controlled-gate lower bound: Gonzales and Chitambar

[Gonzales and Chitambar, Theorem 3 and Section V-C](https://arxiv.org/html/1810.00994v2) prove that exact implementation of a binary-controlled unitary with $`s`$ distinct eigenphases requires at least $`\log_2 s`$ ebits under local operations and broadcast communication (LOBC). They explicitly extend the statement to mixed resources through entanglement of formation. Equations (69)–(79) compare the two control values and construct a Fourier-indexed local measurement extracting maximally entangled states. The remark following equation (79) identifies an approximate counterpart as an open direction.

Their Theorem 1 also gives an $`O(\log(1/\epsilon))`$ entanglement upper bound for arbitrary two-qubit gates, using the full diamond norm. Thus neither the exact LOCC–LOBC separation nor logarithmic dependence on accuracy originates here. The journal citation is **IEEE Transactions on Information Theory 66(5), 2951–2963 (2020)**; the 2019 date encountered in some bibliographies is the online-publication date. [Publisher record](https://ieeexplore.ieee.org/document/8886512).

The additional work needed for the present converse is quantitative. Approximate correctness of a mixed-resource protocol does not imply that each pure component separately approximates the target. The proof instead compares one dilation of the complete protocol, retaining the ensemble label only in the mathematical environment. It then controls changing branch probabilities and entropies without inserting the unbounded local workspace dimension into a continuity bound. The cyclic phase-gradient structure permits a quantitative twirl and restriction to smaller root-of-unity subspaces. These steps produce the displayed finite-error inequality.

Bibliography key: `GonzalesChitambar2020`.

## Fast protocols and the upper-bound comparison

[Yu, Griffiths, and Cohen](https://arxiv.org/abs/1109.5013v2) introduced fast implementations using simultaneous classical messages and shared entanglement. [Yu's subsequent group and quasigroup construction](https://arxiv.org/html/1112.0307v3), especially Sections II–IV, implements controlled operators drawn from finite-group representations and supplies approximate protocols for arbitrary controlled unitaries. The finite-group protocols consume a maximally entangled resource with Schmidt rank equal to the group order. Theorem 3 of the latter preprint gives $`O(d_B^4\log(1/\epsilon_0))`$ ebits for its general approximate construction, where $`\epsilon_0`$ is full diamond error. This is a bound for that general construction, not a lower bound on binary-controlled gates.

For $`C_d`$, the inherited cyclic protocol gives the exact $`n`$-ebit implementation. For an arbitrary known $`V`$, rounding its eigenphases to a common root-of-unity grid and applying the cyclic protocol already gives an upper bound independent of the target dimension, with logarithmic accuracy dependence. It would be misleading to compare the binary-controlled result only against the general $`d_B^4`$ expression.

A sharper comparison uses **unbiased randomized spectral rounding**. With grid spacing $`h=2\pi/R`$, shared randomness can choose adjacent grid phases so that the Hermitian phase error $`H_t`$ satisfies $`\mathbb E H_t=0`$ and $`\|H_t\|\le h`$. The linear term of the averaged channel error vanishes, giving $`O(h^2)`$ diamond error with $`\log_2R`$ ebits. This elementary extension of the cyclic method is derived in [randomized_rounding.md](../science/randomized_rounding.md); it is not attributed to an unverified prior theorem. It already gives the same leading $`\tfrac12\log_2(1/\epsilon)`$ upper dependence.

The tapered protocol supplies a different explicit realization. It uses powers of $`V`$ and a finite shared reference with sine Schmidt coefficients. Its residual noise is exactly dephasing on Alice's control, with half diamond error

```math
\epsilon_R=\frac{1-\cos[\pi/(R+1)]}{2}.
```

This exact noise formula does not require diagonalizing $`V`$. The sine construction and the randomized cyclic comparison support the same accuracy frontier; the matching general converse is the central distinction.

Bibliography keys: `YuGriffithsCohen2012`, `Yu2013FastControlled`. The second source is cited as **arXiv:1112.0307v3, 12 March 2013**, rather than being assigned an unverified journal publication.

## Sine profiles, finite references, and programming

The sine amplitude profile is established in quantum phase estimation. [Berry and Wiseman, equation (10)](https://arxiv.org/html/quant-ph/0009117v2), give the same finite-interval sine coefficients after relabeling $`R=N+1`$. Their equation (9) gives the corresponding inverse-square phase-variance scale, and they credit earlier phase-estimation work for the optimization. [Yang, Renner, and Chiribella](https://arxiv.org/html/2007.10363v3) connect optimal approximate unitary programming to metrology; their phase-gate example in equations (9)–(10) also uses a sine program and quadratic suppression of error with program dimension.

These precedents explain the profile and its scaling. Their resource tasks differ from the present one: an optical phase-estimation probe or a universal program register is not an arbitrary bipartite mixed resource implementing one fixed distributed gate. A program-dimension statement also does not directly bound entanglement of formation. The path-adjacency optimization used for the tapered protocol is a calculation within that construction; it does not prove that the sine resource minimizes entanglement among all allowed protocols.

Bibliography keys: `BerryWiseman2000`, `YangRennerChiribella2020`. The cited Yang–Renner–Chiribella arXiv v3 was revised in February 2021 and improves a dimension-dependent upper bound relative to the 2020 published article; their main accuracy conclusion is unchanged.

## Continuity input: KSW and vom Ende

[Kretschmann, Schlingemann, and Werner](https://doi.org/10.1109/TIT.2008.917696) established dimension-independent continuity of Stinespring representations. The specific fixed-environment statement used here is [vom Ende, Theorem 1, equation (13)](https://arxiv.org/html/2308.15389v3): when one channel has Kraus rank one, arbitrary Stinespring isometries into a common environment can be related by an environment unitary with distance at most the square root of twice the full diamond distance.

For a fixed dilation $`F`$ of the protocol and a unitary target $`U`$, this yields a normalized environment vector $`|\gamma\rangle`$ such that

```math
\|F-U\otimes|\gamma\rangle\|_\infty
\le\sqrt{2\|\Lambda-\mathrm{Ad}_U\|_\diamond}
\le2\sqrt\epsilon.
```

The environment includes discarded systems and the formal purification of the mixed resource. The vector need not factor between Alice and Bob or have the original ensemble probabilities. Preserving these freedoms is essential to the mixed-resource argument. The continuity theorem and its constant are imported tools.

Bibliography keys: `KretschmannSchlingemannWerner2008`, `VomEnde2023`. The published 2023 rank-one theorem suffices; no general KSW conjecture is assumed.

## Cleve and May: evaluating both orientations

[Cleve and May, version 4](https://arxiv.org/html/2602.00255v4), give noisy entanglement-of-formation lower bounds from controllable correlation (Theorem 15) and controllable entanglement (Definition 17 and Theorem 18). Their protocol model allows simultaneous **quantum** messages and mixed resources. Their noisy mixed-resource bounds have penalties depending on the input dimension. Their bounds therefore apply to a broader communication model, but their values must be evaluated on the gate family at issue. The following calculations specialize the ideal criteria to $`C_d`$; they are not claims made in that paper.

### Controllable correlation

With the reference $`Q`$ attached to Alice's control, Bob's input induces a qubit dephasing channel on $`A`$. Up to a local output phase, this channel is a mixture of the identity and Pauli $`Z`$. Adjoining the binary mixture flag shows that its output mutual information lies between the input mutual information minus one bit and the input mutual information. Thus varying Bob's input changes $`I(Q:A)`$ by at most one bit.

With the reference attached to Bob's target, the reduced output for a fixed reference–target input $`\omega_{QB}`$ has the form

```math
\omega_p=(1-p)\omega_{QB}
+p(I_Q\otimes Z_d)\omega_{QB}(I_Q\otimes Z_d^\dagger).
```

Introduce a classical bit recording the mixture branch. Its conditional mutual information is between zero and one, while both branches have the same mutual information as the input. Consequently,

```math
I(Q:B)_\omega-1\le I(Q:B)_{\omega_p}\le I(Q:B)_\omega.
```

The output mutual information varies by at most one. Their correlation lower bound has a factor of one-half, so it yields at most one-half ebit in either orientation. This value is attained: for a Bell reference on the control, compare a target eigenstate with $`(|0\rangle+|d/2\rangle)/\sqrt2`$; for a maximally entangled reference on the target, compare control inputs $`|0\rangle`$ and $`|+\rangle`$. In each case the mutual information changes by one bit. Neither orientation gives a lower bound growing with $`n`$ or with the requested number of accuracy bits.

### Controllable entanglement

Definition 17 of the cited version requires one test output to be exactly separable. For a reference on Alice's qubit, the other output's entanglement of formation is at most one. For a reference maximally entangled with Bob's target, every reduced reference–target output is supported on

```math
\mathrm{span}\left\{
|\Phi_d\rangle,(I\otimes Z_d)|\Phi_d\rangle
\right\}.
```

These two vectors are orthogonal. Let $`P`$ project onto their span. A separable state $`\sigma`$ obeys $`\mathrm{Tr}(P\sigma)\le2/d`$, because its overlap with either maximally entangled vector is at most $`1/d`$. Every such output $`\omega_p`$ therefore satisfies

```math
\inf_{\sigma\in\mathrm{SEP}}\|\omega_p-\sigma\|_1
\ge2(1-2/d).
```

For every $`d>2`$, this is strictly positive, so no output can satisfy the required separability condition in the target-reference orientation. The remaining $`d=2`$ case has an entanglement ceiling of one. Thus this second criterion also does not yield the precision-dependent lower bound considered here.

The distinction is quantitative and model specific. It does not imply a limitation of all possible lower-bound methods in the quantum-message model. Teleporting a total of $`q`$ quantum message qubits converts such a protocol into the classical-message model using $`q`$ additional Bell pairs, so the present argument instead lower-bounds $`E_F(\rho)+q`$ when quantum communication is included and charged.

Bibliography key: `CleveMay2026`, **arXiv:2602.00255v4, 29 April 2026**. Its displayed error parameters are full diamond distances; they must be doubled when translating from this repository's half diamond convention.

## Folkertsma and collaborators: exact impossibility

[Folkertsma, Grinko, Muuss, and Speelman](https://arxiv.org/html/2609.40228v1), Theorem 1.1 and Section 5, show that Haar-almost every bipartite unitary has no exact finite-resource protocol, even with simultaneous quantum messages. They also give explicit controlled-phase examples when the phase factor is transcendental. Their model includes retained quantum memories and general local channels; it is not a restricted final-correction model. Section 1 explicitly distinguishes classical and quantum simultaneous communication.

The phase-gradient family here has root-of-unity phases and an exact finite cyclic implementation. It therefore belongs to a structured implementable family, consistent with their result. Their exact impossibility theorem does not supply the finite-error entropy-versus-accuracy inequality for this family. Conversely, the present theorem does not prove exact impossibility for generic gates.

Bibliography key: `FolkertsmaEtAl2026`, **arXiv:2609.40228v1, 30 September 2026**.

## Interactive implementation and local circuit costs

The remote-control method of [Eisert and collaborators](https://arxiv.org/abs/quant-ph/0005101v2) provides the standard interactive comparison. Applied to a known Bob-local $`V`$, it uses one Bell pair and two causally ordered directed classical messages. The chronology is the resource difference: the second party acts using the first message before returning the second. The gate's controlled-Z restriction witnesses one ebit of entangling power for the phase-gradient family.

Local gate compilation is separately charged. [Dawson and Nielsen](https://www.rintonpress.com/journals/doi/QIC6.1-6.html) provide a conservative polylogarithmic compilation guarantee. [Ross and Selinger](https://www.rintonpress.com/journals/doi/QIC16.11-12-1.html) give sharper Clifford+T synthesis results with explicitly stated computational assumptions and typical-case bounds; those qualifications must accompany any such use. [Cuccaro and collaborators](https://arxiv.org/abs/quant-ph/0410184v1) supply a standard reversible ripple-carry arithmetic construction. None of these local compilation results supplies the simultaneous-message entanglement converse.

Bibliography keys: `EisertEtAl2000`, `DawsonNielsen2006`, `RossSelinger2016`, `CuccaroEtAl2004`.

## Broader context and scope

[May's book-length survey](https://arxiv.org/html/2605.02840v3), particularly Chapter 9, places entropy and entanglement lower bounds alongside the upper constructions and applications of non-local computation. Its default simultaneous-quantum-message model must be distinguished from the classical-message restriction here. The cited version is **v3, 15 September 2026** (`May2026Survey`).

The comparison supports a precise scope: a robust mixed-resource converse for the phase-gradient family, paired with constructions that match its leading accuracy cost. It leaves open the finite additive gap, a general characterization for arbitrary controlled spectra, and optimal local runtime. The exact separation, finite-group protocols, sine profiles, and continuity theorem retain their respective attributions above.

Complete bibliographic records, including the versions used, appear in [references.bib](references.bib).
