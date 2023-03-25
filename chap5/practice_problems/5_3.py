N = int(input())
a = [int(input()) for _ in range(N)]
W = int(input())

dp = [[False] * (W + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(N):
    for j in range(W + 1):
        if not dp[i][j]:
            continue
        dp[i+1][j] = True
        if j+a[i] <= W:
            dp[i+1][j+a[i]] = True

res = 0
for j, bool_j in enumerate(dp[N]):
    if j <= W and bool_j:
        res += 1

print(res)
