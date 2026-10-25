# Explicit protocols for a remote controlled gate

[Model](model.md) · [Resource accounting](resource_accounting.md) · [Tradeoff](frontier.md) · [Related work](../references/RELATED_WORK.md)

Alice holds a control qubit $`A`$, Bob holds a target $`B`$, and the desired gate is

```math
C(V)=|0\rangle\langle0|_A\otimes I_B
     +|1\rangle\langle1|_A\otimes V_B.
```

The unitary $`V`$ is known, including the phase convention that fixes its controlled version. All correctness statements hold, to the stated channel error, for inputs entangled with an untouched reference. Error always means half diamond distance. Offline resource preparation is completed before the unknown input arrives.

The phase of $`V`$ is relevant target data: for $`P(\phi)=\mathrm{diag}(1,e^{i\phi})`$,

```math
C(e^{i\phi}V)=(P(\phi)\otimes I_B)C(V).
```

Thus a phase that would be global for an isolated application of $`V`$ becomes a relative control phase in this task. Only overall phases of completed, unconditionally applied physical operations can be removed during the [local compilation](resource_accounting.md) account.

Three protocols make the communication comparison explicit. The first gives a finite-resource approximation for any known $`V`$ using one simultaneous exchange. The second is the inherited exact cyclic protocol when $`V`$ has finite order. The third uses one Bell pair and two causally ordered messages. Preparation, compilation, workspace, and message lengths are detailed in [resource accounting](resource_accounting.md).

## 1. A noncyclic shift and a tapered resource

### Resource and local operations

Fix an integer $`R\ge1`$ and a real nonnegative normalized vector $`c=(c_0,\ldots,c_{R-1})`$. Share

```math
|\eta_c\rangle_{ab}=\sum_{k=0}^{R-1}c_k|k\rangle_a|k\rangle_b,
\qquad \sum_{k=0}^{R-1}c_k^2=1.
```

Set $`c_k=0`$ outside this interval. Alice holds $`a`$ and Bob holds $`b`$. Let $`\omega_R=e^{2\pi i/R}`$ and fix Bob's Fourier measurement convention as

```math
|f_q\rangle=\frac1{\sqrt R}\sum_{k=0}^{R-1}\omega_R^{qk}|k\rangle,
\qquad q\in\{0,\ldots,R-1\}.
```

**Before exchanging messages**, the parties perform the following independent local operations.

**Alice's local operation.** Alice applies the controlled noncyclic translation

```math
|x\rangle_A|k\rangle_a\longmapsto
|x\rangle_A|k-x\rangle_a,
\qquad x\in\{0,1\}.
```

Its output labels are $`-1,0,\ldots,R-1`$. This is an isometry on the occupied input subspace and has a local unitary extension after padding. Alice measures this register and records $`j`$.

**Bob's local operation.** Bob applies the known local multiplexed unitary

```math
M_V=\sum_{k=0}^{R-1}|k\rangle\langle k|_b\otimes V^k_B,
```

then measures $`b`$ in the Fourier basis and records $`q`$.

Alice sends $`j`$ and Bob sends $`q`$ in one simultaneous classical exchange. Neither preceding operation uses the remote outcome. **After receiving the messages**, Bob applies $`V^{-j}`$ and Alice applies

```math
P_q=|0\rangle\langle0|+\omega_R^q|1\rangle\langle1|.
```

The outcome $`j=-1`$ calls for $`V`$, not an undefined boundary operation. Every outcome is retained. No success test or additional message is performed on the unknown input.

### Corrected branch operators

For a control value $`x`$, Alice's outcome forces $`k=j+x`$. Bob's Fourier bra contributes $`R^{-1/2}\omega_R^{-q(j+x)}`$. Thus the uncorrected branch operator is

```math
L_{j,q}=\frac1{\sqrt R}\sum_{x=0}^1
c_{j+x}\omega_R^{-q(j+x)}
|x\rangle\langle x|\otimes V^{j+x}.
```

Coefficients outside the supported range vanish. Applying the two local corrections gives

```math
K_{j,q}=(P_q\otimes V^{-j})L_{j,q}
=\frac{\omega_R^{-qj}}{\sqrt R}
\left[\begin{pmatrix}c_j&0\\0&c_{j+1}\end{pmatrix}\otimes I_B\right]
C(V).
```

These operators are a complete Kraus family: summing over $`q`$ removes the factor $`1/R`$, and

```math
\sum_{j=-1}^{R-1}
\begin{pmatrix}c_j^2&0\\0&c_{j+1}^2\end{pmatrix}=I_A.
```

The boundary branches are included in this identity. Replacing the noncyclic shift by a cyclic shift for a general $`V`$ would change the implemented gate on those branches.

### Exact residual channel and diamond error

Define the neighboring-amplitude overlap

```math
f(c)=\sum_{k=0}^{R-2}c_kc_{k+1}.
```

Summing the corrected branches preserves both diagonal control blocks and multiplies each off-diagonal control block by $`f(c)`$. Therefore the implemented channel is exactly

```math
\Lambda_c=(\mathcal D_{f(c)}\otimes\mathrm{Id}_B)
\circ\mathrm{Ad}_{C(V)},
\qquad
\mathcal D_f=\frac{1+f}{2}\mathrm{Id}
             +\frac{1-f}{2}\mathrm{Ad}_Z.
```

Control dephasing commutes with $`C(V)`$. Since $`\|\mathrm{Ad}_Z-\mathrm{Id}\|_\diamond=2`$, the error is

```math
\epsilon(c)=\frac12\|\Lambda_c-\mathrm{Ad}_{C(V)}\|_\diamond
=\frac{1-f(c)}{2}.
```

The equality follows both from the Pauli-mixture upper bound and from the perfectly distinguishable outputs of $`\mathrm{Id}`$ and $`\mathrm{Ad}_Z`$ on $`|+\rangle`$. Unitary invariance removes $`C(V)`$. The expression is independent of Bob's dimension and of the spectrum of $`V`$.

### Optimal profile within this protocol

Let $`A_R`$ be the real $`R\times R`$ matrix with $`1/2`$ immediately above and below its diagonal and zero elsewhere. Then $`f(c)=c^TA_Rc`$. Its eigenvectors have components $`\sin[\ell\pi(k+1)/(R+1)]`$, and its eigenvalues are $`\cos[\ell\pi/(R+1)]`$, for $`\ell=1,\ldots,R`$. The largest eigenvalue has a positive normalized eigenvector,

```math
c_k=\sqrt{\frac{2}{R+1}}\sin\!\left(\frac{\pi(k+1)}{R+1}\right),
\qquad k=0,\ldots,R-1.
```

Consequently,

```math
f_R=\cos\!\left(\frac{\pi}{R+1}\right),
\qquad
\epsilon_R=\sin^2\!\left(\frac{\pi}{2(R+1)}\right)
\le\frac{\pi^2}{4(R+1)^2}.
```

This optimizes the profile at fixed support size **within the displayed shift protocol**. It does not assert that this resource minimizes entanglement among all simultaneous-exchange protocols. Sine profiles and closely related shift-overlap optimizations have antecedents in phase estimation and programmable operations; see [related work](../references/RELATED_WORK.md).

The pure resource has Schmidt rank $`R`$ and entanglement

```math
E_F(|\eta_R\rangle)=H(c_0^2,\ldots,c_{R-1}^2)\le\log_2R.
```

For any target error $`\epsilon>0`$, a finite $`R`$ satisfying $`R+1\ge\pi/(2\sqrt\epsilon)`$ suffices in the ideal local-operation model. Replacing any integer rank by the next power of two increases its logarithm by less than one. Writing $`R=2^w`$ for the efficient binary-register implementation,

```math
w=\left\lceil\log_2\max\!\left\{1,\frac{\pi}{2\sqrt\epsilon}\right\}\right\rceil
```

is a convenient sufficient choice. A shared error budget for preparation and local synthesis changes this expression by only an additive constant. The fully charged construction is in [resource accounting](resource_accounting.md).

## 2. The exact cyclic protocol

Suppose $`V^D=I`$ for an integer $`D\ge1`$. The finite cyclic-group construction of Yu–Griffiths–Cohen and Yu gives an exact protocol; the following is its binary-control specialization. Sources and attribution are collected in [related work](../references/RELATED_WORK.md).

Share

```math
|\Phi_D\rangle_{ab}=\frac1{\sqrt D}\sum_{k=0}^{D-1}|k,k\rangle.
```

Alice subtracts her control modulo $`D`$ from $`a`$, measures $`a`$, and obtains $`j\in\mathbb Z_D`$. Independently, Bob applies $`\sum_k|k\rangle\langle k|\otimes V^k`$ and Fourier-measures $`b`$, obtaining $`q\in\mathbb Z_D`$. They exchange $`j,q`$ simultaneously. Bob applies $`V^{-j}`$ and Alice applies $`\mathrm{diag}(1,e^{2\pi iq/D})`$.

Here $`k=j+x\pmod D`$ and $`V^D=I`$ imply $`V^k=V^{j+x}`$ even on the wrap-around branch. The Fourier phase is also periodic. Every corrected branch is therefore

```math
K^{\mathrm{cyc}}_{j,q}=\frac{e^{-2\pi iqj/D}}{D}\,C(V).
```

There are $`D^2`$ branches, each with probability $`1/D^2`$ for every input, so the implemented channel is exactly $`\mathrm{Ad}_{C(V)}`$. The resource entanglement is $`\log_2D`$ and each message has $`D`$ possible values.

For the phase-gradient family $`V=Z_d`$, choose $`D=d=2^n`$. This uses exactly $`n`$ Bell pairs and $`n`$ classical bits in each direction. Combining this construction with the sine protocol gives

```math
E_{\mathrm{sim}}(n,\epsilon)
\le \min\!\left\{n,\frac12\log_2(1/\epsilon)+O(1)\right\}.
```

The coefficient in this upper bound also follows from the inherited cyclic protocol combined with [unbiased spectral rounding](randomized_rounding.md). The comparison to the robust converse is in the [tradeoff](frontier.md).

## 3. One Bell pair with two ordered messages

For every known $`V`$, an exact controlled gate can instead be implemented using one Bell pair and two directed classical messages. This is the standard remote controlled-gate or cat-state construction associated with Eisert and collaborators; see [related work](../references/RELATED_WORK.md).

Write a pure input, including any untouched reference in $`|\psi_x\rangle`$, as

```math
|\psi\rangle=\sum_{x=0}^1|x\rangle_A|\psi_x\rangle.
```

Share $`|\Phi_2\rangle_{ab}`$. Alice applies a CNOT from $`A`$ to $`a`$, measures $`a`$ in the computational basis, and sends the outcome $`s`$ to Bob. The unnormalized state of the remaining systems is

```math
\frac1{\sqrt2}\sum_{x=0}^1
|x\rangle_A|s\mathbin\oplus x\rangle_b|\psi_x\rangle.
```

After receiving $`s`$, Bob applies $`X_b^s`$, then a local controlled-$`V`$ from $`b`$ to $`B`$. He measures $`b`$ in the $`X`$ basis, with outcome $`t=0`$ for $`|+\rangle`$ and $`t=1`$ for $`|-\rangle`$, and sends $`t`$ to Alice. The resulting unnormalized state is

```math
\frac12\sum_{x=0}^1(-1)^{tx}|x\rangle_A V^x|\psi_x\rangle.
```

Alice applies $`Z_A^t`$. Each of the four corrected branches is $`C(V)/2`$, establishing exact operation. Bob's correction and gate depend on the first received bit; his second message is produced afterward. This is a protocol with two causally ordered directed messages, outside the one-simultaneous-exchange model.

For $`C_d`$ with $`n\ge1`$, one Bell pair is also the exact minimum for unrestricted LOCC entanglement of formation. Restrict Bob's input to the span of $`|0\rangle`$ and $`|d/2\rangle`$, on which $`Z_d`$ has eigenvalues $`+1,-1`$. The gate becomes controlled-$`Z`$ on this encoded qubit. Acting on two local $`|+\rangle`$ states produces one ebit, so LOCC monotonicity requires at least one ebit initially. This optimality statement is specific to the phase-gradient family; one Bell pair is merely a sufficient resource for an arbitrary controlled-$`V`$.

## 4. Timing and scope of the comparison

Both the tapered and cyclic constructions finish all resource preparation before the unknown input is supplied. Their online local operations produce one outgoing message per party without receiving the other. After that exchange, only local corrections remain. The interactive construction instead contains a message-dependent operation between its two directed messages.

This identifies a difference in the required causal structure of communication. It does not establish a total runtime advantage: local multiplexed powers, Fourier transforms, resource distribution, memory, and finite-precision synthesis all have physical costs. For a generic known $`V`$, local powers can be expensive. For $`Z_d`$, they have an explicit polynomial implementation in the register size and number of accuracy bits, detailed in [resource accounting](resource_accounting.md).
