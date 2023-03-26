import bisect

N = int(input())
a = [int(input()) for _ in range(N)]
b = [int(input()) for _ in range(N)]
K = int(input())

min_value = 2e10
b.sort()
b.append(2e10)

for i in range(N):
    index = bisect.bisect_left(b, K - a[i])
    val = b[index]
    if a[i] + val < min_value:
        min_value = a[i] + val

print(min_value)
