N = int(input())
h = [int(input()) for _ in range(N)]
s = [int(input()) for _ in range(N)]


left = 0
right = 1e10
while right - left > 1:
    mid = (left + right) // 2

    ok = True
    t = [0] * N
    for i in range(N):
        if mid < h[i]:
            ok = False
        else:
            t[i] = (mid - h[i]) // s[i]
    t.sort()
    for i in range(N):
        if t[i] < i:
            ok = False
    if ok:
        right = mid
    else:
        left = mid

print(right)
