def isValidSudoku(board):
    used_row = [[False for _ in range(9)] for _ in range(9)]
        used_col = [[False for _ in range(9)] for _ in range(9)]
        used = [[False for _ in range(9)] for _ in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    num = int(board[row][col]) - 1
                    n = row // 3 * 3 + col // 3

                    if used_row[row][num] or used_col[col][num] or used[n][num]:
                        return False

                    used_row[row][num] = used_col[col][num] = used[n][num] = True
        return True



