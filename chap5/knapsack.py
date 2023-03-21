from typing import TypeVar


T = TypeVar("T")

def chmax(a: T, b: T) -> int:
    if a < b:
        return b
    else:
        return a

N = int(input())
weight = [int(input()) for _ in range(N)]
value = [int(input()) for _ in range(N)]
W = int(input())

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N):
    for w in range(W+1):
        if w - weight[i] >= 0:
            dp[i + 1][w] = chmax(dp[i + 1][w], dp[i][w - weight[i]] + value[i])
        dp[i + 1][w] = chmax(dp[i + 1][w], dp[i][w])

print(dp[N][W])        
