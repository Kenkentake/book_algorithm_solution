def func(N: int) -> int:
    print(f"{N}を呼び出しました")
    if N == 0:
        return 0
    result = N + func(N-1)
    print(f"{N}までの和 = {result}")
    return result

ans = func(5)
