def mySqrt(x: int) -> int:
    l = 0
    r = x // 2
    while l <= r:
        m = (l + r) // 2 + 1
        print(m)
        tmp = m * m
        if tmp < x:
            l = m + 1
        elif tmp > x:
            r = m - 1
        else:
            return m

    if l * l > x:
        return l - 1
    else:
        return l
    return l


if __name__ == "__main__":
    x = 8
    print(mySqrt(x))
