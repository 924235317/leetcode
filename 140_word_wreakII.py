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


def wordBreak3(s: str, wordDict: list) -> list:
    def findPath(s, wordDict, cur, idx, dp, res):
        if idx < 0:
            return
        if idx == 0:
            res.append(cur)

        for word in wordDict:
            l = len(word)
            if idx - l >= 0 and dp[idx - l] and s[idx - l:idx] == word:

                tmp = word + " " + cur if cur != "" else word
                findPath(s, wordDict, tmp, idx - l, dp, res)
            

    if not s and not wordDict:
        return []

    if not s or not wordDict:
        return []
    
    dp = [False for i in range(len(s)+1)]
    dp[0] = True
    for i in range(len(s)):
        for word in wordDict:
            l = len(word)
            print(word, s[i-l+1:i+1], dp[i-l], i, i-l)
            if i-l+1 >= 0 and s[i-l+1:i+1] == word and dp[i-l+1]:
                dp[i+1] = True 
                break
    
    print(dp)
    if not dp[-1]:
        return []
    #cur = ""
    #res = []
    #findPath(s, wordDict, cur, len(dp) - 1, dp, res)
    #return res


if __name__ == "__main__":
    #s = "catsanddog"
    #wordDict = ["cat","cats","and","sand","dog"]
    #s = "bb"
    #wordDict = ["a", "b", "bbbbbb"]
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

    print(wordBreak3(s, wordDict))

