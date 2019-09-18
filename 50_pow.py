def myPow(x: float, n: int) -> float:
    m = -n if n < 0 else n

    p = 1
    while m:
        if m & 1:
            p *= x

        x *= x
        m >>= 1
    
    return p if n >= 0 else 1/p

if __name__ == "__main__":
    x = 2
    n = 7

    print(myPow(x, n))
