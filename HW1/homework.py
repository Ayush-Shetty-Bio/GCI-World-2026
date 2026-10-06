import numpy as np


def homework(a: np.ndarray) -> np.ndarray:
    return a[(a % 5 == 0) & (a % 2 == 1)]
