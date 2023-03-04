import time

N = int(input())
count = 0
start_time = time.time()
for i in range(N):
    for j in range(N):
        count += 1
print(time.time() - start_time)
