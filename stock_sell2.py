
def stock_sell2(prices: list) -> int:
    if len(prices) < 1:
        return 0
    days = len(prices)
    dp = [[0, 0] for i in range(days)]
    
    for d in range(days):
        if d - 1 < 0:
            dp[d][0] = 0
            dp[d][1] = -prices[d]
        else:
            dp[d][0] = max(dp[d-1][0], dp[d-1][1] + prices[d])
            dp[d][1] = max(dp[d-1][1], dp[d-1][0] - prices[d])

    print(dp)
    return dp[days-1][0]


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(stock_sell2(prices))
