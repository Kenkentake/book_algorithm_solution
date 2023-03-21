from typing import TypeVar


T = TypeVar("T")

def chmin(a: T, b: T) -> int:
    if a < b:
        return a
    else:
        return b

N = int(input())
c = [[int(input()) for j in range(N + 1)] for i in range(N + 1)]

dp = [float("inf")] * (N + 1)
dp[0] = 0

for i in range(N + 1):
    for j in range(i):
        dp[i] = chmin(dp[i], dp[j] + c[j][i])

print(dp[N])
