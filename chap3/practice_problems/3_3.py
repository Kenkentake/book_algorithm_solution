N = int(input())
if N < 2:
    exit("input an integer greater than or equal to 2")
a = [int(input()) for _ in range(N)]

first_min_value = 2e10
second_min_value = 2e10
for i in range(N):
    if a[i] < first_min_value:
        second_min_value = first_min_value
        first_min_value = a[i]
    elif a[i] < second_min_value:
        second_min_value = a[i]

print(second_min_value)
