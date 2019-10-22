def isMatch(s: str, p: str) -> bool:
    if not s and not p:
        return True

    if not p:
        return False

    if s and (p[0] == "?" or s[0] == p[0]):
        return isMatch(s[1:], p[1:])
    elif p[0] == "*":
        if not s:
            return isMatch(s, p[1:])
        return isMatch(s[1:], p[1:]) or isMatch(s[1:], p) or isMatch(s, p[1:])
    else:
        return False


def isMatch2(s: str, p: str) -> bool:
    l_s = len(s)
    l_p = len(p)

    
    dp = [[False for i in range(l_s+1)] for j in range(l_p+1)]

    dp[0][0] = True 
    for i in range(1, l_p+1):
        if p[i-1] == "*":
            dp[i][0] = dp[i-1][0]

    for w in range(1, l_s+1):
        for h in range(1, l_p+1):
            if p[h-1] == "*":
                dp[h][w] = dp[h-1][w] or dp[h-1][w-1] or dp[h][w-1]
            elif p[h-1] == s[w-1] or p[h-1] == "?":
                dp[h][w] = dp[h-1][w-1]
    return dp[-1][-1]


if __name__ == "__main__":
    s = "abcd"
    p = "?b*d"
    #print(isMatch(s, p))
    print(isMatch2(s, p))
        
    

