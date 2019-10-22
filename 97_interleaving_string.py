def isInterleave(s1: str, s2: str, s3: str) -> bool:
    def isInterleaveCore(s1, s2, s3):
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        if not s1 and not s2 and not s3:
            return True
        elif not s3:
            return False

        flag1 = False
        if l1 > 0 and s1[0] == s3[0]:
            flag1 = isInterleaveCore(s1[1:], s2, s3[1:])

        flag2 = False
        if l2 > 0 and s2[0] == s3[0]:
            flag2 = isInterleaveCore(s1, s2[1:], s3[1:])

        return flag1 or flag2
    
    return isInterleaveCore(s1, s2, s3)

def isInterleave1(s1: str, s2: str, s3: str) -> bool:
    def isInterleaveCore(s1, i, s2, j, s3, k, dic):
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        key = i * l3 + j
        if key in dic:
            return False
        if i == l1:
            return s2[j:] == s3[k:]
        if j == l2:
            return s1[i:] == s3[k:]
        if (s1[i] == s3[k] and isInterleaveCore(s1, i+1, s2, j, s3, k+1, dic)) \
            or (s2[j] == s3[k] and isInterleaveCore(s1, i, s2, j+1, s3, k+1, dic)):
            return True

        dic.append(key)
        return False
    
    dic = list()
    return isInterleaveCore(s1, 0, s2, 0, s3, 0, dic)

if __name__ == "__main__":
    #s1 = "aabcc"
    #s2 = "dbbca"
    #s3 = "aadbbcbcac"
    s1 = "abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb"
    s2 = "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc"
    s3 = "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"

    print(isInterleave1(s1, s2, s3))
                
