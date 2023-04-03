class BIT:
    def __init__(self, n):
        self.n = n
        self.dat = [0] * (n + 1)

    def add(self, i, x):
        while i <= self.n:
            self.dat[i] += x
            i += i & -i

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.dat[i]
            i -= i & -i
        return res

    def sum_range(self, l, r):
        return self.sum(r - 1) - self.sum(l - 1)

N = int(input())
a = list(map(int, input().split()))
low, high = 0, 1 << 30
geta = N + 1

while high - low > 1:
    mid = (low + high) // 2
    num = 0
    bit = BIT(N * 2 + 10)
    s = 0
    bit.add(s + geta, 1)

    for i in range(N):
        if a[i] <= mid:
            s += 1
        else:
            s -= 1
        num += bit.sum_range(1, s + geta)
        bit.add(s + geta, 1)
    
    if num > (N + 1) * N / 2 / 2:
        high = mid
    else:
        low = mid

print(high)
