# A converse for one simultaneous exchange

This note proves a finite-error entanglement lower bound for a controlled phase gradient. The bound allows arbitrary finite mixed resource states, arbitrary finite local workspaces, and arbitrary local quantum channels after the messages arrive. Its dependence on the target dimension is explicit; its constants do not depend on the dimensions of the resource, workspace, or classical message registers.

The operational definitions are collected in [the model](model.md). The resulting accuracy frontier, including the upper construction and the interactive comparison, is proved in [the frontier note](frontier.md). Attribution and comparisons with other lower bounds are in [related work](../references/RELATED_WORK.md).

## 1. Statement and conventions

All logarithms are base two. The von Neumann entropy is $`S(\rho)=-\operatorname{Tr}(\rho\log_2\rho)`$, and $`h_2(t)=-t\log_2t-(1-t)\log_2(1-t)`$, with the usual continuous values at zero and one. Write $`\operatorname{Ad}_V(X)=VXV^\dagger`$.

Alice holds a qubit $`A`$. Bob holds a register $`B`$ of dimension $`d=2^n`$, where $`n\ge1`$. The target is

```math
Z_d=\sum_{j=0}^{d-1}e^{2\pi i j/d}|j\rangle\langle j|,
\qquad
C_d=|0\rangle\langle0|\otimes I_B
    +|1\rangle\langle1|\otimes Z_d.
```

An admissible protocol starts with a state $`\rho_{A'B'}`$ independent of the input. Both resource spaces are finite, but there is no common bound on their dimensions across protocols. Each party applies a local instrument, retaining any desired finite quantum memory and a classical outcome from an arbitrary finite alphabet. They then exchange their outcomes simultaneously. Each applies a local CPTP map that may depend on both outcomes, producing the prescribed quantum output. There is no subsequent message. Private local randomness, pure local ancillas, and discarded local environments are allowed. Shared randomness is included in the preshared resource registers.

Accuracy is measured on the unconditional output channel, including inputs entangled with an arbitrary reference:

```math
\frac12\|\Lambda-\operatorname{Ad}_{C_d}\|_\diamond\le\epsilon.
\tag{1}
```

The resource quantity is its entanglement of formation,

```math
E_F(\rho_{A'B'})
=\inf_{\rho=\sum_\lambda p_\lambda
                  |\eta_\lambda\rangle\langle\eta_\lambda|}
  \sum_\lambda p_\lambda
  S\!\left(\operatorname{Tr}_{A'}
       |\eta_\lambda\rangle\langle\eta_\lambda|\right).
\tag{2}
```

The infimum in (2) can be taken over finite pure-state ensembles in finite dimension. This is the standard convex-roof definition of [Bennett, DiVincenzo, Smolin, and Wootters](https://arxiv.org/abs/quant-ph/9604024). Define

```math
E_{\mathrm{sim}}(n,\epsilon)
=\inf\left\{E_F(\rho):
  \text{an admissible protocol using }\rho\text{ satisfies (1)}
  \right\}.
\tag{3}
```

This is an infimum over individual finite protocols and resources. It is not a regularized many-copy entanglement cost, and no minimum is assumed to exist.

### Theorem 1. Finite-error converse

For every admissible protocol satisfying (1), and every $`r=2^k`$ with $`1\le k\le n`$ such that $`\alpha_r=4r\sqrt\epsilon\le1/2`$,

```math
E_F(\rho)\ge
(1-\alpha_r)\log_2r-h_2(\alpha_r).
\tag{4}
```

Consequently,

```math
E_{\mathrm{sim}}(n,\epsilon)\ge
\max\left(
\{0\}\cup
\left\{
(1-4r\sqrt\epsilon)\log_2r-h_2(4r\sqrt\epsilon):
r=2^k,\ 1\le k\le n,\ 4r\sqrt\epsilon\le\tfrac12
\right\}\right).
\tag{5}
```

The statement includes $`\epsilon=0`$. In that case choosing $`r=d`$ gives $`E_F(\rho)\ge n`$. This exact endpoint is the distinct-eigenphase lower bound of [Gonzales and Chitambar, Theorem 3](https://arxiv.org/html/1810.00994v2), specialized to the phase gradient. Their Fourier-basis extraction argument motivates the extraction step below. The proof here establishes the quantitative finite-error statement.

We first prove (4) with $`r=d`$, then obtain the other values of $`r`$ by a local restriction of Bob's input and output.

## 2. Two lemmas about entropy

The comparison states constructed later can occupy an arbitrarily large workspace. An entropy-continuity estimate proportional to the logarithm of that workspace dimension would not give the desired converse. The following elementary estimate instead uses only a bound on the largest eigenvalue of the comparison state.

### Lemma 2. Entropy near a state with bounded largest eigenvalue

Let $`\rho,\sigma`$ be normalized states on the same finite-dimensional space. Suppose $`\sigma\le I/d`$ for an integer $`d\ge2`$, and put $`t=\frac12\|\rho-\sigma\|_1`$. Then

```math
S(\rho)\ge f_d(t),
\qquad
f_d(t)=(1-t)\log_2d-h_2(t).
\tag{6}
```

**Proof.** Dephase $`\sigma`$ in an eigenbasis of $`\rho`$. The resulting diagonal distributions $`p,q`$ satisfy $`S(\rho)=H(p)`$, $`q_i\le1/d`$, and

```math
t'=\frac12\sum_i|p_i-q_i|\le t.
```

If $`t'<1`$, their common part $`a_i=\min(p_i,q_i)`$ has mass $`c=1-t'`$. The normalized distribution $`u_i=a_i/c`$ has largest entry at most $`1/(dc)`$. Since $`p=cu+(1-c)v`$ for a probability distribution $`v`$, concavity of Shannon entropy gives

```math
H(p)\ge cH(u)\ge c\log_2(dc)
\ge (1-t')\log_2d-h_2(t')=f_d(t').
\tag{7}
```

The last inequality uses $`t'\log_2t'\le0`$. When $`t'=1`$, the desired lower bound is simply nonnegativity of entropy.

It remains to replace $`t'`$ by $`t`$. Differentiating on $`(0,1)`$ gives

```math
f_d'(t)=\log_2\frac{t}{d(1-t)}.
```

Thus $`f_d`$ decreases up to $`d/(d+1)`$. Beyond that point it increases to $`f_d(1)=0`$, so it is nonpositive there. If $`t\le d/(d+1)`$, use $`t'\le t`$ in (7). Otherwise use $`S(\rho)\ge0\ge f_d(t)`$. This proves (6). ∎

### Lemma 3. Conditional entropy with different outcome probabilities

Let

```math
\omega=\bigoplus_\ell p_\ell\rho_\ell,
\qquad
\sigma=\bigoplus_\ell q_\ell\sigma_\ell
```

be normalized classical–quantum states with a finite common label set. All quantum blocks act on a common space of dimension at least $`d`$. Suppose every normalized block with $`q_\ell>0`$ obeys $`\sigma_\ell\le I/d`$. Put $`\delta=\frac12\|\omega-\sigma\|_1`$. If $`2\delta\le\alpha\le1/2`$, then

```math
\sum_\ell p_\ell S(\rho_\ell)
\ge (1-\alpha)\log_2d-h_2(\alpha).
\tag{8}
```

**Proof.** For labels with $`q_\ell=0`$, choose any normalized $`\sigma_\ell\le I/d`$ on the common block space. Labels with $`p_\ell=0`$ contribute nothing. Let $`t_\ell=\frac12\|\rho_\ell-\sigma_\ell\|_1`$. The triangle inequality implies

```math
p_\ell t_\ell
\le\frac12\|p_\ell\rho_\ell-q_\ell\sigma_\ell\|_1
   +\frac12|p_\ell-q_\ell|.
```

Taking the trace of a block cannot increase its trace norm. Summing therefore gives

```math
\bar t:=\sum_\ell p_\ell t_\ell
\le\delta+\frac12\sum_\ell|p_\ell-q_\ell|
\le2\delta\le\alpha.
\tag{9}
```

Lemma 2 applies to every block. The function $`f_d`$ is convex on $`[0,1]`$, since $`-h_2`$ is convex. Jensen's inequality and its monotonic decrease on $`[0,1/2]`$ give

```math
\sum_\ell p_\ell S(\rho_\ell)
\ge\sum_\ell p_\ell f_d(t_\ell)
\ge f_d(\bar t)
\ge f_d(\alpha).
```

No bound on the number of labels or on the block-space dimension appears. ∎

## 3. A purified form of the protocol

Fix an arbitrary finite pure-state ensemble in (2), and abbreviate

```math
\eta_{\lambda,B'}
=\operatorname{Tr}_{A'}|\eta_\lambda\rangle\langle\eta_\lambda|.
```

All bounds below hold for this ensemble without assuming that its label is available to either party.

For each pre-message instrument, retain its local Stinespring environment. Its branches can then be represented by single linear maps

```math
A_a:A A'\longrightarrow K_A,
\qquad B_b:B B'\longrightarrow K_B,
\qquad
\sum_a A_a^\dagger A_a=I_{AA'},\quad
\sum_b B_b^\dagger B_b=I_{BB'}.
\tag{10}
```

If a branch originally had several Kraus operators, the additional index is retained coherently in its local quantum output; it need not be sent as an extra message. Local private coins can be retained in the same way.

The final local CPTP decoders admit isometric dilations. After adding pure local padding, choose common spaces large enough that each decoder dilation extends to a square unitary,

```math
W_{ab}:K_A\longrightarrow A\otimes E_A,
\qquad
V_{ab}:K_B\longrightarrow B\otimes E_B.
\tag{11}
```

Here $`\dim K_A=2\dim E_A`$ and $`\dim K_B=d\dim E_B`$. To justify the padding, first choose an environment large enough for every decoder in the finite family. Embed each original input space into a space of the same dimension as the corresponding enlarged output. Each decoder isometry, defined on the embedded subspace, extends to a unitary by completing orthonormal bases. The maps in (10) include the input embedding. This changes no output channel and adds no entanglement.

A Stinespring isometry for the entire channel is

```math
F|\psi\rangle_{AB}
=\sum_{\lambda,a,b}\sqrt{p_\lambda}
  |\lambda,a,b\rangle_C
  (W_{ab}\otimes V_{ab})(A_a\otimes B_b)
  \bigl(|\psi\rangle_{AB}\otimes|\eta_\lambda\rangle_{A'B'}\bigr).
\tag{12}
```

The computational outputs are $`A B`$; the environment is $`C E_AE_B`$. Tracing it out gives the original protocol channel, including its classical measurement records and mixed resource. The register $`C`$ is a mathematical purification register. Its ensemble component is not an extra shared register supplied to the protocol.

### Lemma 4. A common environment vector

Under (1), there is a normalized $`|\gamma\rangle\in C E_AE_B`$ such that

```math
\|F-C_d\otimes|\gamma\rangle\|_\infty
\le\kappa,
\qquad \kappa=2\sqrt\epsilon.
\tag{13}
```

**Justification.** The fixed-environment Stinespring-continuity theorem for a pair of channels of which one has Kraus rank one states that their dilations can be aligned by an environment unitary to operator-norm distance at most the square root of twice their diamond-norm distance; see [vom Ende, *Progress on the Kretschmann–Schlingemann–Werner Conjecture*](https://arxiv.org/abs/2308.15389). Apply it to $`F`$ and the dilation $`C_d\otimes|0\rangle`$ of the unitary target, in the same environment. The aligning unitary sends $`|0\rangle`$ to some normalized $`|\gamma\rangle`$. Since (1) bounds the **full** diamond norm by $`2\epsilon`$, the resulting bound is $`\sqrt{2(2\epsilon)}=2\sqrt\epsilon`$. ∎

Expand this one common vector as

```math
|\gamma\rangle
=\sum_{\lambda,a,b}|\lambda,a,b\rangle_C
 |\gamma_{\lambda ab}\rangle_{E_AE_B},
\qquad
\gamma^B_{\lambda ab}
=\operatorname{Tr}_{E_A}
  |\gamma_{\lambda ab}\rangle\langle\gamma_{\lambda ab}|.
\tag{14}
```

The branch vectors may be entangled and subnormalized. Their squared norms sum to one, but their weights need not equal the protocol's ensemble or measurement probabilities.

For later use, if two isometries are at operator-norm distance at most $`\kappa`$, the channels obtained from them before any environment is discarded are at full diamond distance at most $`2\kappa`$. Indeed, for an operator $`X`$ on the input and any reference, write the difference as

```math
(F-G)XF^\dagger+GX(F-G)^\dagger
```

and use the trace-norm ideal property and $`\|F\|_\infty=\|G\|_\infty=1`$. This bound survives any common CPTP postprocessing.

## 4. A Bob channel independent of the control input

Apply the following common mathematical postprocessing to the two isometries in (13): dephase $`C`$ in its displayed basis, use its labels to apply $`V_{ab}^\dagger`$ on Bob's output and environment, and trace Alice's output and environment together with the record $`a`$. Retain the labels $`\lambda,b`$ and the space $`K_B`$.

This is a CPTP map used to compare states in the proof. It does not assert that Bob can access the purification register or undo his decoder before the messages arrive.

Fix Alice's input to $`|x\rangle`$, where $`x\in\{0,1\}`$. For the actual dilation (12), the resulting channel on Bob's input is

```math
\mathcal R(X)
=\bigoplus_{\lambda,b}p_\lambda
 B_b\bigl(X\otimes\eta_{\lambda,B'}\bigr)B_b^\dagger.
\tag{15}
```

Crucially, (15) does not depend on $`x`$. Bob's decoder has been undone; Alice's decoder disappears under a partial trace; and summing over $`a`$ uses the first completeness identity in (10). This last step is the no-signalling property of Alice's trace-preserving local operation. It holds separately for each ensemble component and with a reference attached to Bob's input.

For the ideal dilation, the same processing gives $`\mathcal T\circ\operatorname{Ad}_{Z_d^x}`$, where

```math
\mathcal T(X)
=\bigoplus_{\lambda,b}\sum_a
 V_{ab}^\dagger
 \bigl(X\otimes\gamma^B_{\lambda ab}\bigr)V_{ab}.
\tag{16}
```

Both $`\mathcal R`$ and $`\mathcal T`$ are CPTP. For (16), complete positivity is immediate and trace preservation follows from

```math
\sum_{\lambda,a,b}\operatorname{Tr}\gamma^B_{\lambda ab}=1.
```

The isometry bound and common postprocessing now give

```math
\|\mathcal R-\mathcal T\|_\diamond\le2\kappa,
\qquad
\|\mathcal R-\mathcal T\circ\operatorname{Ad}_{Z_d}\|_\diamond
\le2\kappa.
```

Taking their difference yields the approximate invariance

```math
\|\mathcal T-\mathcal T\circ\operatorname{Ad}_{Z_d}\|_\diamond
\le4\kappa.
\tag{17}
```

The same environment vector in the two comparisons is essential. It is supplied by approximation of the full controlled unitary, including superpositions of the control input.

## 5. Cyclic averaging removes coherences

Put $`\mathcal A=\operatorname{Ad}_{Z_d}`$. Its cyclic average is computational-basis dephasing:

```math
\mathcal D_d
=\frac1d\sum_{j=0}^{d-1}\mathcal A^j,
\qquad
\mathcal D_d(X)
=\sum_{s=0}^{d-1}|s\rangle\langle s|X|s\rangle\langle s|.
\tag{18}
```

To verify this, apply the average to $`|s\rangle\langle t|`$ and sum the geometric series $`d^{-1}\sum_j e^{2\pi i j(s-t)/d}`$. It equals one for $`s=t`$ and zero otherwise.

The telescoping identity

```math
\mathcal T-\mathcal T\mathcal A^j
=\sum_{i=0}^{j-1}(\mathcal T-\mathcal T\mathcal A)\mathcal A^i
```

and unitary invariance of the diamond norm imply

```math
\|\mathcal T-\mathcal T\mathcal A^j\|_\diamond\le4j\kappa.
```

Averaging this bound and then comparing to $`\mathcal R`$ gives

```math
\|\mathcal T-\mathcal T\mathcal D_d\|_\diamond
\le2(d-1)\kappa,
\qquad
\|\mathcal R-\mathcal T\mathcal D_d\|_\diamond
\le2d\kappa.
\tag{19}
```

This is where the factor $`d`$ enters the finite-error converse. No bound on an environmental dimension has been introduced.

## 6. A local instrument extracts high conditional entropy

Let $`\{|f_t\rangle\}_{t=0}^{d-1}`$ be the Fourier basis of Bob's input:

```math
|f_t\rangle
=\frac1{\sqrt d}\sum_{s=0}^{d-1}e^{2\pi i ts/d}|s\rangle.
```

Define an instrument acting only on Bob's share $`B'`$ of the preshared resource,

```math
M_{bt}
=\frac1{\sqrt d}\,B_b\bigl(|f_t\rangle_B\otimes I_{B'}\bigr).
\tag{20}
```

It is a valid complete instrument, since

```math
\sum_{b,t}M_{bt}^\dagger M_{bt}
=\frac1d\sum_t
 (\langle f_t|\otimes I)
 \left(\sum_b B_b^\dagger B_b\right)
 (|f_t\rangle\otimes I)
=I_{B'}.
\tag{21}
```

Operationally Bob chooses $`t`$ uniformly, prepares $`|f_t\rangle`$ locally, and runs the original pre-message instrument. The instrument (20) is independent of $`\lambda`$.

Collect its conditional Bob states, including their ensemble weights, into

```math
\omega
=\bigoplus_{\lambda,b,t}
 \frac{p_\lambda}{d}
 B_b\bigl(|f_t\rangle\langle f_t|
          \otimes\eta_{\lambda,B'}\bigr)B_b^\dagger.
\tag{22}
```

Its comparison state is

```math
\sigma
=\bigoplus_{\lambda,b,t}
 \frac1d\sum_a
 V_{ab}^\dagger
 \left(\frac{I_B}{d}\otimes\gamma^B_{\lambda ab}\right)V_{ab}.
\tag{23}
```

Both states are normalized. Because $`\mathcal D_d(|f_t\rangle\langle f_t|)=I_B/d`$, (19) bounds the difference of their blocks for every $`t`$. Therefore

```math
\delta:=\frac12\|\omega-\sigma\|_1\le d\kappa.
\tag{24}
```

Every normalized, nonzero block of $`\sigma`$ has largest eigenvalue at most $`1/d`$. To see this without imposing any size limit on $`E_B`$, use

```math
\gamma^B_{\lambda ab}
\le(\operatorname{Tr}\gamma^B_{\lambda ab})I_{E_B}.
```

Conjugation by the unitary $`V_{ab}`$, followed by summation over $`a`$, shows that the block $`\sigma_{\lambda bt}`$ in (23) satisfies

```math
\sigma_{\lambda bt}
\le\frac{\sum_a\operatorname{Tr}\gamma^B_{\lambda ab}}{d^2}I_{K_B},
\qquad
q_{\lambda bt}:=\operatorname{Tr}\sigma_{\lambda bt}
=\frac1d\sum_a\operatorname{Tr}\gamma^B_{\lambda ab}.
```

Hence

```math
\frac{\sigma_{\lambda bt}}{q_{\lambda bt}}
\le\frac{I_{K_B}}d
\quad\text{whenever }q_{\lambda bt}>0.
\tag{25}
```

Let $`p_{\lambda bt}=\operatorname{Tr}\omega_{\lambda bt}`$. If $`\alpha_d=2d\kappa=4d\sqrt\epsilon\le1/2`$, Lemma 3 applies to (22)–(25) and gives

```math
\sum_{\lambda,b,t}p_{\lambda bt}
 S\left(\frac{\omega_{\lambda bt}}{p_{\lambda bt}}\right)
\ge(1-\alpha_d)\log_2d-h_2(\alpha_d).
\tag{26}
```

Zero-probability summands are omitted. Equation (26) does not presume equality of the label probabilities in $`\omega`$ and $`\sigma`$; that is the purpose of Lemma 3.

## 7. From conditional entropy to entanglement of formation

For a fixed $`\lambda`$, applying (20) to the pure resource $`|\eta_\lambda\rangle`$ gives pure conditional states on $`A'K_B`$. Write their outcome probabilities as $`s_{bt|\lambda}`$. Thus $`p_{\lambda bt}=p_\lambda s_{bt|\lambda}`$.

The average of their Alice marginals equals the original Alice marginal, by (21). Concavity of entropy therefore yields

```math
S(\eta_{\lambda,A'})
\ge\sum_{b,t}s_{bt|\lambda}
 S(\text{conditional state on }A').
```

The conditional global states are pure, so each conditional Alice entropy equals the corresponding Bob entropy. The original resource component is also pure, so its Alice and Bob entropies agree. Consequently,

```math
\sum_\lambda p_\lambda S(\eta_{\lambda,B'})
\ge\sum_{\lambda,b,t}p_{\lambda bt}
 S\left(\frac{\omega_{\lambda bt}}{p_{\lambda bt}}\right)
\ge(1-\alpha_d)\log_2d-h_2(\alpha_d).
\tag{27}
```

The ensemble chosen before (10) was arbitrary. Taking the infimum over ensembles in (2) proves (4) for $`r=d`$.

The ensemble label served only to organize a purification and evaluate the convex roof. Neither the physical protocol nor the extraction instrument is given that label. In particular, the proof does not infer that every channel obtained from a pure component of the mixed resource individually approximates $`C_d`$.

## 8. Restricting to a smaller phase gradient

Let $`r=2^k`$ with $`k\le n`$. Define Bob's local isometric encoder by

```math
J_r|j\rangle=|j d/r\rangle,
\qquad j=0,\ldots,r-1.
```

Then $`Z_dJ_r=J_rZ_r`$, and therefore

```math
C_d(I_A\otimes J_r)=(I_A\otimes J_r)C_r.
\tag{28}
```

To account for leakage in an approximate protocol, use the CPTP decoder

```math
\mathcal Q_r(Y)
=J_r^\dagger YJ_r
 +\operatorname{Tr}[(I_B-J_rJ_r^\dagger)Y]
   |0\rangle\langle0|.
\tag{29}
```

Compose the original protocol with $`J_r`$ before Bob's instrument and $`\mathcal Q_r`$ after his decoder. These are local changes and use exactly the same preshared resource and communication pattern. By (28), the ideal composed channel is $`\operatorname{Ad}_{C_r}`$. Diamond-norm contraction under CPTP pre- and postprocessing preserves (1), with $`d`$ replaced by $`r`$.

Applying (27) to this smaller target proves (4) for every stated $`r`$. Since the bound holds for every admissible resource, taking the infimum over protocols yields (5). ∎

## 9. What the proof uses

The simultaneous timing makes the recovered pre-message Bob channel independent of Alice's control input. Approximation to a unitary gives a common environment vector, turning that independence into approximate invariance under $`Z_d`$. Cyclic averaging then compares the recovered channel to one that has lost all input coherences. Fourier test inputs force the corresponding conditional resource outputs to have high entropy. The argument bounds that entropy without any restriction on hidden workspace or message dimensions.

The assumptions about communication and correctness matter. Equation (5) concerns one simultaneous exchange of classical messages and the unconditional channel in half diamond distance. It is not a lower bound on a postselected successful branch, nor an entanglement-only lower bound in a model with uncharged quantum messages. The [model note](model.md) fixes those resource conventions, and the [frontier note](frontier.md) identifies the quantitative consequences of (5).
