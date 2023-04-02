import bisect

N = int(input())
p = [int(input()) for _ in range(N)] 
M = int(input())


s = []
for i in p:
    for j in p:
        p.append(i+j)

s.sort()

res = 0
for a in s:
    it = bisect.bisect_right(s, M - a)
    if it == 0:
        continue
    it -= 1
    res = max(res, a + s[it])

print(res)
