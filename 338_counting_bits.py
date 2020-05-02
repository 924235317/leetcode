def countBits(num: int):
    
    if num <= 0:
        return []

    dp = [0 for i in range(num + 1)]
    next_e = 0
    for i in range(1, num + 1):
        if i == 2 ** next_e:
            dp[i] = 1
            next_e += 1
        else:
            cur_val = 2 ** (next_e - 1)
            dp[i] = dp[cur_val] + dp[i - cur_val]

    return dp[1:]

if __name__ == "__main__":
    print(countBits(10))
