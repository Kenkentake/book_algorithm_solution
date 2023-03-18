K = abs(int(input()))

def func(N: int, cur: int, use: int, counter: int) -> int:
    if cur > N:
        return
    if use == 0b111:
        counter.append(1)
    func(N, cur*10+7, use | 0b001, counter)
    func(N, cur*10+5, use | 0b010, counter)
    func(N, cur*10+3, use | 0b100, counter)

counter = []
func(K, 0, 0, counter)
print(sum(counter))
