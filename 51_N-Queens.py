from copy import deepcopy
def solveNQueens(n: int) -> list:
    def check(board, x, y, n):
        for j in range(y):
            if board[j][x] == "Q":
                return False

            if x-j-1 >= 0 and board[y-j-1][x-j-1] == "Q":
                return False

            if x+j+1 < n and board[y-j-1][x+j+1] == "Q":
                return False

        return True

    def solveNQueensCore(y, n, board, res):
        if y >= n:
            res.append(["".join(i) for i in board])
            return True

        for x in range(n):
            if check(board, x, y, n):
                board[y][x] = "Q"
                solveNQueensCore(y+1, n, board, res)
                board[y][x] = "."
        return False

    board = [["." for i in range(n)]  for j in range(n)]
    print(board)
    res = list()
    solveNQueensCore(0, n, board, res)

    return res


def print_board(board):
    print(len(board))
    for b in board:
        print("====================")
        for bb in b:
            print(bb)
        print("====================")



if __name__ == "__main__":
    n = 4
    print_board(solveNQueens(n))





