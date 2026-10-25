"""Check finite threshold rounding and the cancellation of phase bias."""
from __future__ import annotations

import numpy as np


def run() -> dict:
    maxima = {"mean_phase_error": 0.0, "finite_order_residual": 0.0,
              "averaged_matrix_unit_residual": 0.0}
    cases = 0
    for n in range(1, 7):
        d = 2**n
        original = 2 * np.pi * np.arange(d) / d
        for q in range(1, n + 1):
            rank, denominator = 2**q, 2 ** (n - q)
            h = 2 * np.pi / rank
            high, low = np.divmod(np.arange(d), denominator)
            errors, rounded = [], []
            for t in range(denominator):
                phases = h * (high + (t < low))
                errors.append(phases - original)
                rounded.append(np.exp(1j * phases))
            errors = np.asarray(errors)
            rounded = np.asarray(rounded)
            mean_error = float(np.max(np.abs(errors.mean(axis=0))))
            order_error = float(np.max(np.abs(rounded**rank - 1)))
            # Relative phase factors on ALL matrix units of the controlled gate.
            relative = np.exp(1j * np.concatenate([np.zeros_like(errors), errors], axis=1))
            matrix_factors = np.einsum("ta,tb->ab", relative, relative.conj()) / denominator
            remainder = float(np.max(np.abs(matrix_factors - 1)))
            # A matrix-unit check is not a computation of the diamond norm.
            assert mean_error < 1e-13
            assert order_error < 1e-12
            assert remainder <= 2 * h**2 + 1e-12
            maxima["mean_phase_error"] = max(maxima["mean_phase_error"], mean_error)
            maxima["finite_order_residual"] = max(maxima["finite_order_residual"], order_error)
            if q == n:
                maxima["averaged_matrix_unit_residual"] = max(maxima["averaged_matrix_unit_residual"], remainder)
            cases += 1
    return {"phase_gradient_cases": cases, "maximum_residuals": maxima,
            "scope": "Finite-order phases and exact bias cancellation; the uniform diamond estimate is proved analytically."}


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
