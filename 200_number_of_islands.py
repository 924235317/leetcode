def numIslands(grid: list) -> int:
    def fill(grid, w, h, visited, move):
        grid_w = len(grid[0])
        grid_h = len(grid)

        visited[h][w] = True
        for m in move:
            next_w = w + m[0]
            next_h = h + m[1]
            if 0 <= next_w < grid_w and 0 <= next_h < grid_h \
                and not visited[next_h][next_w] and grid[next_h][next_w] == "1":
                fill(grid, next_w, next_h, visited, move)

    
    if not grid or not grid[0]:
        return 0

    move = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    grid_w = len(grid[0])
    grid_h = len(grid)
    res = 0
    visited = [[False for i in range(grid_w)] for j in range(grid_h)]
    for h in range(grid_h):
        for w in range(grid_w):
            if grid[h][w] == "1" and not visited[h][w]:
                res += 1
                fill(grid, w, h, visited, move)

    return res


if __name__ == "__main__":
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(numIslands(grid))

