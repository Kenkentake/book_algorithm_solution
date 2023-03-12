def func(N: int) -> int:
    if N == 0:
        return 0
    return N + func(N - 1)

ans = func(5)
print(ans)
