N = int(input())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(N)]

sum = 0
for i in range(N - 1, 0, -1):
    A[i] += sum
    amari = A[i] % B[i]
    D = 0
    if amari != 0:
        D = B[i] - amari
    sum += D

print(sum)