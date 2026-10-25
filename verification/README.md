# Reproducing the finite checks

[Scientific overview](../README.md) · [Converse proof](../science/converse.md) · [Protocols](../science/protocols.md) · [Finite bounds](../science/frontier.md)

The general entanglement lower bound is an analytical theorem. The scripts here check physical constructions, normalization and error conventions, finite-parameter consequences, and the numerical evaluation used in the figure. They do not enumerate all protocols or certify a mixed-resource converse by simulation.

## Environment and commands

The reference run used Python 3.12.14, NumPy 2.3.5, and Matplotlib 3.10.8. The scientific checks require NumPy; Matplotlib is used only by the figure generator. Install the pinned packages and run from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The final output is `All finite checks passed`. To keep a fresh result separately from the committed reference:

```bash
python3 verification/run_all.py --output verification/latest_results.json
```

[The reference JSON](expected/results.json) records the dimensions, counts, tolerances, representative bounds, and observed residuals. Floating-point residuals may vary slightly across platforms; the scripts assert explicit tolerances instead of requiring byte-identical output.

## What each check establishes

| Script | Independent calculation | Claim boundary |
|---|---|---|
| [verify_protocols.py](verify_protocols.py) | Initialize the full control/resource/target state; apply physical controlled shifts, local powers, Fourier measurement and corrections; compare the resulting superoperator with target plus dephasing | Checks the displayed construction on finite instances, not optimality among all protocols |
| [verify_protocols.py](verify_protocols.py) | Check exact cyclic gates and the offline sine-amplitude and shared-resource preparation, including every preparation outcome | Checks correction signs, normalization, heralding probability, and resource-state identity |
| [verify_bounds.py](verify_bounds.py) | Evaluate the optimized finite converse and achievable upper bound across register sizes and accuracy values; check conservative constants, monotonicity, and endpoints | Checks evaluation and numerical consequences; the full parameter statements are proved in the science pages |
| [verify_rounding.py](verify_rounding.py) | Enumerate the finite random thresholds; verify zero mean phase error and the rounded unitary's finite order | Checks the finite construction; the dimension-independent diamond estimate uses the analytical remainder bound |

The protocol checks use target dimensions 2, 3, and 4; resource ranks 1, 2, 3, 5, and 8; and sine, uniform, and nonuniform real profiles. The resource-rank-one case tests the zero-entanglement dephasing endpoint. Generic target unitaries are generated reproducibly with a fixed seed. The expected-channel comparison uses complete superoperators, so it checks action on every matrix element in each finite instance.

The half-trace-distance witness uses a coherent control input and verifies the attained error. The equality with half diamond error follows analytically from the residual Pauli channel; a trace-distance witness alone would supply only a lower bound on diamond error. No semidefinite-program calculation of that norm is claimed.

The protocol residual tolerance is $`2\times10^{-11}`$. In the recorded run all channel and preparation residuals were below $`1.8\times10^{-15}`$. The finite-threshold root-of-unity residual was below $`4.3\times10^{-14}`$. These values measure floating-point consistency with the claimed finite identities.

## Figure generation

```bash
python3 verification/plot_frontier.py
```

This overwrites [precision_frontier.svg](../figures/precision_frontier.svg) using the same [bound functions](bounds.py) as the checks. An optional local PNG preview can be produced with `--preview PATH.png`. On a system without a writable default Matplotlib cache, set `MPLCONFIGDIR` to a writable temporary directory before running.

The left panel fixes $`n=32`$ and varies accuracy bits $`p=\log_2(1/\epsilon)`$. The right panel fixes $`\epsilon=2^{-48}`$ and varies $`n`$. The lower curve is the maximum of zero and all eligible power-of-two converse bounds. The upper curve is $`\min\{n,\log_2\lceil\pi/(2\sqrt\epsilon)\rceil\}`$, an achievable entropy bound. It does not substitute the smaller entropy of the actual sine profile or claim that every point in the shaded interval is attainable. The dashed line is the leading scale $`m`$. The one-Bell-pair baseline allows two sequential directed messages.

## Analytical dependencies

The scientific proof separately establishes the purified protocol normal form, the common environment approximation, no-signalling invariance, the cyclic twirl, the conditional entropy estimate without a workspace-dimension factor, and the convex-roof step. See [converse](../science/converse.md) for those arguments and [related work](../references/RELATED_WORK.md) for imported theorems. The finite checks are useful for identifying normalization, boundary, sign, and evaluation errors; their successful completion is not a substitute for those analytical dependencies.
