N = int(input())
K = int(input())
a = [int(input()) for _ in range(N)]
b = [int(input()) for _ in range(N)]

min_value = 2e10
for i in a:
    for j in b:
        pair = i + j
        if K < pair and pair < min_value:
            min_value = pair

print(min_value)
