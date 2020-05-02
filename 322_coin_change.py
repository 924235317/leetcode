def coinChange(coins, amount):
    if not coins or amount < 0:
        return -1

    dp = [2**31 for i in range(amount + 1)]

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i - coin] + 1, dp[i])

    return dp[-1]


