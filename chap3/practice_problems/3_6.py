K = int(input())
N = int(input())

count = 0
for i in range(min(K, N)+1):
    for j in range(min(K, N)+1):
        x = i
        y = j
        z = N - x - y
        if 0 <= z <= K:
            count += 1

print(count)
