"""Small statistics shared by the blind-judging scorers: Wilson intervals and Fleiss' kappa."""
from __future__ import annotations

import numpy as np


def wilson(k: int, n: int, z: float = 1.959964) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return (round(float(centre - half), 4), round(float(centre + half), 4))


def fleiss_kappa(counts: np.ndarray) -> float:
    """counts: items x categories, each row summing to the number of raters."""
    counts = np.asarray(counts, float)
    n = counts.sum(axis=1)[0]
    p_cat = counts.sum(axis=0) / counts.sum()
    p_item = ((counts * (counts - 1)).sum(axis=1)) / (n * (n - 1))
    pe = (p_cat ** 2).sum()
    return round(float((p_item.mean() - pe) / (1 - pe)), 4) if pe < 1 else float("nan")
