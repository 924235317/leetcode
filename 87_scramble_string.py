def isScramble(s1: str, s2: str) -> bool:
    if not s1 and not s2:
        return True

    if not s1 or not s2 or len(s1) != len(s2):
        return False

    if len(s1) == 1 and len(s2) == 1:
        return s1 == s2

    dic = dict()
    l = len(s1)
    for i in range(l):
        if s1[i] not in dic:
            dic[s1[i]] = 0
        dic[s1[i]] += 1

    for i in range(len(s2)):
        if s2[i] not in dic:
            return False
        dic[s2[i]] -= 1

    for i in dic.values():
        if i != 0:
            return False


    for i in range(1, l):
        if (isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:])) \
            or (isScramble(s1[:i], s2[l-i:]) and isScramble(s1[i:], s2[:l-i])):
            return True
    return False


if __name__ == "__main__":
    s1 = "great"
    s2 = "eatgr" 
    print(isScramble(s1, s2))

