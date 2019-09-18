def reverse(x: int) -> int:
    
    tmp = x if x > 0 else -x
    res = 0
    while tmp:
        res *= 10
        res += tmp % 10
        tmp //= 10
    res = res if x > 0 else -res
    return res if -(2**31) <= res <= 2**31 else 0

if __name__ == "__main__":
    x = -102
    print(reverse(x))
