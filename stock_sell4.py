import numpy as np

def stock_sell4(k: int, prices: list) -> int:
    if len(prices) < 1:
        return 0
    
    days = len(prices)
    dp = [[[0, 0] for i in range(k+1)] for j in range(days)]
    
    for d in range(days):
        for _k in range(k, 0, -1):
            if d - 1 < 0:
                dp[d][_k][0] = 0
                dp[d][_k][1] = -prices[d]
            else:
                dp[d][_k][0] = max(dp[d-1][_k][0], dp[d-1][_k][1] + prices[d])
                dp[d][_k][1] = max(dp[d-1][_k][1], dp[d-1][_k-1][0] - prices[d])
    
    print(np.array(dp))
    return dp[days-1][k][0]


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4, 6]
    print(stock_sell4(3, prices))
