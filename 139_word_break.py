def wordBreak(s: str, wordDict: list) -> bool:
    if not s and not wordDict:
        return True

    if not s or not wordDict:
        return False

    dp = [False for i in range(len(s)+1)]
    dp[0] = True
    for i in range(len(s)):
        for word in wordDict:
            l = len(word)
            if i-l+1 >= 0 and s[i-l+1:i+1] == word \
                and dp[i-l+1]:
                dp[i+1] = True
                break

    return dp[-1]


if __name__ == "__main__":
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(wordBreak(s, wordDict))
                
