def divide(dividend:int, divisor: int) -> int:
    sign = 1
    INT_MAX = 2 ** 31
    INT_MIN = -2 ** 31 -1
    if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
        sign = -1

    if divisor == 0:
        return INT_MAX if dividend > 0 else INT_MIN

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX
    
    if dividend == 0:
        return 0

    a = abs(dividend)
    b = abs(divisor)
    res = 0
    
    while a >= b:
        shift = 0
        while a >= b << shift:
            shift += 1

        a -= b << shift - 1
        res += 1 << shift - 1

    return res * sign


if __name__ == "__main__":
    print(2 ** 31)
    print(divide(10, 3))
