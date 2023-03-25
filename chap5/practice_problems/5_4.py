from typing import TypeVar

T = TypeVar("T")
N = int(input())
a = [int(input()) for _ in range(N)]
W = int(input())
k = int(input())

def chmin(a: T, b: T) -> int:
    if (a > b):
        return b
    else:
        return a

dp = [[float("inf")] * (W + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(W + 1):
        dp[i + 1][j] = chmin(dp[i + 1][j], dp[i][j])
        if j + a[i] <= W:
            dp[i + 1][j + a[i]] = chmin(dp[i + 1][j + a[i]], dp[i][j] + 1)

if dp[N][W] <= k:
    print("Yes")
