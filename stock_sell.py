import numpy as np

def stock_sell(prices: list) -> int:
    if len(prices) < 1:
        return 0

    dp = np.zeros((len(prices), 2, 2), dtype=np.int8)
    dp[0, 0, 0] = 0
    dp[0, 0, 1] = -prices[0]
    dp[0, 1, 0] = 0
    dp[0, 1, 1] = -prices[0]

    for d in range(1, len(prices)):
        for k in range(1, 0, -1):
            dp[d, k, 0] = max(dp[d-1, k, 0], dp[d-1, k, 1] + prices[d])
            dp[d, k, 1] = max(dp[d-1, k, 1], dp[d-1, k-1, 0] - prices[d])

    print(dp)
    return dp[len(prices)-1, 1, 0]

if __name__ == "__main__":
    print(stock_sell([7, 1, 5, 3, 6, 4]))
