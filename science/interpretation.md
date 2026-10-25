# What the tradeoff says about remote quantum computation

[Model](model.md) · [Finite bounds](frontier.md) · [Resource accounting](resource_accounting.md) · [Related work](../references/RELATED_WORK.md)

## Entanglement can replace a feedback step

The usual remote controlled-unitary protocol needs one Bell pair and two sequential directed messages. The second party acts after receiving the first correction, then sends a correction back. Its entanglement cost does not grow with the dimension of the controlled unitary. That construction and the exact entanglement gap under simultaneous classical communication are established results, credited in [related work](../references/RELATED_WORK.md).

For the phase-gradient family, a one-exchange protocol instead has leading cost

```math
m=\min\!\left\{n,\frac12\log_2\frac1\epsilon\right\},
```

with an upper additive constant and a lower additive $`O(\log(m+1))`$ correction. The robust lower bound permits arbitrary finite mixed resources and arbitrary local quantum memories. Its conclusion therefore concerns the communication model, not only the efficiency of the displayed protocol.

The distinction is causal: two messages sent at once cannot use each other's information. It does not imply that the local computation is instantaneous, or that the construction halves physical runtime. State distribution, local processing, communication propagation, and synthesis contribute separate costs.

## Exact spectral distinctness is not a finite-accuracy resource law

All $`d=2^n`$ eigenphases are distinct, so exact implementation under one simultaneous classical exchange costs $`n`$ ebits. The finite-error upper bound gives a different conclusion: for any fixed $`\epsilon>0`$, a resource of size independent of $`n`$ suffices.

Both statements are consistent. An exact requirement resolves every distinct phase, even when adjacent phases become extremely close. A fixed error tolerance does not. The result identifies a resolution scale at which accuracy, rather than the full target dimension, determines the leading entanglement cost.

The raw finite converse also shows that, for each fixed $`n`$, the cost approaches $`n`$ as $`\epsilon\to0`$. The large-register and high-accuracy regimes should therefore be specified when discussing the separation.

## Examples of the asymptotic regimes

These examples describe leading orders, not exact finite-error minima. Their rigorous finite inequalities are in the [frontier](frontier.md).

| Accuracy requirement as $`n`$ grows | Leading cost of one simultaneous exchange | Exact interactive implementation |
|---|---|---|
| Fixed nonzero error | Bounded above independently of $`n`$ | One Bell pair |
| $`\epsilon=2^{-n}`$ | $`n/2`$ up to an additive logarithmic gap | One Bell pair |
| $`\epsilon=2^{-2n}`$ | $`n`$ up to an additive logarithmic gap | One Bell pair |
| Zero error | Exactly $`n`$ | Exactly one Bell pair |

The first row prevents an incorrect interpretation of the result as an unbounded constant-error separation. The middle rows show the robust separation that remains as more accuracy is demanded. They do not rely on sending a larger quantum input from Alice; her input is always one qubit.

## Why a tapered resource helps

In the explicit protocol, shifting the shared resource by one label correlates it with Alice's control. After the classical corrections, the only remaining disturbance is determined by the overlap of the resource profile with its one-step translate:

```math
f=\sum_{k=0}^{R-2}c_kc_{k+1}.
```

A uniform profile has an abrupt boundary and gives $`1-f=1/R`$. The sine profile smoothly decreases toward the two boundaries and gives $`1-f=1-\cos(\pi/(R+1))=O(R^{-2})`$. The resulting half-diamond error is $`(1-f)/2`$. This is an exact channel calculation, not a fidelity proxy.

Sine profiles and related reference-state optimizations are established tools. Their role here is to supply a transparent construction against which to compare the general converse. The [randomized rounding argument](randomized_rounding.md) offers a different mechanism for the same leading upper order: cancel first-order coherent phase errors by averaging, leaving a quadratic channel error.

## How the converse detects the cost

After mathematically undoing Bob's final correction, his actual pre-exchange channel cannot depend on Alice's control basis value. Closeness to an ideal controlled gate forces this channel to be approximately invariant under Bob's phase-gradient action. Averaging that action nearly dephases Bob's input.

The argument then inserts local Fourier inputs into Bob's instrument. The ideal comparison states are flat across at least $`r`$ directions, so they carry at least $`\log_2r`$ entropy. A dimension-independent entropy estimate transfers most of this entropy to the actual conditional states. Since Bob's local operation cannot increase the average entanglement in any pure decomposition of the shared resource, the initial resource must already have that entanglement.

The [full proof](converse.md) handles the mismatch between actual and ideal branch probabilities. It uses the ensemble label only as a mathematical flag and does not assume that the parties can read a decomposition of their mixed resource.

## Limits of the conclusion

The quantitative lower bound is proved for this cyclic phase-gradient family. The tapered upper protocol works more broadly for known binary-controlled unitaries, but it does not supply a matching lower bound for every spectrum. Local powers of a generic unitary may be expensive.

The theorem counts initial entanglement of formation. It is not an exact formula for one-shot Bell-pair formation cost, retained catalyst cost, or a regularized many-copy rate. The construction's Bell-pair count has the same leading scaling, while its resource entropy can be smaller.

Finally, free quantum messages change the model. Teleporting a protocol's $`q`$ communicated qubits gives a lower bound on $`E_F+q`$, not on entanglement alone. An operational statement about position-verification security would additionally need a particular verification task, its success criterion, and a reduction; the gate-simulation theorem by itself is not that security statement.
