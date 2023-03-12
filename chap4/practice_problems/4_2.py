N = int(input())

if N < 3:
    a = [0, 0, 1]
else:
    a = [-1] * (N + 1)
    a[0] = 0
    a[1] = 0
    a[2] = 1

def func(N: int) -> int:
    if a[N] != -1:
        return a[N]
    else:
        a[N] = func(N - 1) + func(N - 2) + func(N - 3)
        return a[N]

ans = func(N)
print(ans)
