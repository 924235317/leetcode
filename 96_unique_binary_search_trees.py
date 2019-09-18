def numTrees(n: int) -> int:
    if n <= 1:
        return 1

    dp = [0 for i in range(n+1)]
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        for j in range(1, i+1):
            dp[i] += dp[j-1] * dp[i-j]

    print(dp)
    return dp[-1]

if __name__ == "__main__":
    n = 5
    print(numTrees(n))
