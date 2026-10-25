# Preparation and implementation costs

[Model](model.md) · [Protocols](protocols.md) · [Tradeoff](frontier.md) · [Related work](../references/RELATED_WORK.md)

The entanglement bounds concern the preshared state and the causal structure of online communication. This page supplies a concrete local implementation and distinguishes those quantities from Bell-pair supply, preparation work, classical bits, workspace, and gate precision. The construction uses ordinary finite registers and explicitly specified rotations. It requires no quantum random-access memory or oracle for spectral data.

The efficient register implementation takes $`R=2^w`$. Its ideal tapered resource is

```math
|\eta_R\rangle=\sum_{k=0}^{R-1}c_k|k,k\rangle,
\qquad
c_k=\sqrt{\frac{2}{R+1}}\sin\!\left(\frac{\pi(k+1)}{R+1}\right).
```

The exact ideal-protocol error is $`\epsilon_R=\sin^2[\pi/(2(R+1))]`$, as derived in [protocols](protocols.md). Taking $`w=\tfrac12\log_2(1/\epsilon)+O(1)`$ leaves a constant fraction of the requested error for preparation and synthesis. For the phase-gradient family, use the exact cyclic protocol if its $`n`$-Bell-pair resource is smaller.

## 1. Entanglement entropy and Bell-pair supply

Because $`|\eta_R\rangle`$ is pure, its entanglement of formation is

```math
E_F(|\eta_R\rangle)=H(p_0,\ldots,p_{R-1}),
\qquad p_k=\frac{2}{R+1}\sin^2\!\left(\frac{\pi(k+1)}{R+1}\right).
```

This is at most $`\log_2R`$. In fact, a Riemann sum gives

```math
H(p)=\log_2(R+1)-\frac{1-\ln2}{\ln2}+o(1).
```

To obtain the constant, subtract $`\log_2(R+1)`$ and use
$`\int_0^1 2\sin^2(\pi x)\ln[2\sin^2(\pi x)]\,dx=1-\ln2`$.

An exact deterministic preparation of this rank-$`R`$ pure state from Bell pairs requires at least $`\lceil\log_2R\rceil`$ Bell pairs: a local measurement branch cannot increase the Schmidt rank beyond the initial rank $`2^b`$ of $`b`$ Bell pairs. That many also suffice, by the explicit conversion below. Thus the entropy and the exact one-copy Bell-pair cost are different, even though they have the same leading logarithmic scaling. The cost function $`E_{\mathrm{sim}}`$ is an infimum of $`E_F`$ for one implementation, as defined in the [model](model.md); no many-copy regularization is implicit.

For arbitrary integer $`R`$, pad the coefficient vector by zeros to dimension $`2^{\lceil\log_2R\rceil}`$ in the conversion below. A prescribed finite local pure state can be prepared exactly by a fixed local unitary in the ideal local-operation model; the deterministic Bell-pair sufficiency statement therefore does not rely on repeat-until-success preparation. The simple efficient Fourier and heralded preparation circuits used here are specified for $`R=2^w`$. This restriction changes the entanglement upper bound by only an additive constant.

## 2. Preparing the sine amplitudes locally

### An explicit circuit with constant success probability

Alice first prepares a local $`w`$-qubit register $`K`$ uniformly and a flag qubit $`h`$ in $`|0\rangle`$. Write $`k=\sum_{s=0}^{w-1}2^s k_s`$ and define $`R_y(\theta)=e^{-i\theta Y/2}`$. Apply a base rotation to the flag and one controlled rotation for each bit:

```math
R_y\!\left(\frac{2\pi}{R+1}\right)
\quad\text{and}\quad
\mathrm{controlled}_{k_s}\!-
R_y\!\left(\frac{2\pi 2^s}{R+1}\right),
\qquad s=0,\ldots,w-1.
```

All rotate the same flag about the same axis. On a fixed computational label $`k`$, their angles add. The resulting state is

```math
\frac1{\sqrt R}\sum_{k=0}^{R-1}|k\rangle_K
\left[
\cos\!\left(\frac{\pi(k+1)}{R+1}\right)|0\rangle_h
+\sin\!\left(\frac{\pi(k+1)}{R+1}\right)|1\rangle_h
\right].
```

Measure $`h`$. If the result is one, $`K`$ is exactly

```math
|c\rangle=\sum_{k=0}^{R-1}c_k|k\rangle.
```

The success probability is

```math
p_R=\frac1R\sum_{k=0}^{R-1}
\sin^2\!\left(\frac{\pi(k+1)}{R+1}\right)
=\frac{R+1}{2R}>\frac12.
```

On failure, Alice discards and resets these local registers and repeats. The expected number of attempts is $`1/p_R<2`$. Each attempt uses $`w`$ Hadamards, one base rotation, $`w`$ controlled rotations, and one measurement. Each controlled rotation has a constant-size decomposition into single-qubit rotations and CNOTs. Thus this is an explicit expected-$`O(w)`$ local preparation in an arbitrary-rotation gate model. The rotation angles are a short analytic list; no table of $`R`$ amplitudes is loaded.

These attempts occur before the unknown input arrives and before the Bell pairs are acted upon. Failed attempts consume local work and time, but they do not consume additional Bell pairs. This is offline heralding of a resource, not postselection of a gate applied to an unknown input.

### A bounded preparation schedule

For a strict finite preparation schedule, stop after $`T`$ attempts. With ideal rotations, the probability of obtaining no success is at most $`2^{-T}`$. On that event the parties can discard the unused Bell pairs, prepare a product resource $`|0,0\rangle`$, and run the same online protocol. A failure flag is communicated offline. This gives an ordinary trace-preserving overall implementation; the failure event is included in its error.

If the failure probability is $`\nu`$, replacing the ideal resource by this mixture changes the induced channel by at most $`\nu`$ in half diamond distance. Alternatively, when there is no fixed delivery deadline, Alice may repeat until the herald succeeds and supply the input only afterward. In either case, each subsequent online protocol has exactly one simultaneous classical exchange and finite registers. Finite-precision success probabilities and a fully specified finite error budget appear below.

## 3. Converting Bell pairs into the shared resource

Assume $`R=2^w`$ and that the parties already share $`w`$ Bell pairs, equivalently $`|\Phi_R\rangle_{ab}`$. Alice has prepared $`|c\rangle_K`$ locally. She subtracts her resource label from $`K`$ modulo $`R`$:

```math
|k\rangle_a|t\rangle_K\longmapsto
|k\rangle_a|t-k\bmod R\rangle_K.
```

The joint state becomes

```math
\frac1{\sqrt R}\sum_{k,t=0}^{R-1}
c_t|k,k\rangle_{ab}|t-k\bmod R\rangle_K.
```

Alice measures $`K`$, obtaining $`s`$. Each outcome has probability $`1/R`$, and the normalized remaining state is

```math
\sum_{k=0}^{R-1}c_{k+s\bmod R}|k,k\rangle.
```

She sends the $`w`$-bit value $`s`$ to Bob **offline**. Both parties cyclically shift their resource labels by $`+s`$. Relabeling $`t=k+s\pmod R`$ leaves exactly $`|\eta_R\rangle`$. All outcomes give the same corrected state, so this conversion itself is deterministic and needs no entanglement postselection.

Equivalently, Alice has implemented the diagonal instrument

```math
M_s=\mathrm{diag}_{k=0}^{R-1}(c_{k+s\bmod R}),
\qquad \sum_s M_s^\dagger M_s=I.
```

The modular subtraction and shifts have linear-size reversible ripple-carry implementations, with clean carry ancillas; the standard construction of Cuccaro and collaborators is included in [related work](../references/RELATED_WORK.md). A conservative $`O(w)`$ workspace bound is sufficient here. The offline conversion uses one $`w`$-bit directed message in addition to whatever physical process establishes the initial Bell pairs. With a capped preparation schedule, add an offline success/failure bit.

The same construction applies to any normalized coefficient vector. In particular, a small error in the locally prepared state is not amplified by this conversion: its action on that state, after correcting and forgetting $`s`$, is the isometry $`|k\rangle\mapsto|k,k\rangle`$. Trace distance is preserved on the encoded state.

For completeness, take any integer rank $`R`$, put $`w=\lceil\log_2R\rceil`$ and $`N=2^w`$, and define a normalized padded vector $`a_t=c_t`$ for $`0\le t<R`$ and $`a_t=0`$ otherwise. Starting from $`w`$ Bell pairs, use $`|\Phi_N\rangle`$ and the instrument

```math
M_s=\mathrm{diag}_{k=0}^{N-1}(a_{k+s\bmod N}),
\qquad s=0,\ldots,N-1,
\qquad \sum_s M_s^\dagger M_s=I_N.
```

Every outcome has probability $`1/N`$. Both shifts by $`+s\bmod N`$ then give $`\sum_{t=0}^{N-1}a_t|t,t\rangle=\sum_{t=0}^{R-1}c_t|t,t\rangle`$. The extra local levels are unoccupied. This verifies exact deterministic conversion from $`\lceil\log_2R\rceil`$ Bell pairs for arbitrary $`R`$; it does not assert that the power-of-two Fourier circuit applies unchanged to a non-power-of-two protocol rank.

## 4. Online registers and classical messages

For the binary tapered implementation, return to $`R=2^w`$. Alice's mathematical output label lies in $`\{-1,0,\ldots,R-1\}`$. The implementation adds a zero high bit to her $`w`$-qubit resource register and performs controlled subtraction by one modulo $`2R`$. On the occupied subspace, the result represents $`k-x`$ in signed binary: $`2R-1`$ represents $`-1`$, while $`0,\ldots,R-1`$ retain their usual values. There is no physical wrap-around between the two occupied endpoints of the mathematical interval.

This controlled decrement has a reversible arithmetic circuit. For example, a carry/borrow register gives linear-size arithmetic; even a direct decomposition using multi-controlled bit flips uses only polynomially many gates and $`O(w)`$ clean work qubits. Bob uses a $`w`$-qubit resource register and its inverse quantum Fourier transform before computational-basis measurement. The standard binary Fourier circuit has $`O(w^2)`$ controlled phase rotations and $`O(w)`$ Hadamards and swaps.

The fixed-length message costs are as follows. They count online messages only, after offline resource preparation is complete.

| Protocol | Alice to Bob | Bob to Alice | Communication dependence |
| --- | --- | --- | --- |
| Tapered, $`R=2^w`$ | $`w+1`$ bits for $`j`$ | $`w`$ bits for $`q`$ | One simultaneous exchange |
| Exact cyclic, $`D=2^n`$ | $`n`$ bits | $`n`$ bits | One simultaneous exchange |
| Interactive controlled gate | One bit | One bit | Bob's message is produced after receiving Alice's bit |

The tapered construction uses $`w`$ preshared resource qubits at each site. Alice needs one additional online label bit and at most $`O(w)`$ arithmetic workspace. Her offline preparation also uses a $`w`$-qubit amplitude register and a flag, which can be released before the input arrives. Bob retains his target and $`w`$ resource qubits, plus any workspace used by his implementation of $`V`$. For the phase-gradient target, total quantum storage across the two laboratories is $`O(n+w)`$, including the input, shared resource, and these workspaces. This counts qubits, not their storage lifetime.

## 5. General known unitaries: powers must be implemented

The online multiplexor is

```math
M_V=\sum_{k=0}^{R-1}|k\rangle\langle k|\otimes V^k.
```

Writing $`k`$ in binary implements it using controlled powers $`V^{2^s}`$, controlled on the $`s`$th resource bit. A short list of such powers does not make their implementation free. If an elementary known circuit for $`V`$ is the starting point, a direct realization makes

```math
\sum_{s=0}^{w-1}2^s=R-1
```

controlled applications of that circuit. After receiving $`j`$, Bob also needs $`V^{-j}`$: at most $`R-1`$ applications of the known inverse for $`j\ge0`$, or one forward application for $`j=-1`$. The direct local cost is therefore $`O(RG_V)`$ if a controlled implementation of the supplied circuit has cost $`O(G_V)`$. With $`R=O(1/\sqrt\epsilon)`$, this need not be polynomial in $`\log(1/\epsilon)`$.

The assumption is a known circuit or another explicit implementation of $`V`$, including its controlled form and its phase convention. If a circuit represents $`e^{i\phi}V`$ rather than $`V`$, the known phase $`\phi`$ must be compensated on the control when forming a controlled operation. It cannot be discarded as a global phase of the target gate. Reversing a known unitary circuit supplies its inverse; access only to an unknown forward oracle does not. A classical dense matrix description also does not, by itself, promise an efficient local circuit. These protocols make no forward-query complexity or generic fast-forwarding claim.

## 6. The phase-gradient family has explicit short circuits

For $`V=Z_{2^n}`$, write Bob's input label as $`x=\sum_{t=0}^{n-1}2^t x_t`$ and his resource label as $`k=\sum_{s=0}^{w-1}2^s k_s`$. Then the multiplexor is diagonal with phase

```math
e^{2\pi ikx/2^n}
=\prod_{s=0}^{w-1}\prod_{t=0}^{n-1}
\exp\!\left(2\pi i\,2^{s+t-n}k_sx_t\right).
```

Each factor is one known controlled phase rotation between resource bit $`k_s`$ and target bit $`x_t`$. Factors with $`s+t\ge n`$ are identity. At most $`nw`$ such rotations suffice. This circuit uses the binary representation directly; it neither enumerates eigenvalues nor loads a spectral table.

After learning $`j`$, Bob implements $`Z_{2^n}^{-j}`$ with at most $`n`$ single-qubit phase rotations,

```math
Z_{2^n}^{-j}
=\bigotimes_{t=0}^{n-1}
\mathrm{diag}\!\left(1,e^{-2\pi i j2^{t-n}}\right).
```

The angles are computed from the known classical integer $`j`$ and reduced modulo $`2\pi`$. Alice's correction is one phase rotation with angle $`2\pi q/R`$. Including Bob's Fourier transform and local arithmetic, the online circuit uses

```math
O(nw+w^2+n)
```

elementary rotations and reversible gates. The exact cyclic construction with $`D=2^n`$ has the same binary form with $`w=n`$, and uses $`O(n^2)`$ local gates in this gate model. The interactive one-Bell-pair construction uses $`O(n)`$ local controlled phase rotations on Bob's site.

These are gate-count upper bounds with ordinary local connectivity left unspecified. Routing on a particular device, entanglement distribution, gate duration, and memory noise require a separate hardware model. Counting one simultaneous exchange does not imply that the corresponding complete implementation finishes sooner.

The [randomized-rounding alternative](randomized_rounding.md) gives another polynomial local implementation for this family. It uses a maximally entangled resource and a finite shared random threshold, with its comparison and rounding arithmetic charged there.

## 7. Finite precision and a complete error budget

### How implementation errors enter

For a fixed online protocol, replacing a resource $`\rho`$ by $`\widetilde\rho`$ changes the induced channel by at most

```math
\frac12\|\Lambda_{\widetilde\rho}-\Lambda_\rho\|_\diamond
\le\frac12\|\widetilde\rho-\rho\|_1.
```

This follows by applying the same trace-preserving circuit to the input, its reference, and the two resource states, and using contractivity. It does not depend on the input dimension.

For local unitary gates, $`\|U-\widetilde U\|_\infty\le\delta`$ implies a half diamond channel error at most $`\delta`$. A hybrid argument therefore bounds the online synthesis error by the sum of the gate errors. The operator-norm comparisons below apply to fixed-phase $`SU(2)`$ elementary rotations after controlled gates have been decomposed. An irrelevant overall phase of a completed unconditionally applied block may be removed in making that comparison. For outcome-dependent corrections, the bound is uniform over all outcomes. Measurements, classical feedforward, and discarding do not increase it.

### Accuracy of the heralded preparation

Suppose the entire unitary for one local preparation attempt is synthesized to operator-norm error at most $`\zeta`$. Projecting onto the success flag changes the unnormalized successful vector by at most $`\zeta`$. If the ideal success probability is $`p_R`$, normalization gives

```math
D(|\widetilde c\rangle,|c\rangle)
\le \bigl\||\widetilde c\rangle-|c\rangle\bigr\|_2
\le \frac{2\zeta}{\sqrt{p_R}}
\le 2\sqrt2\,\zeta<3\zeta.
```

Here $`D`$ denotes trace distance between pure-state density operators. If $`\zeta\le1/8`$, the actual success probability obeys

```math
\widetilde p_R\ge(\sqrt{p_R}-\zeta)^2
\ge(1/\sqrt2-1/8)^2>1/3.
```

Thus the expected number of attempts remains below three, and a cap of $`T`$ attempts has failure probability at most $`(2/3)^T`$. The offline Bell-pair conversion preserves the successful state's trace-distance error. With the explicit fallback on failure, the total resource error is at most $`3\zeta+\nu`$.

### One sufficient finite choice

For a requested $`0<\epsilon\le1`$, allocate four equal portions of the error:

```math
\epsilon_R\le\epsilon/4,
\qquad 3\zeta\le\epsilon/4,
\qquad \nu\le\epsilon/4,
\qquad \delta_{\mathrm{online}}\le\epsilon/4.
```

For example, choose a power of two $`R\ge\pi/\sqrt\epsilon`$, set $`\zeta\le\epsilon/12`$, and use

```math
T=\left\lceil\frac{\ln(4/\epsilon)}{\ln(3/2)}\right\rceil.
```

The implemented trace-preserving channel then has half diamond error at most $`\epsilon`$. This finite construction has $`w=\tfrac12\log_2(1/\epsilon)+O(1)`$ and $`T=O(\log(1/\epsilon))`$. It starts from $`w`$ Bell pairs, so its resource entanglement of formation is at most $`w`$ even with preparation flags and approximation. The exact entropy formula for the ideal sine state is not silently substituted for the cost of its imperfect realization.

If the exact cyclic protocol has lower Bell-pair cost, it has no intrinsic approximation or sine-preparation error; allocate the error budget directly to its local implementation. Its description is exact in the unrestricted local-operation model. Exact realization of every root-of-unity rotation by a finite Clifford+T circuit is not assumed.

### Compilation to a discrete gate set

The preceding counts allow specified single-qubit rotations, CNOTs, and reversible arithmetic gates. Before synthesis, decompose the phase and controlled-rotation gates into $`SU(2)`$ rotations $`R_z(\theta)=e^{-i\theta Z/2}`$, $`R_y(\theta)=e^{-i\theta Y/2}`$, and Clifford gates. For example,

```math
P(\theta)=\mathrm{diag}(1,e^{i\theta})
=e^{i\theta/2}R_z(\theta),
```

and the two-qubit controlled phase satisfies

```math
\mathrm{CP}(\theta)
=e^{i\theta/4}
\bigl[R_z(\theta/2)\otimes R_z(\theta/2)\bigr]
\mathrm{CNOT}
\bigl[I\otimes R_z(-\theta/2)\bigr]
\mathrm{CNOT}.
```

The scalar in each equality is a global phase of the entire unconditionally applied operation and has no channel effect. Controlled $`R_y`$ similarly decomposes into two unconditionally applied $`R_y`$ rotations and two CNOTs. These decompositions preserve all relative phases of the controlled operations. In particular, the known phase defining $`C(V)`$ is retained before decomposition; an unknown phase of a controlled-$`V`$ oracle cannot be ignored. Reversible arithmetic uses Clifford and Toffoli gates, and Toffoli has an exact Clifford+T decomposition.

Choose $`SU(2)`$ representatives for the one-qubit Clifford+T generators. Solovay–Kitaev approximates the fixed-phase $`R_z`$ and $`R_y`$ matrices in operator norm using these representatives. Restoring the physical generators contributes only an overall phase to each unconditionally applied compiled block, which can be removed when applying the hybrid bound. This avoids assuming that arbitrary $`U(2)`$ phase gates $`P(\theta)`$ admit literal operator-norm approximation by Clifford+T words with their physical phases fixed; their determinant and global-phase restrictions must first be handled by the displayed decompositions.

To obtain a conservative fully discrete bound, let $`M`$ bound the number of rotations on a longest capped execution, including preparation attempts. For the phase-gradient construction one may take

```math
M=O(nw+w^2+n+wT).
```

Assign each elementary rotation an operator-norm error at most $`\epsilon/(C M)`$ for a sufficiently large absolute constant $`C`$. This meets both the one-attempt preparation requirement and the online hybrid bound. Standard Solovay–Kitaev compilation gives $`O(\log^c(M/\epsilon))`$ gates per rotation for a fixed constant $`c`$, hence

```math
O\!\left(M\log^c(M/\epsilon)\right)
```

gates overall, in addition to polynomial classical compilation and angle calculation. Dawson–Nielsen provide a constructive version; sharper single-qubit synthesis is available, but no optimal T count is needed here. Sources are in [related work](../references/RELATED_WORK.md). Angles such as $`2\pi2^s/(R+1)`$ and $`2\pi j2^{t-n}`$ are computed to the assigned precision from their explicit integer data.

Consequently the phase-gradient implementation has finite local workspace and a gate count polynomial in $`n`$ and $`\log(1/\epsilon)`$. This conclusion assumes ideal elementary gates from the chosen discrete set. Additional Bell-pair infidelity, physical gate errors, and storage noise enter through the same resource-distance or channel-error accounting; no device-specific tolerance or execution-time improvement is inferred.
