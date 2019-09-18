def reverseString(s:list) -> None:
    if len(s) <= 1:
        return

    l = 0
    r = len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    reverseString(s)
    print(s)
