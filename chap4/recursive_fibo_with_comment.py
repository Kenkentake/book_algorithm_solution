def fibo_with_comment(N: int) -> int:
    print(f"fibo({N})を呼び出しました")
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        result = fibo_with_comment(N - 1) + fibo_with_comment(N - 2)
        print(f"{N}項目 = {result}")
        return result

print(fibo_with_comment(6))
