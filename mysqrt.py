
def mySqrt(x: int) -> int:
    if x == 0:
        return 0

    if x == 1:
        return 1

    left = 0
    right = x // 2
    mid = (left + right + 1) // 2
    while left < right:
        mid = (right + left + 1) // 2
        if mid**2 > x:
            right = mid - 1
        elif mid**2 < x:
            left = mid
        else:
            return int(mid)

    return int(left)

if __name__ == "__main__":
    print(mySqrt(10))
