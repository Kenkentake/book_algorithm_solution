def func(N: int) -> int:
    if N == 0:
        return N
    return N + func(N + 1)
