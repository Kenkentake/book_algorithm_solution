N = int(input())
v = int(input())
a = [int(input()) for _ in range(N)]

flag = False
for i in a:
    if i == v:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
