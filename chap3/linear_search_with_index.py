N = int(input())
v = int(input())
a = [int(input()) for _ in range(N)]

found_id = -1
for i in a:
    if i == v:
        found_id = i

print(found_id)
