N = int(input())
a = [int(input()) for _ in range(N)]
v = int(input())

count = 0
for i in range(N):
    if a[i] == v:
        count += 1

print(count)
