# The remote gate and the resources being counted

[Repository overview](../README.md) · [Converse](converse.md) · [Protocols](protocols.md) · [Tradeoff](frontier.md)

## A question about feedback

Alice and Bob want to apply a joint quantum gate while keeping their input and output systems in separate laboratories. With an entangled pair, Alice can first send Bob a correction bit; after acting on his input, Bob sends a correction bit back. That second message depends on receiving the first. If both parties must send their messages simultaneously, this feedback mechanism is unavailable.

The question here is how much additional preshared entanglement replaces that feedback, and how the answer changes when the implemented gate may have a small error. The target family keeps Alice's input to one qubit while increasing Bob's register size. It therefore distinguishes communication structure from the number of qubits held by the smaller party.

## Target family

Let Alice's system $`A`$ be a qubit and Bob's system $`B`$ have dimension $`d=2^n`$, with $`n\ge1`$. In Bob's computational basis, define

```math
Z_d=\sum_{j=0}^{d-1}e^{2\pi i j/d}|j\rangle\langle j|,
\qquad
C_d=|0\rangle\langle0|\otimes I_B
    +|1\rangle\langle1|\otimes Z_d.
```

The corresponding quantum channel is $`\mathcal C_d(X)=C_dXC_d^\dagger`$. More generally, $`C(V)`$ denotes the binary-controlled version of a known unitary $`V`$ on Bob's system. The tapered protocol works for every such $`V`$; the quantitative lower bound is proved for $`V=Z_d`$.

This is a concrete arithmetic family. With the little-endian expansion $`j=\sum_{\ell=0}^{n-1}2^\ell j_\ell`$,

```math
Z_d=\bigotimes_{\ell=0}^{n-1}
\operatorname{diag}\!\left(1,e^{2\pi i 2^{\ell-n}}\right).
```

Thus $`C_d`$ is a product of controlled phase rotations between Alice's one control and Bob's individual qubits. The model assumes the target is known; it does not assume an oracle for an unknown unitary or a free inverse oracle. The [implementation account](resource_accounting.md) charges the required local rotations and their precision.

## One simultaneous classical exchange

An admissible protocol consists of the following operations.

1. Before the unknown inputs arrive, the parties share a finite-dimensional state $`\rho_{A'B'}`$. It may be mixed. Local pure ancillas and preshared classical randomness are allowed.
2. Alice applies an arbitrary local quantum instrument to $`AA'`$, producing a classical outcome $`a`$ and retained quantum systems. Bob independently applies an arbitrary local instrument to $`BB'`$, producing $`b`$ and retained quantum systems.
3. Alice sends $`a`$ while Bob sends $`b`$. Neither party's message can depend on receiving the other message.
4. Each party applies an arbitrary local completely positive trace-preserving map depending on both outcomes. The final computational systems have the same locations and dimensions as the original $`A`$ and $`B`$. Extra systems may be discarded.

This is the local-operations-and-broadcast-communication model, abbreviated LOBC in [Gonzales–Chitambar](../references/RELATED_WORK.md). The messages are classical. All resource spaces, outcome alphabets, and workspaces are finite in each admissible protocol, but there is no common dimension or message-length bound across the class. The converse allows arbitrarily large finite quantum memories and does not restrict operations to stabilizer circuits, a chosen construction, or unitary final decoders.

Local steps before or after the exchange can be composed into the instruments and maps above. Offline communication used to establish the resource takes place before the unknown inputs arrive. It is recorded as a preparation cost; it does not supply an additional online feedback step.

## Accuracy on unknown inputs

The implemented channel $`\Lambda`$ must satisfy

```math
\frac12\|\Lambda-\mathcal C_d\|_\diamond\le\epsilon.
```

The diamond norm maximizes the output trace norm over inputs that may be entangled with an untouched reference. Consequently, this is a worst-case quantum-channel requirement, including coherent superpositions of the control and entanglement with an external system. It is stronger than agreement on computational-basis inputs or average state fidelity.

Every error parameter in this repository is a **half diamond distance**, unless a full norm is explicitly written. For states, trace distance means half the trace norm. Logarithms and entropies are in base two, and $`h_2(t)=-t\log_2t-(1-t)\log_2(1-t)`$ with the usual endpoint convention.

## Entanglement cost

For a pure resource $`|\eta\rangle`$, its entanglement is the entropy of either reduced state. For a mixed resource, use entanglement of formation,

```math
E_F(\rho)=\inf_{\{p_\lambda,|\eta_\lambda\rangle\}}
\sum_\lambda p_\lambda
S\!\left(\operatorname{Tr}_{A'}|\eta_\lambda\rangle\langle\eta_\lambda|\right),
\qquad
\rho=\sum_\lambda p_\lambda|\eta_\lambda\rangle\langle\eta_\lambda|.
```

The main cost function is

```math
E_{\mathrm{sim}}(n,\epsilon)
=\inf\{E_F(\rho):\rho\text{ permits an admissible protocol for }C_d
\text{ with error at most }\epsilon\}.
```

This is the infimum for one implementation, not a regularized many-copy entanglement cost. No attainment is assumed. Any preshared quantum systems used by a protocol belong to its resource; shared classical registers may be included without entanglement charge. An ensemble label used in a proof is not assumed available to the parties.

For a maximally entangled rank-$`R`$ state, the entropy is $`\log_2R`$. An integer count of Bell pairs and $`E_F`$ are different resource measures: an arbitrary rank-$`R`$ pure state can be prepared from at most $`\lceil\log_2R\rceil`$ Bell pairs by offline LOCC, but its entropy need not equal that integer. The protocol pages keep these costs separate. Every lower bound on $`E_F`$ also lower-bounds the initial Bell-pair count of a realization that starts from Bell pairs and local resources.

## Claims and reading route

The [converse](converse.md) proves that, for every power of two $`r\le2^n`$ with $`\alpha_r=4r\sqrt\epsilon\le1/2`$,

```math
E_{\mathrm{sim}}(n,\epsilon)
\ge (1-\alpha_r)\log_2r-h_2(\alpha_r).
```

The [protocols](protocols.md) give an explicit tapered resource with error

```math
\epsilon_R=\frac{1-\cos(\pi/(R+1))}{2}
\le\frac{\pi^2}{4(R+1)^2},
\qquad E_F\le\log_2R.
```

Combining it with the inherited exact cyclic protocol gives a cost capped by $`n`$. The [tradeoff](frontier.md) states the resulting finite bounds, limiting cases, and leading asymptotic law. [Randomized spectral rounding](randomized_rounding.md) gives another way to understand the leading upper coefficient using established cyclic protocols. The [interpretation](interpretation.md) explains the communication advantage and the distinction between exact and approximate operation. Attribution and the comparison to other communication models are in [related work](../references/RELATED_WORK.md).

The scientific statements concern entanglement and online classical communication. Local gates, ancillas, synthesis accuracy, and offline preparation are separately accounted for in [resource accounting](resource_accounting.md); they are not assumed to have zero physical duration.
