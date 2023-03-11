N = int(input())
a = [int(input()) for _ in range(N)]

count = 0
flag = True
while flag:
    for i in range(N):
        if a[i] % 2 != 0:
            flag = False
        a[i] = a[i] / 2
    if flag:
        count += 1

print(count)
