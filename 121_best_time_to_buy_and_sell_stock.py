def maxProfit(prices: list) -> int:
    if len(prices) < 1:
        return 0

    # day, num of transaction, hold(0: hold, 1: sell)
    dp = [[[0 for i in range(2)] for j in range(2)] for k in range(len(prices))]
    dp[0][0][0] = -prices[0]
    dp[0][1][0] = -prices[0]
    for k in range(1, len(prices)):
        for j in range(1, 0, -1):
            dp[k][j][0] = max(dp[k-1][j][0], dp[k-1][j-1][1]-prices[k])      
            dp[k][j][1] = max(dp[k-1][j][1], dp[k-1][j][0]+prices[k])      
    
    print(dp)
    return dp[-1][1][1]

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))

