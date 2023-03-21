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

for i in range(1, N):
    dp[i] = chmin(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]))
    if i > 1:
        dp[i] = chmin(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]))

print(dp[N - 1])
