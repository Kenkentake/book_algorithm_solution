import math

A = int(input())
B = int(input())
C = int(input())

PI = math.acos(-1.0)

def func(t):
    return A * t + B * math.sin(C * PI * t)

alpha = 0
beta = 200
for _ in range(100):
    gamma = (alpha + beta) / 2
    if func(gamma) <= 100:
        alpha = gamma
    else:
        beta = gamma

print("{:.15f}".format(alpha))
