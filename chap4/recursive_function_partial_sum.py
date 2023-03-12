from typing import List


def func(i: int, w: int, a: List[int]):
    if i == 0:
        if w == 0:
            return True
        else:
            return False
    if func(i - 1, w, a):
        return True
    if func(i - 1, w - a[i - 1], a):
        return True
    else:
        return False


N = int(input())
a = [int(input()) for _ in range(N)]
W = int(input())

if func(N, W, a):
    print("Yes")
else:
    print("No")
