N = int(input())
a = [int(input()) for _ in range(N)]
M = int(input())

def chmax(a, b):
    if a < b:
        return b
    else:
        return a

f = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(i):
        sum_ji = 0
        for k in range(j, i):
            sum_ji += a[k]
        f[j][i] = sum_ji / (i - j)
    
dp = [[float("-inf")] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(i):
        for k in range(1, M + 1):
            dp[i][k] = chmax(dp[i][k], dp[j][k-1] + f[j][i])

print(dp[N][M])
