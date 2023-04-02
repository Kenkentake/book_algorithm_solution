import bisect

N = int(input())
a = [int(input()) for _ in range(N)]
b = [int(input()) for _ in range(N)]
K = int(input())

b.sort()

def check(x: int) -> bool:
    count = 0
    for i in a:
        count += bisect.bisect_right(b, x // i)
    return count >= K

left = 0
right = 1 << 10
while right - left > 1:
    mid = (right + left) // 2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)
