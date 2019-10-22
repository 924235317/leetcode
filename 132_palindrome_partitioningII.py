
# time outof limit
def minCut(s: str) -> int:
    def isPalindrome(s):
        return s == s[::-1]

    def Core(s, cur_cut, min_cut):
        if not s:
            return cur_cut-1

        for i in range(len(s)):
            if isPalindrome(s[:i+1]):
                min_cut = min(Core(s[i+1:], cur_cut+1, min_cut), min_cut)

        return min_cut
    
    min_cut = len(s)
    cur_cut = 0
    return Core(s, cur_cut, min_cut)

def minCut2(s: str) -> int:
    def isPalindrome(s):
        return s == s[::-1]
    
    dp = [0 for i in range(len(s)+1)]
    dp[0] = -1

    for i in range(1, len(s)+1):
        min_cut = len(s)
        for j in range(i):
            print(j, i, s[j:i])
            if isPalindrome(s[j:i]):
                min_cut = min(dp[j]+1, min_cut)
        dp[i] = min_cut

    return dp[-1]


def minCut3(s: str) -> int:
    length = len(s)
    min_cuts = [length for i in range(length+1)]
    min_cuts[0] = -1
    dp = [[False for i in range(length+1)] for j in range(length+1)]

    for i in range(1, length+1):
        for j in range(i-1, -1, -1):
            print(j, i)
            if s[i-1] == s[j] and (i-j-1 < 2 or dp[i-1][j+1]):
                print(1)
                dp[i][j] = True
                min_cuts[i] = min(min_cuts[j]+1, min_cuts[i])

    print(dp)
    return min_cuts[-1]


if __name__ == "__main__":
    #s = "ababababababababababababcbabababababababababababa"
    s = "a"
    print(minCut3(s))
