def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    dev = 1
    while x // dev >= 10:
        dev *= 10

    while x:
        l = x // dev
        r = x % 10
        if l != r:
            return False

        x = x % dev
        x //= 10
        dev //= 100

    return True

if __name__ == "__main__":
    x = 121
    print(isPalindrome(x))



