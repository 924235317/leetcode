def solve(board: list) -> None:
    def dfs(board, x, y):
        if x >= len(board[0]) or x < 0 or y >= len(board) or y < 0:
            return
        
        if board[y][x] == "X" or board[y][x] == "1":
            return
        elif board[y][x] == "O":
            board[y][x] = "*"
            dfs(board, x-1, y)
            dfs(board, x+1, y)
            dfs(board, x, y-1)
            dfs(board, x, y+1)
    
    if not board or not board[0]:
        return 
    h = len(board)
    w = len(board[0])

    for i in range(h):
        if i == 0 or i == h-1:
            for j in range(w):
                dfs(board, j, i)
        else:
            dfs(board, 0, i)
            dfs(board, w-1, i)

    for i in range(h):
        for j in range(w):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "*":
                board[i][j] = "O"
    #for i in range(h):
    #    for j in range(w):
    #        if board[i][j] == "*":
    #            board[i][j] = "O"
   
    
if __name__ == "__main__":
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    for i in range(len(board)):
        print(board[i])
    solve(board)
    print("------------------")
    for i in range(len(board)):
        print(board[i])
        
        
