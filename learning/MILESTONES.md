# Thirty milestones for the remote-gate entanglement frontier

[Repository overview](../README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [Model](../science/model.md) · [Finite bounds](../science/frontier.md)

This map organizes the scientific understanding of one question: how much preshared entanglement is needed to apply a controlled phase-gradient gate when Alice and Bob have one simultaneous exchange of classical messages? The targets describe the project itself and apply independently of any reader's previous study.

The **13 background milestones** assemble registers, states, channels, accuracy, entropy, and causality into the complete operational model. The **17 narrative milestones** begin with individual protocol branches, develop the construction and the converse, and end with their joint physical interpretation. This allocation gives the mixed-resource proof and the implementation account their own conceptual steps. It does not attempt to cover every technical lemma or neighboring research area.

The educational anchor is John Watrous, [*The Theory of Quantum Information*](https://cs.uwaterloo.ca/~watrous/TQI/), using the [official 2018 manuscript](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf). Section numbers below refer to that manuscript. The [bridge](WATROUS_BRIDGE.md#conventions) translates its notation into the repository's conventions. Watrous supplies the foundations; the project pages supply the particular protocol and converse. Research-level ingredients and attribution remain linked separately, especially the fixed-environment continuity theorem used at M09 and M22.

Throughout the map, $`d=2^n`$ is Bob's target dimension, $`r=2^k\le d`$ is a smaller encoded target dimension, and $`R`$ is the Schmidt rank of the tapered resource. Error means **half diamond distance**. The cost $`E_{\mathrm{sim}}(n,\epsilon)`$ is the infimum of entanglement of formation for one implementation in the [stated model](../science/model.md), not a regularized many-copy rate.

## Phase I: background and preliminaries

<a id="m01"></a>

### M01 — Bipartite registers and tensor products

**Central question.** What mathematical structure records which degrees of freedom Alice and Bob can act on locally?

**Understanding target.** A register has a finite-dimensional complex state space, and joint registers use a tensor product. The factors $`A,B,A',B'`$ distinguish computational inputs from preshared resource systems; an untouched reference is another factor. An operator local to Alice acts as the identity on Bob and the reference. This distinction concerns ownership, not whether the joint state factors into independent states.

**Dependencies and story role.** This is the starting point. It establishes the local objects from which the state, channel, and communication descriptions will be built.

**Conceptual connection.** Entanglement is a property relative to a tensor-factor partition. A register count, a tensor-product decomposition, and a restriction on allowed operations therefore answer different questions even when they describe the same physical device.

**Source pointers.** Watrous §§1.1.1–1.1.2 and 2.1.1–2.1.2; [model: target family](../science/model.md#target-family); [bridge: conventions](WATROUS_BRIDGE.md#conventions).

<a id="m02"></a>

### M02 — Reduced states and purification

**Central question.** How can local mixedness arise from a globally pure description, and what information is lost by discarding a system?

**Understanding target.** The partial trace produces the state relevant to local observations. Every finite mixed state has a purification, while a purification is not a declaration that its extra system is physically available to a party. The Schmidt decomposition connects the two reductions of a bipartite pure state: their nonzero eigenvalues coincide.

**Dependencies and story role.** Requires M01. It supplies the state-level language needed both to measure pure-state entanglement and to retain mathematical environments without adding an operational resource.

**Conceptual connection.** A mixed resource can be represented through a larger pure state without giving Alice or Bob access to the purifying register. The distinction later prevents a mathematical ensemble label from becoming an unauthorized classical message or shared control.

**Source pointers.** Watrous §§1.1.3 and 2.1.3; [converse §3](../science/converse.md#3-a-purified-form-of-the-protocol); [bridge: hidden ensemble](WATROUS_BRIDGE.md#hidden-ensemble).

<a id="m03"></a>

### M03 — Pure-state entanglement entropy

**Central question.** Which feature of a bipartite pure state measures the entanglement being counted?

**Understanding target.** For Schmidt coefficients $`c_j`$, the entanglement is

```math
S(\mathrm{Tr}_{A'}|\eta\rangle\langle\eta|)
=H(|c_0|^2,|c_1|^2,\ldots).
```

The two reduced entropies agree. A Bell pair has one bit of entanglement, and a maximally entangled rank-$`R`$ state has $`\log_2R`$ bits. Schmidt rank specifies how many coefficients are nonzero; entropy also depends on their distribution.

**Dependencies and story role.** Requires M01–M02. It introduces the resource quantity for pure states before mixed resources or protocol optimization enter.

**Conceptual connection.** The tapered protocol deliberately uses a nonuniform Schmidt distribution. Its rank, entanglement entropy, and integer Bell-pair supply can therefore differ even though they describe the same resource state.

**Source pointers.** Watrous §§5.1.1, 5.2.1, and 6.2.1, together with the Schmidt decomposition in §1.1.3; [resource accounting §1](../science/resource_accounting.md#1-entanglement-entropy-and-bell-pair-supply).

<a id="m04"></a>

### M04 — Mixed resources and the convex roof

**Central question.** How is entanglement assigned to a mixed state whose pure-state decomposition is not unique?

**Understanding target.** Entanglement of formation is the infimum of average pure-state entanglement over all pure ensembles representing the same density operator:

```math
E_F(\rho)=\inf_{\rho=\sum_\lambda p_\lambda|\eta_\lambda\rangle\langle\eta_\lambda|}
\sum_\lambda p_\lambda S(\eta_{\lambda,B'}).
```

An ensemble used in this definition need not be a preparation record accessible to either party. A lower bound that holds for every ensemble can pass through this infimum. Approximate correctness for the mixed resource does not imply approximate correctness for each ensemble component.

**Dependencies and story role.** Requires M02–M03. It identifies the full resource class before operational representations are introduced.

**Conceptual connection.** A convex-roof measure is neither the entropy of a mixed marginal nor an automatic formula for exact one-copy Bell-pair preparation. These distinctions are essential to the scope of the converse.

**Source pointers.** Watrous Exercise 6.3, Eq. (6.437), contains the convex-roof definition; §6.2.2 provides context on asymptotic entanglement cost. See [model: entanglement cost](../science/model.md#entanglement-cost) and the Bennett–DiVincenzo–Smolin–Wootters citation in [related work](../references/RELATED_WORK.md).

<a id="m05"></a>

### M05 — Channels and completely positive maps

**Central question.** What description of a quantum operation remains valid when its input is entangled with an external system?

**Understanding target.** A quantum channel is a completely positive trace-preserving map. Kraus representations, Choi representations, and compositions describe the same input–output operation in different forms. Trace preservation is expressed by $`\sum_jK_j^\dagger K_j=I`$ in a Kraus representation. Complete positivity preserves valid states when an identity operation is attached to any reference.

**Dependencies and story role.** Requires M01–M02. It extends the description from states to transformations and makes arbitrary local processing precise.

**Conceptual connection.** The target gate is a unitary channel, while an implemented protocol can involve measurements, discarded ancillas, classical randomization, and general final corrections. All are compared at the level of their resulting channels.

**Source pointers.** Watrous §§2.2.1–2.2.2; [model: one simultaneous classical exchange](../science/model.md#one-simultaneous-classical-exchange); [protocols: corrected branches](../science/protocols.md#corrected-branch-operators).

<a id="m06"></a>

### M06 — Instruments, classical records, and retained environments

**Central question.** How can a local operation produce a classical message while preserving quantum information for later use?

**Understanding target.** An instrument is a collection of completely positive outcome maps whose sum is trace preserving. A classical outcome can be stored in an orthogonal flag, and each outcome can retain a quantum output. Refining a branch by keeping its environment permits a single Kraus operator into a larger output space without restricting the original instrument. Forgetting the record gives a channel; conditioning on an outcome gives a subnormalized branch until its probability is divided out.

**Dependencies and story role.** Requires M02 and M05. It supplies the local message-generating operations used by both the constructions and the arbitrary-protocol converse.

**Conceptual connection.** Measurement does not imply that every quantum workspace is discarded. The converse must allow retained memories and outcome-dependent later operations, while distinguishing outcome probabilities from normalized conditional states.

**Source pointers.** Watrous §2.3.2, particularly Eqs. (2.258)–(2.262); [converse §3](../science/converse.md#3-a-purified-form-of-the-protocol); [bridge: hidden ensemble](WATROUS_BRIDGE.md#hidden-ensemble).

<a id="m07"></a>

### M07 — Stinespring dilation and unitary padding

**Central question.** Why can a proof retain environments and use reversible final decoders without assuming that the actual protocol is reversible?

**Understanding target.** A channel can be written as an isometry followed by a partial trace. Finite isometries can be extended to unitaries after adding local pure ancillas and completing orthonormal bases. In this project, padding puts each party's outcome-dependent final decoder on a common finite workspace. Tracing the added environments returns the original channel, and local pure padding adds no preshared entanglement.

**Dependencies and story role.** Requires M01–M02 and M05–M06. It gives a convenient common representation of otherwise unrestricted local operations.

**Conceptual connection.** The proof later undoes a padded decoder as a mathematical comparison. The ability to write this inverse does not grant either party earlier access to the other party's outcome.

**Source pointers.** Watrous §2.2.2 and the linear-algebra foundations of §§1.1.1–1.1.3; [converse §3](../science/converse.md#3-a-purified-form-of-the-protocol); [bridge: unitary continuity](WATROUS_BRIDGE.md#unitary-continuity).

<a id="m08"></a>

### M08 — Trace distance, diamond distance, and the half convention

**Central question.** Which error criterion controls a gate on every unknown input, including inputs entangled with a reference?

**Understanding target.** State trace distance is $`\tfrac12\|\rho-\sigma\|_1`$. Channel error here is $`\tfrac12\|\Lambda-\mathcal U\|_\diamond`$, where the diamond norm stabilizes the trace norm by allowing a reference. Common CPTP pre- and postprocessing cannot increase this distance. An operator-norm comparison of two unitaries or isometries supplies a channel-distance upper bound; it is not the definition of the diamond norm. A single input witness supplies a lower bound unless a matching channel upper bound is also established.

**Dependencies and story role.** Requires M02 and M05–M07. It fixes the accuracy convention before continuity estimates or operational guarantees are used.

**Conceptual connection.** Correct action on the control basis alone does not preserve the relative phase of a control superposition. The reference-sensitive channel criterion is what makes the common-environment argument and the exact dephasing error meaningful.

**Source pointers.** Watrous §§1.1.3, 3.1.1, and 3.3.1–3.3.3; Definition 3.43 uses the completely bounded trace norm denoted here by $`\|\cdot\|_\diamond`$. See [model: accuracy](../science/model.md#accuracy-on-unknown-inputs) and [bridge: conventions](WATROUS_BRIDGE.md#conventions).

<a id="m09"></a>

### M09 — A unitary target and one common environment

**Central question.** What does small channel error imply about the environment of an entire implemented protocol?

**Understanding target.** If a fixed dilation $`F`$ implements a channel within half diamond error $`\epsilon`$ of a unitary channel $`\mathrm{Ad}_U`$, there is one normalized environment vector $`|\gamma\rangle`$ satisfying

```math
\|F-U\otimes|\gamma\rangle\|_\infty\le2\sqrt\epsilon.
```

The same vector works coherently for all inputs. It need not factor between the parties or reproduce the actual branch probabilities. The environment alignment is a theorem about representations, not an allowed online operation.

**Dependencies and story role.** Requires M07–M08. It connects worst-case channel accuracy to the single enlarged description that the robust converse will analyze.

**Conceptual connection.** Separate environment choices for separate control values would not provide the comparison needed by no-signalling. A unitary target has Kraus rank one, which is the hypothesis enabling the particular fixed-environment theorem used here.

**Source pointers.** Watrous §§2.2.2, 3.2.2, and 3.3 supply the dilation and distance foundations. The displayed quantitative statement is the additional research theorem of [vom Ende, Theorem 1, Eq. (13)](https://arxiv.org/html/2308.15389v3), not a claim that the anchor proves it. See [converse Lemma 4](../science/converse.md#lemma-4-a-common-environment-vector), [related work](../references/RELATED_WORK.md#continuity-input-ksw-and-vom-ende), and [bridge: unitary continuity](WATROUS_BRIDGE.md#unitary-continuity).

<a id="m10"></a>

### M10 — No-signalling and the causal order of messages

**Central question.** What can change in Bob's laboratory before a message from Alice has arrived?

**Understanding target.** A trace-preserving local operation on Alice, averaged over its outcomes, leaves Bob's reduced state unchanged. This remains true with a reference and with preshared entanglement. Simultaneously sent messages may each depend on local inputs and local outcomes, but neither may depend on the received remote message. Subsequent local processing may use both outcomes. Two sequential directed messages permit a different causal dependence.

**Dependencies and story role.** Requires M01–M02 and M05–M07. It turns the register ownership of M01 into a restriction on complete protocols.

**Conceptual connection.** The entanglement question arises because a feedback step is unavailable. No-signalling will force two mathematically recovered versions of Bob's channel to agree before that feedback could occur.

**Source pointers.** Watrous §§2.2.1–2.2.2 and 6.1.2 provide the local-channel and LOCC framework; the simultaneous-message restriction is defined in the [model](../science/model.md#one-simultaneous-classical-exchange). See [converse §4](../science/converse.md#4-a-bob-channel-independent-of-the-control-input) and [bridge: timing and resources](WATROUS_BRIDGE.md#timing-and-resources).

<a id="m11"></a>

### M11 — Fourier bases and cyclic dephasing

**Central question.** Why does averaging a phase gradient remove coherences, and why are Fourier inputs useful afterward?

**Understanding target.** For $`Z_D=\sum_s e^{2\pi i s/D}|s\rangle\langle s|`$, the finite geometric sum gives

```math
\frac1D\sum_{j=0}^{D-1}Z_D^jXZ_D^{-j}
=\sum_s|s\rangle\langle s|X|s\rangle\langle s|.
```

A Fourier-basis vector has equal computational-basis probabilities, so this dephasing sends its density operator to $`I/D`$. Fourier measurement also turns a resource index into a known phase that can be corrected classically.

**Dependencies and story role.** Requires M01, M05, and M08. It supplies one algebraic mechanism used in both directions of the argument: correction in the construction and entropy extraction in the converse.

**Conceptual connection.** Cyclic phase action, basis coherence, and a maximally mixed comparison state are linked by the same finite Fourier identity.

**Source pointers.** Watrous §§4.1.1–4.1.2 provide context on unitary mixtures and Weyl operators. The exact identity used here is derived in [converse §5](../science/converse.md#5-cyclic-averaging-removes-coherences); Fourier conventions for the construction appear in [protocols §1](../science/protocols.md#1-a-noncyclic-shift-and-a-tapered-resource).

<a id="m12"></a>

### M12 — Entropy concavity, spectral flatness, and classical flags

**Central question.** How can conditional entropy be bounded without bounding the size of a quantum workspace?

**Understanding target.** Entropy is concave, the entropy of a classical–quantum state separates into its classical entropy and the average of its conditional quantum entropies, and a normalized state $`\sigma\le I/r`$ has entropy at least $`\log_2r`$. The last statement uses a bound on the largest eigenvalue, even if the state occupies more than $`r`$ dimensions. Classical outcome probabilities and normalized conditional states must remain separate when two flagged states are compared.

**Dependencies and story role.** Requires M03–M04, M06, and M08. It collects the entropy tools needed to make a lower bound uniform over arbitrarily large finite memories.

**Conceptual connection.** Local measurements can redistribute pure-state entanglement among outcomes. Concavity bounds its average, while a flat comparison spectrum gives a lower target for that same average. The unequal-probability continuity step joining them is supplied later at M25.

**Source pointers.** Watrous §§5.1.1–5.1.2 and 5.2.1–5.2.3; [converse Lemmas 2–3](../science/converse.md#2-two-lemmas-about-entropy); [bridge: entropy without workspace size](WATROUS_BRIDGE.md#entropy-without-workspace).

<a id="m13"></a>

### M13 — The complete resource and accuracy model

**Central question.** Which protocols does the resource infimum include, and which physical choices remain separately charged?

**Understanding target.** An admissible implementation uses an arbitrary finite mixed resource, local instruments with retained quantum memories, one simultaneous exchange of classical outcomes, and arbitrary final local CPTP maps. Input and output locations are fixed. Accuracy is half diamond distance on unknown inputs, and $`E_{\mathrm{sim}}`$ takes an infimum over entanglement of formation. Every individual protocol is finite, but the model imposes no common bound on resource dimension, workspace size, or message alphabet across protocols. Offline preparation precedes input arrival; local gates, preparation effort, and message lengths are accounted for separately.

**Dependencies and story role.** Integrates M01–M12. It closes the background phase by assembling local mathematical objects into the global operational question.

**Conceptual connection.** A construction gives an upper bound by exhibiting one admissible protocol. A converse must cover this entire class, including mixed resources and general decoders. Quantum messages or additional online feedback would define a different optimization problem.

**Source pointers.** [Model](../science/model.md); [resource accounting](../science/resource_accounting.md); Watrous §6.1.2 for the broader LOCC language; [bridge: timing and resources](WATROUS_BRIDGE.md#timing-and-resources).

## Phase II: narrative and contribution

<a id="m14"></a>

### M14 — The phase gradient and its encoded subfamilies

**Central question.** What structure makes the chosen remote gate both explicitly implementable and suitable for a quantitative lower bound?

**Understanding target.** The target is

```math
C_d=|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes Z_d,
\qquad d=2^n.
```

Its target phase is a product of known one-qubit rotations. For every $`r=2^k\le d`$, the local encoding $`J_r|j\rangle=|jd/r\rangle`$ obeys $`Z_dJ_r=J_rZ_r`$. The family therefore contains smaller cyclic phase gradients and, in particular, a controlled-$`Z`$ restriction. Its adjacent eigenphases become closer as $`d`$ grows even though they remain distinct.

**Dependencies and story role.** Requires M01, M08, M11, and M13. It starts the narrative with the target's local algebra and the subspaces that will later tune the lower bound to the error tolerance.

**Conceptual connection.** Algebraic exactness and finite-accuracy resolution need different resource statements. The encoded subfamilies make that distinction quantitative.

**Source pointers.** [Model: target family](../science/model.md#target-family); [converse §8](../science/converse.md#8-restricting-to-a-smaller-phase-gradient); [resource accounting §6](../science/resource_accounting.md#6-the-phase-gradient-family-has-explicit-short-circuits).

<a id="m15"></a>

### M15 — Exact cyclic and interactive baselines

**Central question.** What is already achievable exactly, and what changes when the messages can be causally ordered?

**Understanding target.** A finite-order controlled unitary has a cyclic-group protocol with a maximally entangled resource. For $`Z_d^d=I`$, it uses $`n`$ ebits and one simultaneous exchange. A standard remote-control protocol instead uses one Bell pair and two sequential directed messages. The controlled-$`Z`$ restriction witnesses the necessity of one ebit for exact interactive implementation. The known exact LOBC lower bound matches the cyclic upper bound, giving $`E_{\mathrm{sim}}(n,0)=n`$.

**Dependencies and story role.** Requires M03, M06, M10–M11, and M13–M14. It establishes the exact reference points before approximation changes the cost.

**Conceptual connection.** The interactive protocol's second operation and message use information received in the first message. Sending both correction bits at once would remove that causal mechanism.

**Source pointers.** [Protocols §§2–3](../science/protocols.md#2-the-exact-cyclic-protocol); [frontier Proposition 4](../science/frontier.md#4-exact-implementation-and-the-interactive-comparison). Attribution belongs to Yu–Griffiths–Cohen and Yu for the cyclic protocols, Eisert and collaborators for the interactive method, and Gonzales–Chitambar for the exact lower bound; see [related work](../references/RELATED_WORK.md). Watrous §§6.1.2 and 6.3.1 supply LOCC and teleportation context.

<a id="m16"></a>

### M16 — Physical branches of the noncyclic-shift protocol

**Central question.** How do local operations and one simultaneous exchange implement a controlled unitary without requiring it to have finite order?

**Understanding target.** For real nonnegative coefficients with $`\sum_kc_k^2=1`$, share $`\sum_{k=0}^{R-1}c_k|k,k\rangle`$. Alice shifts her label by minus the control value into a padded register and measures $`j`$. Independently, Bob applies controlled powers $`V^k`$ and Fourier-measures his label as $`q`$. After exchanging the outcomes, their corrections produce

```math
K_{j,q}=\frac{e^{-2\pi iqj/R}}{\sqrt R}
\bigl(\mathrm{diag}(c_j,c_{j+1})\otimes I\bigr)C(V),
```

with coefficients outside the supported range set to zero. The boundary outcomes are retained and are part of Kraus completeness. The known phase convention of $`V`$ fixes the controlled gate.

**Dependencies and story role.** Requires M06–M07, M10–M11, and M13–M15. It builds the approximate construction from physically admissible local branches.

**Conceptual connection.** The desired target survives every correction; the branch amplitudes retain information about the control. Their neighboring-index overlap will determine the residual noise.

**Source pointers.** [Protocols §1, local operations and corrected branches](../science/protocols.md#1-a-noncyclic-shift-and-a-tapered-resource); [bridge: worked example](WATROUS_BRIDGE.md#worked-example).

<a id="m17"></a>

### M17 — Exact dephasing and its diamond error

**Central question.** What error remains after all branches and corrections are included?

**Understanding target.** The implemented channel is exactly the target followed by dephasing of Alice's control. Its coherence multiplier and half diamond error are

```math
f(c)=\sum_{k=0}^{R-2}c_kc_{k+1},
\qquad
\epsilon(c)=\frac{1-f(c)}2.
```

The error equality combines a Pauli-mixture upper bound with the distinguishable outputs of the identity and Pauli-$`Z`$ channels on $`|+\rangle`$. It holds with arbitrary references and is independent of Bob's dimension or the spectrum of the known $`V`$.

**Dependencies and story role.** Requires M05, M08, and M16. It converts the local branch calculation into the construction's complete channel guarantee.

**Conceptual connection.** The resource's imperfect overlap with its one-step translation appears as lost control coherence. A state-fidelity calculation alone would not establish this channel-level guarantee.

**Source pointers.** [Protocols: exact residual channel](../science/protocols.md#exact-residual-channel-and-diamond-error); [frontier Eqs. (5)–(7)](../science/frontier.md#1-explicit-finite-upper-and-lower-bounds); [bridge: worked example](WATROUS_BRIDGE.md#worked-example).

<a id="m18"></a>

### M18 — Sine optimization, entropy, and rank

**Central question.** Which amplitude profile minimizes this protocol's error at fixed support size, and what does that optimization establish?

**Understanding target.** The overlap $`f(c)`$ is a Rayleigh quotient for the path matrix with neighboring entries $`1/2`$. Its largest-eigenvalue vector is

```math
c_k=\sqrt{\frac2{R+1}}\sin\frac{(k+1)\pi}{R+1},
\qquad
\epsilon_R=\sin^2\frac{\pi}{2(R+1)}.
```

The resource has entropy $`H(c_k^2)\le\log_2R`$, while the error is $`O(R^{-2})`$. This proves optimality of the profile at fixed support within the displayed shift protocol. It does not minimize entanglement over all LOBC protocols or identify entropy with Schmidt rank.

**Dependencies and story role.** Requires M03, M11, and M16–M17. It turns a channel identity into an explicit accuracy–resource construction.

**Conceptual connection.** The smoother boundary profile improves the translation overlap. The same sine mathematics has established phase-estimation and programming precedents, although those tasks count different resources.

**Source pointers.** Watrous §1.1.3 for spectral decomposition; [protocols: optimal profile](../science/protocols.md#optimal-profile-within-this-protocol); [resource accounting §1](../science/resource_accounting.md#1-entanglement-entropy-and-bell-pair-supply); Berry–Wiseman and Yang–Renner–Chiribella in [related work](../references/RELATED_WORK.md#sine-profiles-finite-references-and-programming).

<a id="m19"></a>

### M19 — Preparing the shared resource before the input arrives

**Central question.** How is the sine resource supplied with explicit finite operations and a stated Bell-pair cost?

**Understanding target.** For $`R=2^w`$, local controlled rotations prepare the sine amplitudes on a success flag with probability $`(R+1)/(2R)>1/2`$. This preparation occurs before the Bell-pair conversion and before the unknown input arrives. A local modular subtraction, measurement, offline message, and shared label correction convert $`w`$ Bell pairs into the desired resource. A finite attempt cap with an explicit fallback gives a trace-preserving implementation; its preparation and failure errors are charged at M28.

**Dependencies and story role.** Requires M03, M05–M06, M10, and M18. It makes the abstract resource state operational without adding online feedback.

**Conceptual connection.** Offline heralding is compatible with a deterministic online channel when failure is included in the finite preparation procedure. The supplied Bell-pair count and the ideal state's entanglement entropy are related but distinct costs.

**Source pointers.** [Resource accounting §§1–3](../science/resource_accounting.md#1-entanglement-entropy-and-bell-pair-supply); Watrous §6.2.1 for pure-state entanglement transformations; [bridge: timing and resources](WATROUS_BRIDGE.md#timing-and-resources).

<a id="m20"></a>

### M20 — Unbiased randomized rounding and upper-bound attribution

**Central question.** Can the leading precision cost also follow from the established cyclic protocol?

**Understanding target.** A known spectrum can be rounded randomly to adjacent points of a common order-$`D`$ phase grid so that every phase error has zero mean. A finite shared threshold selects among finitely many rounded gates, each implemented exactly by the cyclic protocol. If the grid spacing is $`h=2\pi/D`$, cancellation of the first channel-expansion term gives half diamond error at most $`h^2`$ for the averaged channel. Individual rounded gates need only have first-order error. Hence this route also gives $`\tfrac12\log_2(1/\epsilon)+O(1)`$ entanglement.

**Dependencies and story role.** Requires M05, M08, M11, M13–M15, and M18. It places the explicit sine construction beside a second upper mechanism before the general lower bound is developed.

**Conceptual connection.** Shared randomness is allowed by the model, and its record is not an additional required target output. The leading upper coefficient alone therefore does not establish the project's resource frontier; a matching converse is essential.

**Source pointers.** [Randomized rounding](../science/randomized_rounding.md), including its finite arithmetic implementation for the phase gradient; [related work: fast protocols](../references/RELATED_WORK.md#fast-protocols-and-the-upper-bound-comparison). The rounding derivation is supplied locally as an extension of the inherited cyclic method, not attributed to an unverified prior theorem.

<a id="m21"></a>

### M21 — Normal form for an arbitrary mixed-resource protocol

**Central question.** How can one analyze every admissible protocol without revealing a decomposition of its mixed resource?

**Understanding target.** Choose an arbitrary pure ensemble for the resource, retain local instrument environments, and pad final decoders to unitaries $`W_{ab}`$ and $`V_{ab}`$. A single dilation $`F`$ records $`\lambda,a,b`$ in a formal environment register $`C`$ while reproducing the actual mixed-resource channel after tracing that environment. The ensemble label $`\lambda`$ is mathematical: the physical instruments do not receive it. The allowed workspace and outcome sets remain arbitrary finite sizes.

**Dependencies and story role.** Requires M04, M06–M07, M09, and M13. It begins the converse with the whole protocol class rather than a chosen construction.

**Conceptual connection.** Purification, convex roofs, and causality must be compatible in the same representation. Retaining a hidden flag permits ensemble bookkeeping without assuming that each pure component separately implements a good channel.

**Source pointers.** [Converse §3, Eqs. (10)–(12)](../science/converse.md#3-a-purified-form-of-the-protocol); [bridge: hidden ensemble](WATROUS_BRIDGE.md#hidden-ensemble); Watrous §§2.1.3, 2.2.2, and 2.3.2 for the component representations.

<a id="m22"></a>

### M22 — Common-environment recovery and no-signalling

**Central question.** How does accuracy of the complete controlled gate constrain Bob's operation before the exchange?

**Understanding target.** Apply M09 to the complete dilation, with $`\kappa=2\sqrt\epsilon`$. In a common mathematical postprocessing, dephase the formal record, undo Bob's padded decoder, and trace Alice and her outcome. For the actual protocol the recovered channel $`\mathcal R`$ is independent of Alice's control basis value. For the ideal comparison it is $`\mathcal T`$ or $`\mathcal T\circ\mathrm{Ad}_{Z_d}`$, using the same environment vector. Each is within full diamond distance $`2\kappa`$ of $`\mathcal R`$.

**Dependencies and story role.** Requires M08–M10 and M21. It turns global accuracy into the approximate symmetry on which the rest of the converse depends.

**Conceptual connection.** The proof's record-controlled recovery is not an online capability assigned to Bob. Its value is to expose no-signalling in the actual channel while retaining one coherent ideal comparison for both control inputs.

**Source pointers.** [Converse Lemma 4 and §4](../science/converse.md#lemma-4-a-common-environment-vector); [bridge: unitary continuity](WATROUS_BRIDGE.md#unitary-continuity) and [hidden ensemble](WATROUS_BRIDGE.md#hidden-ensemble); the vom Ende theorem identified at M09.

<a id="m23"></a>

### M23 — Approximate invariance and the cyclic twirl

**Central question.** How does a constraint from two control values become a comparison with a fully dephased input?

**Understanding target.** The two comparisons at M22 imply

```math
\|\mathcal T-\mathcal T\circ\mathrm{Ad}_{Z_d}\|_\diamond
\le4\kappa.
```

Telescoping bounds the error after each power of $`Z_d`$. Averaging all powers then gives

```math
\|\mathcal R-\mathcal T\mathcal D_d\|_\diamond\le2d\kappa,
```

where $`\mathcal D_d`$ is computational-basis dephasing. The factor $`d`$ comes from accumulated cyclic comparisons, not from a bound on memory size.

**Dependencies and story role.** Requires M08, M11, M14, and M22. It converts the causal constraint into a spectral statement that will force entropy.

**Conceptual connection.** The same cyclic group that gives an exact upper protocol also supplies the averaging operation in the lower bound. Its accumulated error explains why smaller encoded subfamilies become useful at finite accuracy.

**Source pointers.** [Converse §5, Eqs. (17)–(19)](../science/converse.md#5-cyclic-averaging-removes-coherences); [bridge: reading route](WATROUS_BRIDGE.md#reading-route).

<a id="m24"></a>

### M24 — Fourier inputs as a local extraction instrument

**Central question.** How can the comparison with dephasing reveal entanglement already present in the resource?

**Understanding target.** Bob can choose a Fourier input locally and run his original pre-message instrument. The resulting resource-only operators

```math
M_{bt}=d^{-1/2}B_b(|f_t\rangle\otimes I_{B'})
```

form a complete local instrument and do not depend on the hidden ensemble label. Because dephasing sends each Fourier input to $`I/d`$, its ideal comparison has normalized conditional Bob states bounded above by $`I/d`$. Actual and comparison classical–quantum states are within trace distance $`d\kappa`$. Their outcome probabilities need not match.

**Dependencies and story role.** Requires M03, M06, M11–M12, and M21–M23. It translates an abstract channel comparison into conditional resource states whose entropies can be bounded.

**Conceptual connection.** A purely local operation cannot create average pure-state entanglement. If its conditional outputs must have large entropy, that entropy must have been supported by the initial resource.

**Source pointers.** [Converse §6, Eqs. (20)–(25)](../science/converse.md#6-a-local-instrument-extracts-high-conditional-entropy); Gonzales–Chitambar's exact Fourier-extraction antecedent in [related work](../references/RELATED_WORK.md#exact-controlled-gate-lower-bound-gonzales-and-chitambar).

<a id="m25"></a>

### M25 — Conditional entropy without a workspace-size penalty

**Central question.** How much entropy survives approximation when the actual and comparison branch probabilities differ?

**Understanding target.** If $`\sigma\le I/d`$ and $`t=\tfrac12\|\rho-\sigma\|_1`$, the project proves

```math
S(\rho)\ge(1-t)\log_2d-h_2(t).
```

For flagged states at trace distance $`\delta`$, the actual-probability-weighted average distance between normalized blocks is at most $`2\delta`$, including blocks with zero comparison probability. Convexity of the displayed lower function and its monotonicity on the relevant interval give the conditional bound with $`\alpha_d=2d\kappa=4d\sqrt\epsilon\le1/2`$.

**Dependencies and story role.** Requires M08, M12, and M24. It supplies the robust step between approximately flat comparison outputs and an actual entanglement lower bound.

**Conceptual connection.** The entropy estimate uses a largest-eigenvalue constraint and common probability mass. Its penalty depends on the target dimension, not the unbounded allowed workspace or the number of outcomes. Ignoring probability mismatch would lose the justification for normalized conditional states.

**Source pointers.** [Converse Lemmas 2–3 and Eq. (26)](../science/converse.md#2-two-lemmas-about-entropy); [bridge: entropy without workspace size](WATROUS_BRIDGE.md#entropy-without-workspace). Watrous's entropy foundations at M12 support the locally supplied derivation.

<a id="m26"></a>

### M26 — The convex-roof conclusion and restriction with leakage

**Central question.** How do conditional pure-state bounds become a theorem for arbitrary mixed resources and every smaller encoded target?

**Understanding target.** For every resource ensemble, Bob's local extraction instrument leaves the average Alice marginal unchanged. Entropy concavity and equality of pure-state marginal entropies bound the extracted average by the original ensemble's entanglement. Taking the infimum over ensembles gives the $`E_F`$ lower bound. To use a smaller $`r`$, Bob encodes with $`J_r`$ and applies a trace-preserving decoder that maps any output outside the encoded subspace to a fixed state. This includes leakage, preserves the resource and message timing, and cannot increase diamond error.

**Dependencies and story role.** Requires M04, M05, M08, M12, M14, and M21–M25. It completes the general converse and makes the accuracy-dependent choice of target scale legitimate.

**Conceptual connection.** The hidden-label argument handles convexity of the resource; the complete decoder handles approximation of the target. Neither can be replaced by assuming ideal behavior separately in each ensemble component or by postselecting the encoded subspace.

**Source pointers.** [Converse §§7–8](../science/converse.md#7-from-conditional-entropy-to-entanglement-of-formation); [bridge: hidden ensemble](WATROUS_BRIDGE.md#hidden-ensemble); Watrous §§5.2.2 and 6.2.1 for the entropy and pure-entanglement foundations.

<a id="m27"></a>

### M27 — Finite inequalities and the leading frontier

**Central question.** What quantitative resource law follows when the unrestricted converse and explicit constructions are compared?

**Understanding target.** For $`0<\epsilon\le1/2`$, the finite upper bound is

```math
E_{\mathrm{sim}}(n,\epsilon)
\le\min\left\{n,\log_2\left\lceil\frac{\pi}{2\sqrt\epsilon}\right\rceil\right\}.
```

For every $`r=2^k\le2^n`$ with $`k\ge1`$ and $`\alpha_r=4r\sqrt\epsilon\le1/2`$, the lower bound is $`(1-\alpha_r)\log_2r-h_2(\alpha_r)`$. Choosing the restriction scale gives

```math
m-\log_2[16(m+1)]-3\le E_{\mathrm{sim}}(n,\epsilon)\le m+2,
\qquad m=\min\left\{n,\frac12\log_2\frac1\epsilon\right\}.
```

Thus the ratio to $`m`$ tends to one when $`m\to\infty`$. The finite additive gap remains logarithmic. A separate uniform consequence is $`m/16\le E_{\mathrm{sim}}\le3m`$ for all $`n\ge1`$ and $`0<\epsilon\le2^{-16}`$.

**Dependencies and story role.** Integrates M15, M17–M18, M20, and M26. It joins the constructive and universal arguments into the central quantitative result.

**Conceptual connection.** Accuracy limits the phase scale that the converse can resolve, while the cyclic construction caps the cost by the full register size. Exact finite bounds, leading asymptotics, and a uniform small-error statement have different quantifiers.

**Source pointers.** [Frontier Theorem 1 and Corollaries 2–3](../science/frontier.md#1-explicit-finite-upper-and-lower-bounds); [converse Theorem 1](../science/converse.md#theorem-1-finite-error-converse).

<a id="m28"></a>

### M28 — Local operation counts and a complete finite error budget

**Central question.** Can the resource frontier be realized while charging preparation, local powers, arithmetic, and synthesis precision?

**Understanding target.** With $`R=2^w`$, the phase-gradient construction uses $`O(n+w)`$ local storage and $`O(nw+w^2+n)`$ online gates in the stated rotation-and-arithmetic basis. The tapered messages have $`w+1`$ and $`w`$ bits. Finite preparation attempts, imperfect resource amplitudes, intrinsic dephasing, and online synthesis contribute separately to a sufficient budget

```math
\epsilon_R+3\zeta+\nu+\delta_{\mathrm{online}}\le\epsilon.
```

Explicit rotations and finite attempt caps lead to a discrete gate count polynomial in $`n`$ and $`\log(1/\epsilon)`$. Controlled operations must preserve relative phases before decomposition into unconditionally applied rotations. A generic known $`V`$ has separately charged power and inverse costs; the short phase-gradient circuit does not make arbitrary powers free.

**Dependencies and story role.** Requires M07–M08, M14, M16–M20, and M27. It combines the ideal construction with a finite implementation account.

**Conceptual connection.** Resource-state entropy, Bell-pair supply, gate count, message length, and physical execution time measure different things. A shared error convention lets preparation and compilation guarantees be composed without changing the online causal model.

**Source pointers.** [Resource accounting §§4–7](../science/resource_accounting.md#4-online-registers-and-classical-messages); [randomized rounding: explicit arithmetic](../science/randomized_rounding.md#explicit-finite-randomness-for-the-phase-gradient-family); Dawson–Nielsen, Ross–Selinger, and Cuccaro and collaborators in [related work](../references/RELATED_WORK.md#interactive-implementation-and-local-circuit-costs).

<a id="m29"></a>

### M29 — Comparison with prior results and communication models

**Central question.** Which established results supply ingredients, and which comparisons address the same operational question?

**Understanding target.** The exact separation, finite-group protocols, sine profiles, interactive implementation, and continuity theorem retain their respective prior attributions. The central quantitative contribution is the robust mixed-resource converse and the resulting matching leading frontier. Cleve–May's ideal correlation criterion yields one-half ebit on this family in either orientation; its entanglement criterion does not give a growing target-reference bound here. Their quantum-message model and dimension-dependent noisy bounds require a separate comparison. Generic exact-impossibility results also concern a different statement from finite-error cost for root-of-unity targets.

**Dependencies and story role.** Requires M13, M15, M18, M20, and M26–M28. It places the completed theorem among existing tools and distinct operational results.

**Conceptual connection.** Allowing $`q`$ quantum message qubits changes what is charged: teleportation converts the present lower bound into a bound on $`E_F+q`$, not on entanglement alone. Comparisons must retain communication type, error convention, resource measure, and exact-versus-approximate scope.

**Source pointers.** [Related work](../references/RELATED_WORK.md), including [Cleve–May v4](https://arxiv.org/html/2602.00255v4) and [Folkertsma and collaborators](https://arxiv.org/html/2609.40228v1); [bridge: attribution](WATROUS_BRIDGE.md#attribution). Watrous §6.3.1 supplies the teleportation foundation.

<a id="m30"></a>

### M30 — Complete physical account, regimes, and verification boundaries

**Central question.** What does the finished result establish about replacing feedback with entanglement, and where does that conclusion stop?

**Understanding target.** The target, causal model, mixed-resource measure, reference-sensitive error, explicit preparation and local circuits, and arbitrary-protocol converse form one consistent account. For fixed nonzero error, an upper cost independent of $`n`$ is available. For fixed $`n`$, the cost approaches $`n`$ as error tends to zero. When $`m\to\infty`$, the simultaneous-message cost has leading value $`m`$, while two sequential messages still permit exact implementation with one ebit. The remaining additive gap and the restriction of the lower bound to the phase-gradient family are visible parts of the result.

**Dependencies and story role.** Integrates M13–M29, with M27–M29 providing the final quantitative, physical, and comparative pieces. It closes the narrative by relating the complete implementation to the complete theorem.

**Conceptual connection.** Finite superoperator calculations can check signs, boundary branches, preparation identities, and evaluated bounds. They do not prove the converse for every mixed resource or establish optimality of a particular resource profile. Likewise, a communication-round advantage does not by itself establish shorter physical runtime, device noise tolerance, or a security guarantee for a separate verification task.

**Source pointers.** [Interpretation](../science/interpretation.md); [frontier: consequences and limits](../science/frontier.md#5-consequences-and-limits); [resource accounting](../science/resource_accounting.md); [verification scope](../verification/README.md); [bridge: timing and resources](WATROUS_BRIDGE.md#timing-and-resources).
