"""Finite checks of constants and limiting cases in the analytic bounds."""
from __future__ import annotations

import math
from bounds import lower_bound, sine_error, upper_bound


def run() -> dict:
    cases = 0
    smallest_margin = float("inf")
    table = []
    for n in range(1, 65):
        previous_lower = previous_upper = 0.0
        for precision_bits in range(1, 193):
            eps = 2.0 ** (-precision_bits)
            low, k = lower_bound(n, eps)
            up, rank = upper_bound(n, eps)
            m = min(n, precision_bits / 2)
            conservative = m - math.log2(16 * (m + 1)) - 3
            assert low + 1e-12 >= conservative
            assert low <= up + 1e-12
            assert up <= m + 2 + 1e-12
            assert low + 1e-12 >= previous_lower
            assert up + 1e-12 >= previous_upper
            if rank is not None:
                assert sine_error(rank) <= eps * (1 + 1e-12)
            if precision_bits >= 16:
                assert low + 1e-12 >= m / 16
                assert up <= 3 * m + 1e-12
            smallest_margin = min(smallest_margin, low - conservative)
            previous_lower, previous_upper = low, up
            cases += 1
            if n == 32 and precision_bits in (16, 32, 48, 64, 96):
                table.append({"n": n, "accuracy_bits": precision_bits, "lower_ebits": round(low, 8),
                              "upper_ebits": round(up, 8), "lower_restriction_bits": k})
        assert lower_bound(n, 0)[0] == upper_bound(n, 0)[0] == n
        assert upper_bound(n, 0.5)[0] == 0
    return {"finite_bound_cases": cases, "minimum_conservative_lower_margin": smallest_margin,
            "illustrative_bounds": table, "scope": "Evaluation of proved inequalities; no universal converse is numerically certified."}


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
