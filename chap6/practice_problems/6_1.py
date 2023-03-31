import bisect

N = int(input())
a = [int(input()) for _ in range(N)]

b = sorted(a)

res = []
for i in a:
    res.append(bisect.bisect(b, i))

print(res)
