import numpy as np

__all__ = ('euclidean', 'manhattan', )


def _validate_arrays(x: np.ndarray, y: np.ndarray):

    if not isinstance(x, np.ndarray):
        raise ValueError("x should be an instance of np.ndarray")

    if not isinstance(y, np.ndarray):
        raise ValueError("y should be an instance of np.ndarray")

    if x.shape != y.shape:
        raise ValueError("Arrays should be of same shape")


def _normalize(arr: np.ndarray) -> np.ndarray:
    s = arr.sum()
    if s == 0:
        return ValueError("Sum should be not zero")
    return arr / s


def euclidean(x: np.ndarray, y: np.ndarray, normalize=False) -> float:
    _validate_arrays(x, y)
    if normalize:
        x = _normalize(x)
        y = _normalize(y)
    return np.sqrt(np.power(x - y, 2.0).sum())


def manhattan(x: np.ndarray, y: np.ndarray, normalize=False) -> float:
    _validate_arrays(x, y)
    if normalize:
        x = _normalize(x)
        y = _normalize(y)
    return np.fabs(x - y).sum()
