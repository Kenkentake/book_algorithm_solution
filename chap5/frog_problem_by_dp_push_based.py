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

dp[0] = 0

for i in range(0, N - 1):
    dp[i + 1] = chmin(dp[i + 1], dp[i] + abs(h[i + 1] - h[i]))
    if i < N - 2:
        dp[i + 2] = chmin(dp[i + 2], dp[i] + abs(h[i + 2] - h[i]))

print(dp[N - 1])
