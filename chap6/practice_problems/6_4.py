N = int(input())
a = [int(input()) for _ in range(N)]
M = int(input())

left = 0
right = 1e10
a.sort()

while right - left > 1:
    x = (left + right) // 2
    count = 1
    prev = 0
    for i in range(N):
        if a[i] - a[prev] >= x:
            count += 1
            prev = i
    if count >= M:
        left = x
    else:
        right = x

print(left)
