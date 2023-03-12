N = int(input())

def func(N: int) -> int:
    if N == 0 or N == 1 :
        return 0
    elif N == 2:
        return 1
    return  func(N - 1) + func(N - 2) + func(N - 3)

ans = func(N)
print(ans)
