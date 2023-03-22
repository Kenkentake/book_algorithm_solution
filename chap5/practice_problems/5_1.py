from typing import TypeVar


T = TypeVar("T")

def chmax(a: T, b: T) -> int:
    if a < b:
        return b
    else:
        return a

N = int(input())
a = [int(input()) for _ in range(N)]
b = [int(input()) for _ in range(N)]
c = [int(input()) for _ in range(N)]
h = [a, b, c]

dp = [[0 for _ in range(3)] for _ in range(N + 1)]

for i in range(N):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i + 1][k] = chmax(dp[i + 1][k], dp[i][j] + h[k][i])

res = 0
for j in range(3):
    res = chmax(res, dp[N][j])
    
print(res)    
