def numDecodings(s: str) -> int:
    length = len(s)
    if length == 0:
        return length
    if length == 1:
        return 0 if s[0] == "0" else 1

    dp = [0] * (length + 1)
    dp[0] = 1 
    dp[1] = 1 if "0" < s[0] <= "9" else 0
    
    for i in range(2, length+1):
        if "0" < s[i-1] <= "9":
            dp[i] += dp[i-1]
        if "09" < s[i-2:2] < "27":
            dp[i] += dp[i-2]

    print(dp)
    return dp[length]



if __name__ == "__main__":
    s = "17"
    print(numDecodings(s))
