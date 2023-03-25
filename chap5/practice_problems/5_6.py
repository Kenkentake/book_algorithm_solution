from typing import TypeVar

T = TypeVar("T")
N = int(input())
a = [int(input()) for _ in range(N)]
m = [int(input()) for _ in range(N)]
W = int(input())

def chmin(a: T, b: T) -> T:
    if a > b:
        return b
    else:
        return a

dp = [[float("inf")] * (W + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(W + 1):
        if dp[i][j] < float("inf"):
            dp[i + 1][j] = chmin(dp[i + 1][j], 0)
        if j >= a[i] and dp[1 + 1][j - a[i]] < m[i]:
            dp[i + 1][j] = chmin(dp[i + 1][j], dp[i + 1][j - a[i]] + 1)

if dp[N][W]:
    print("Yes")
