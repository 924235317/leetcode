def maxProfit(k, prices) -> int:
    if not prices:
        return 0
    
    days = len(prices)
	
    if k >= days // 2:
        return sum(
            x - y
            for x, y in zip(prices[1:], prices[:-1])
            if x > y)

    dp = [[0 for i in range(2)] for j in range(k + 1)]
    
    for day in range(0, days + 1):
        for kk in range(k, -1, -1):
            if kk == 0:
                dp[kk][1] = -2**31
                continue
            if day == 0:
                dp[kk][1] = -2**31
                continue
            
            dp[kk][0] = max(dp[kk][1] + prices[day - 1], dp[kk][0])
            dp[kk][1] = max(dp[kk - 1][0] - prices[day - 1], dp[kk][1])

    
    return dp[-1][0]


if __name__ == "__main__":
    prices = [2, 4, 1]
    k = 2
    print(maxProfit(k, prices))
