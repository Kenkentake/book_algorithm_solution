from typing import List


def func(i: int, w: int, a: List[int]):
    if i == 0:
        if w == 0:
            return True
        else:
            return False
    if memo[i][w] != -1:
        return bool(memo[i][w])
    if func(i - 1, w, a):
        memo[i][w] = 1
        return True
    if func(i - 1, w - a[i - 1], a):
        memo[i][w] = 1
        return True
    else:
        memo[i][w] = 0
        return False

N = int(input())
a = [int(input()) for _ in range(N)]
W = int(input())

memo = [[-1]*(W+1) for _ in range(N+1)]
if func(N, W, a):
    print("Yes")
else:
    print("No")
