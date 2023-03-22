N = int(input())
a = [int(input()) for _ in range(N)]
W = int(input())

dp = [[False for _ in range(W + 1)] for _ in range(N + 1)]
dp[0][0] = True

for i in range(N):
    for j in range(W + 1):
        if dp[i][j]:
            dp[i + 1][j] = True
        if a[i] <= j and dp[i][j - a[i]]:
            dp[i + 1][j] = True

if dp[N][W]:
    print("Yes")
