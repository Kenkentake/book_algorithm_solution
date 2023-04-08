from typing import TypeVar, List, Tuple

T = TypeVar('T')
Pair = Tuple[T, T]

Interval = Pair[int]

first = 0
second = 1

def cmp(val: Interval) -> int:
    return val[second]

N = int(input())
inter: List[Interval] = [(int(input()), int(input())) for _ in range(N)]

inter = sorted(inter, key=cmp)

res = 0
current_end_time = 0

for i in range(N):
    if (inter[i][first] < current_end_time):
        continue
    res += 1

    current_end_time = inter[i][second]

print(res)