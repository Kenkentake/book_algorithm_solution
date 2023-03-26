from typing import TypeVar

T = TypeVar("T")
N = int(input())
a = [int(input()) for _ in range(N)]

def chmin(a: T, b: T) -> T:
    if a > b:
        return b
    else:
        return a

S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + a[i]

dp = [[float("inf")] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    dp[i][i + 1] = 0

for bet in range(2, N + 1):
    for i in range(0, N + 1 - bet):
        j = i + bet
        for k in range(i + 1, j):
            dp[i][j] = chmin(dp[i][j], dp[i][k] + dp[k][j] + S[j] - S[i])

print(dp[0][N])
