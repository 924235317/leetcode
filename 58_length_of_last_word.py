def lengthOfLastWord(s: str) -> int:
    if len(s) < 1:
        return 0

    length = len(s)
    idx1 = -1
    for i in range(length-1, -1, -1):
        if s[i] != " ":
            idx1 = i
            break
    idx2 = -1
    for j in range(idx1, -1, -1):
        if s[j] == " ":
            idx2 = j
            break

    if idx2 == -1:
        return idx1 + 1
    else:
        return idx1 - idx2 

if __name__ == "__main__":
    s = "a bcd "
    print(lengthOfLastWord(s))
