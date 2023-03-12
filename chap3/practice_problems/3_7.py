N = int(input())
S = "".join([str(input()) for _ in range(N)])

res = 0
for bit in range(1 << N-1):
    tmp = 0
    for i in range(N-1):
        tmp *= 10
        tmp += int(S[i])
        if bit & (1 << i):
            res += tmp
            tmp = 0

    tmp *= 10
    tmp += int(S[-1])
    res += tmp
            
print(res)
