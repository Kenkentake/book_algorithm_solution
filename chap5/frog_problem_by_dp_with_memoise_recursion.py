from typing import TypeVar

T = TypeVar("T")
N = int(input())
h = [int(input()) for _ in range(N)]

dp = [float("inf")] * N

def chmin(a: T, b: T) -> int:
    if (a > b):
        return b
    else:
        return a

def rec(i: int) -> int:
    if dp[i] < float("inf"):
        return dp[i]

    if i == 0:
        return 0

    res = float("inf")
    chmin(res, rec(i - 1) + abs(h[i] - h[i - 1]))
    if i > 1:
        chmin(res, rec(i - 2) + abs(h[i] - h[i - 2]))
    return dp[i] := res

print(rec[N - 1])
