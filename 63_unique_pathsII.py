import numpy as np

def uniquePathsWithObstacles1(obstacleGrid: list) -> int:
    def uniquePathsWithObstaclesCore(obstacleGrid: list, target: list, w: int, h: int, count: list):
        if [h, w] == target:
            count.append(1)
            return

        next_w = w + 1
        next_h = h + 1

        obstacleGrid[h][w] = 1
        if next_w < len(obstacleGrid[0]):
            if obstacleGrid[h][next_w] != 1:
                uniquePathsWithObstaclesCore(obstacleGrid, target, next_w, h, count)
        if next_h < len(obstacleGrid):
            if obstacleGrid[next_h][w] != 1:
                uniquePathsWithObstaclesCore(obstacleGrid, target, w, next_h, count)
        obstacleGrid[h][w] = 0

    if obstacleGrid[0][0] == 1:
        return 0
    target = [len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1]
    count = list()
    uniquePathsWithObstaclesCore(obstacleGrid, target, 0, 0, count)
    return sum(count)

def uniquePathsWithObstacles(obstacleGrid: list) -> int:
    if len(obstacleGrid) < 1:
        return 0
        
    if len(obstacleGrid[0]) < 1:
        return 0    

    if obstacleGrid[0][0] == 1:
        return 0

    row, col = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0 for i in range(col)] for j in range(row)]
    dp[0][0] = 1
    
    for i in range(1, col):
        if obstacleGrid[0][i] != 1:
            dp[0][i] = dp[0][i-1]

    for h in range(1, row):
        for w in range(col):
            if obstacleGrid[h][w] == 1:
                dp[h][w] = 0
            else:
                if w == 0:
                    dp[h][w] = dp[h-1][w]
                else:
                    dp[h][w] = dp[h-1][w] + dp[h][w-1]

    return dp[row-1][col-1]
    

def print_ob(l):
    for ll in l:
        print(ll)

if __name__ == "__main__":
    #obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    #obstacleGrid = [[0]]
    obstacleGrid = [[0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],[1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1],[0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0],[1,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],[0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1],[1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1],[0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1],[1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]]
    print(uniquePathsWithObstacles(obstacleGrid))
    
