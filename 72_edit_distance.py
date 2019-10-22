def minDistance(word1: str, word2: str) -> int:

    l1 = len(word1)
    l2 = len(word2)
    dp = [[0 for i in range(l2+1)] for j in range(l1+1)]

    for i in range(l1+1):
        dp[i][0] = i
    for i in range(l2+1):
        dp[0][i] = i

    for i in range(1, l1+1):
        for j in range(1, l2+1):

            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1],
                               dp[i-1][j],
                               dp[i][j-1]) + 1 #replace, add, delete
    return dp[-1][-1]
    

def minDistance2(word1, word2):
    l1 = len(word1)
    l2 = len(word2)

    dp = [i for i in range(l2+1)]

    for i in range(1, l1+1):
        pre = dp[0]
        dp[0] = i
        for j in range(1, l2+1):
            tmp = dp[j]
            if word1[i-1] != word2[j-1]:
                dp[j] = min(dp[j-1], dp[j], pre) + 1
            else:
                dp[j] = pre
    
            pre = tmp
    return dp[-1]

if __name__ == "__main__":
    word1 = "abcde"
    word2 = "acdd"
    print(minDistance(word1, word2))
    print(minDistance2(word1, word2))
