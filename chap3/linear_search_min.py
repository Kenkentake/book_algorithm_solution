N = int(input())
a = [int(input()) for _ in range(N)]

min_value = 2e10
for i in a:
    if i < min_value:
        min_value = i

print(min_value)
