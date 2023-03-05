N = int(input())
a = [int(input()) for _ in range(N)]

min_value = 2e10
max_value = -2e10
for i in range(N):
    if a[i] < min_value:
        min_value = a[i]
    elif a[i] > max_value:
        max_value = a[i]

print(int(max_value - min_value))
