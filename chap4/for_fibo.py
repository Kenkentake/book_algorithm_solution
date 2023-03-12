N = 50
F = [0, 1]

for n in range(2, N+1):
    F.append(F[n - 1] + F[n - 2])
    print(f"{n}項目: {F[n]}")
