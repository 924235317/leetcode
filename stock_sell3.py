import numpy as np

def stock_sell3(prices: list) -> int:
    if len(prices) < 1:
        return 0

    days = len(prices)
    dp = [[[0, 0] for i in range(3)] for j in range(days)]

    for d in range(days):
        for k in range(2, 0, -1):
            if d - 1 < 0:
                dp[d][k][0] = 0
                dp[d][k][1] = -prices[d]
            else:
                dp[d][k][0] = max(dp[d-1][k][0], dp[d-1][k][1] + prices[d])
                dp[d][k][1] = max(dp[d-1][k][1], dp[d-1][k-1][0] - prices[d])
    
    print(np.array(dp))
    return dp[days-1][2][0]


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(stock_sell3(prices))
