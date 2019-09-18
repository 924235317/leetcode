def minPathSum(grid: list) -> int:
    if len(grid) < 1:
        return 0
    if len(grid[0]) < 1:
        return 0
    
    row, col = len(grid), len(grid[0])

    dp = [[0 for i in range(col)] for j in range(row)]
    dp[0][0] = grid[0][0]
    for w in range(1, col):
        dp[0][w] = dp[0][w-1] + grid[0][w]

    for h in range(1, row):
        for w in range(col):
            if w == 0:
                dp[h][w] = grid[h][w] + dp[h-1][w]
            else:
                dp[h][w] = grid[h][w] + min(dp[h-1][w], dp[h][w-1])

    return dp[row-1][col-1]

if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(minPathSum(grid))

                
