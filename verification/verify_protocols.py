"""Independent finite checks of physical operations and resource preparation.

This script contracts the control, both local resource registers, and target
before comparing the channel with the claimed dephasing form. It does not
establish the universal mixed-resource converse or a diamond-norm SDP bound.
"""
from __future__ import annotations

import math
import numpy as np

TOL = 2e-11


def controlled(v: np.ndarray) -> np.ndarray:
    d = len(v)
    out = np.eye(2 * d, dtype=complex)
    out[d:, d:] = v
    return out


def unitary(d: int, rng: np.random.Generator) -> np.ndarray:
    a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    q, r = np.linalg.qr(a)
    phases = np.diag(r)
    return q @ np.diag(phases / np.abs(phases))


def superoperator(kraus: list[np.ndarray]) -> np.ndarray:
    # Column-vectorization convention.
    dim = kraus[0].shape[0]
    out = np.zeros((dim * dim, dim * dim), dtype=complex)
    for k in kraus:
        out += np.kron(k.conj(), k)
    return out


def tapered_physical_kraus(v: np.ndarray, c: np.ndarray) -> list[np.ndarray]:
    """Apply each physical local operation to the full initialized isometry."""
    r, d = len(c), len(v)
    # Indices: A, Alice-resource (R+1 levels), Bob-resource, B, input AB.
    state = np.zeros((2, r + 1, r, d, 2 * d), dtype=complex)
    for x in range(2):
        for k in range(r):
            for b in range(d):
                state[x, k + 1, k, b, x * d + b] = c[k]
    # Controlled decrement is a full cyclic permutation on R+1 levels.
    state[1] = np.roll(state[1], -1, axis=0)
    # Bob's controlled powers, before receiving Alice's message.
    for k in range(r):
        state[:, :, k] = np.einsum(
            "ij,xajn->xain", np.linalg.matrix_power(v, k), state[:, :, k]
        )
    result = []
    for encoded_j in range(r + 1):
        j = encoded_j - 1
        for q in range(r):
            fourier_bra = np.exp(-2j * np.pi * q * np.arange(r) / r) / np.sqrt(r)
            # Local measurements: computational on Alice; Fourier on Bob.
            branch = np.einsum("k,xkbn->xbn", fourier_bra, state[:, encoded_j])
            # Corrections are applied only after the simultaneous exchange.
            branch = np.einsum("ab,xbn->xan", np.linalg.matrix_power(v, -j), branch)
            branch[1] *= np.exp(2j * np.pi * q / r)
            result.append(branch.reshape(2 * d, 2 * d))
    return result


def cyclic_physical_kraus(v: np.ndarray, r: int) -> list[np.ndarray]:
    """Inherited cyclic protocol; exact only when V**R=I."""
    d = len(v)
    state = np.zeros((2, r, r, d, 2 * d), dtype=complex)
    for x in range(2):
        for k in range(r):
            for b in range(d):
                state[x, k, k, b, x * d + b] = 1 / np.sqrt(r)
    state[1] = np.roll(state[1], -1, axis=0)
    for k in range(r):
        state[:, :, k] = np.einsum(
            "ij,xajn->xain", np.linalg.matrix_power(v, k), state[:, :, k]
        )
    result = []
    for a in range(r):
        for q in range(r):
            fourier_bra = np.exp(-2j * np.pi * q * np.arange(r) / r) / np.sqrt(r)
            branch = np.einsum("k,xkbn->xbn", fourier_bra, state[:, a])
            branch = np.einsum("ab,xbn->xan", np.linalg.matrix_power(v, -a), branch)
            branch[1] *= np.exp(2j * np.pi * q / r)
            result.append(branch.reshape(2 * d, 2 * d))
    return result


def run() -> dict:
    rng = np.random.default_rng(271828)
    maxima = {"channel_residual": 0.0, "trace_preservation_residual": 0.0,
              "half_trace_witness_residual": 0.0, "sine_identity_residual": 0.0,
              "cyclic_channel_residual": 0.0, "offline_preparation_residual": 0.0,
              "preparation_success_residual": 0.0}
    total = 0
    for d in (2, 3, 4):
        v = unitary(d, rng)
        target = controlled(v)
        z = np.diag([1] * d + [-1] * d)
        plus_zero = np.zeros(2 * d, dtype=complex)
        plus_zero[0] = plus_zero[d] = 1 / np.sqrt(2)
        input_rho = np.outer(plus_zero, plus_zero.conj())
        for r in (1, 2, 3, 5, 8):
            profiles = {
                "sine": np.sqrt(2 / (r + 1)) * np.sin(np.pi * np.arange(1, r + 1) / (r + 1)),
                "uniform": np.full(r, 1 / np.sqrt(r)),
                "nonuniform": rng.uniform(0.1, 1.0, size=r),
            }
            profiles["nonuniform"] /= np.linalg.norm(profiles["nonuniform"])
            for name, c in profiles.items():
                klist = tapered_physical_kraus(v, c)
                f = float(c[:-1] @ c[1:])
                eps = (1 - f) / 2
                expected = [np.sqrt((1 + f) / 2) * target, np.sqrt(eps) * z @ target]
                channel_err = np.linalg.norm(superoperator(klist) - superoperator(expected), 2)
                tp_err = np.linalg.norm(sum(k.conj().T @ k for k in klist) - np.eye(2 * d), 2)
                actual = sum(k @ input_rho @ k.conj().T for k in klist)
                ideal = target @ input_rho @ target.conj().T
                witness = np.linalg.norm(actual - ideal, ord="nuc") / 2
                maxima["channel_residual"] = max(maxima["channel_residual"], float(channel_err))
                maxima["trace_preservation_residual"] = max(maxima["trace_preservation_residual"], float(tp_err))
                maxima["half_trace_witness_residual"] = max(maxima["half_trace_witness_residual"], abs(float(witness) - eps))
                if name == "sine":
                    maxima["sine_identity_residual"] = max(maxima["sine_identity_residual"], abs(f - math.cos(math.pi / (r + 1))))
                assert max(channel_err, tp_err, abs(witness - eps)) < TOL
                total += 1
    for d in (2, 4, 8):
        v = np.diag(np.exp(2j * np.pi * np.arange(d) / d))
        klist = cyclic_physical_kraus(v, d)
        err = float(np.linalg.norm(superoperator(klist) - superoperator([controlled(v)]), 2))
        maxima["cyclic_channel_residual"] = max(maxima["cyclic_channel_residual"], err)
        assert err < TOL
    for r in (2, 4, 8, 16):
        angles = np.pi * np.arange(1, r + 1) / (r + 1)
        unnormalized = np.sin(angles) / np.sqrt(r)
        success = float(unnormalized @ unnormalized)
        c = np.sqrt(2 / (r + 1)) * np.sin(angles)
        prep_err = float(np.linalg.norm(unnormalized / np.sqrt(success) - c))
        success_err = abs(success - (r + 1) / (2 * r))
        completeness = sum(np.diag(np.roll(c, -s) ** 2) for s in range(r))
        prep_err = max(prep_err, float(np.linalg.norm(completeness - np.eye(r), 2)))
        target_shared = np.diag(c).reshape(-1)
        for s in range(r):
            # Measuring the local sine ancilla after subtraction gives c[k+s].
            branch = np.diag(np.roll(c, -s)) / np.sqrt(r)
            probability = float(np.vdot(branch, branch).real)
            corrected = np.roll(np.roll(branch, s, axis=0), s, axis=1)
            corrected = corrected.reshape(-1) / np.sqrt(probability)
            prep_err = max(prep_err, float(np.linalg.norm(corrected - target_shared)), abs(probability - 1 / r))
        maxima["offline_preparation_residual"] = max(maxima["offline_preparation_residual"], prep_err)
        maxima["preparation_success_residual"] = max(maxima["preparation_success_residual"], success_err)
        assert max(prep_err, success_err) < TOL
    return {"tapered_cases": total, "cyclic_cases": 3, "offline_preparation_ranks": [2, 4, 8, 16],
            "tolerance": TOL, "maximum_residuals": maxima}


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
