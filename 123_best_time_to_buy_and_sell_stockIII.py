def maxProfit(prices: list) -> int:
    if len(prices) < 2:
        return 0

    dp = [[[0 for i in range(2)] for j in range(3)] for k in range(len(prices))]
    for i in range(len(prices)):
        for j in range(2, 0, -1):
            if i - 1 < 0:
                dp[i][j][0] = -prices[i]
            else:
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1]-prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0]+prices[i])
                
    return dp[-1][-1][1]


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))
