import bisect

N = int(input())
a = [int(input()) for _ in range(N)]
b = [int(input()) for _ in range(N)]
c = [int(input()) for _ in range(N)]


a.sort()
b.sort()
c.sort()

res = 0
for i in b:
    res += bisect.bisect_left(a, i) * (N - bisect.bisect_right(c, i))

print(res)
