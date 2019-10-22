# time outof limit
def wordBreak(s: str, wordDict: list) -> list:
    def wordBreakCore(s, wordDict, tmp, res):
        if not s:
            if tmp:
                res.append(" ".join(tmp))
            return

        for word in wordDict:
            l = len(word)
            if s[:l] == word:
                tmp.append(s[:l])
                wordBreakCore(s[l:], wordDict, tmp, res)
                tmp.pop(-1)
        
    res = list()
    tmp = list()

    wordBreakCore(s, wordDict, tmp, res)
    return res


def wordBreak2(s: str, wordDict: list) -> list:
    if not s and not wordDict:
        return True

    if not s or not wordDict:
        return False

    dp = [[] for i in range(len(s)+1)]
    for i in range(len(s)):
        for word in wordDict:
            l = len(word)
            if i-l+1 > 0 and s[i-l+1:i+1] == word and len(dp[i-l+1]) > 0:
                tmp = [t+" "+word for t in dp[i-l+1]]
                dp[i+1] += tmp 
            elif i-l+1 == 0 and s[i-l+1:i+1] == word:
                dp[i+1] += [word] 

    return dp[-1]


if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    print(wordBreak2(s, wordDict))

