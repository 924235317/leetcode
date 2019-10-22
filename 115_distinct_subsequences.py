def numDistinct(s: str, t: str) -> int:
    if not s or not t:
        return 0

    l_s = len(s)
    l_t = len(t)
    dp = [[0 for i in range(l_s+1)] for j in range(l_t+1)]
    
    for i in range(l_s+1):
        dp[0][i] = 1

    for i in range(l_s):
        for j in range(l_t):
            dp[j+1][i+1] = dp[j+1][i]
            
            if s[i] == t[j]:
                dp[j+1][i+1] += dp[j][i]
    return dp[l_t][l_s]

if __name__ == "__main__":
    s = "rabbbit"
    t = "rabbit"

    print(numDistinct(s, t))
