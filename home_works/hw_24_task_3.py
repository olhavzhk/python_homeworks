from typing import Optional


def mult(a: Optional[int], n: Optional[int]) -> Optional[int]:
    if a <= 0 or n < 0:
        raise ValueError("This function works only with positive integers")
    if n == 0:
        return 0
    if n == 1:
        return a
    return a + mult(a, n - 1)
