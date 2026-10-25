"""Evaluate proved finite bounds; these numerical evaluations are not a proof."""
from __future__ import annotations

import math


def binary_entropy(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def sine_error(rank: int) -> float:
    """Half-diamond error, evaluated without 1-cos cancellation."""
    if rank < 1:
        raise ValueError("rank must be positive")
    return math.sin(math.pi / (2.0 * (rank + 1))) ** 2


def lower_bound(n: int, epsilon: float) -> tuple[float, int | None]:
    if n < 1 or not 0.0 <= epsilon <= 1.0:
        raise ValueError("require n>=1 and 0<=epsilon<=1")
    if epsilon == 0.0:
        return float(n), n
    best, best_k = 0.0, None
    for k in range(1, n + 1):
        alpha = 4.0 * 2.0**k * math.sqrt(epsilon)
        if alpha > 0.5:
            break
        value = (1.0 - alpha) * k - binary_entropy(alpha)
        if value > best:
            best, best_k = value, k
    return best, best_k


def upper_bound(n: int, epsilon: float) -> tuple[float, int | None]:
    """Entropy upper bound log R, or exact n; None selects the exact protocol."""
    if n < 1 or not 0.0 <= epsilon <= 1.0:
        raise ValueError("require n>=1 and 0<=epsilon<=1")
    if epsilon >= 0.5:
        return 0.0, 1
    if epsilon == 0.0:
        return float(n), None
    # Conservative rank used in the written theorem; the +1 in sine_error
    # only improves the achieved error. The actual sine entropy can be lower.
    rank = math.ceil(math.pi / (2.0 * math.sqrt(epsilon)))
    if math.log2(rank) >= n:
        return float(n), None
    return math.log2(rank), rank
