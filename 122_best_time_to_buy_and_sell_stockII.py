def maxProfit(prices: list) -> int:
    if len(prices) < 2:
        return 0

    dp = [[0 for i in range(2)] for k in range(len(prices))]
    dp[0][0] = -prices[0]
    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])

    return dp[-1][1]


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))
