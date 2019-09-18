def exist(board: list, word: str) -> bool:
    def existCore(board: list, word: str, word_pos: int, maze: list, w: int, h: int, ) -> bool:
        if word_pos == len(word):
            return True

        if w >= len(maze[0]) or h >= len(maze) or w < 0 or h < 0 or board[h][w] != word[word_pos] or maze[h][w] == 1:
            return False

        maze[h][w] = 1
        print(maze)
        flag = False
        if board[h][w] == word[word_pos]:
            flag = existCore(board, word, word_pos+1, maze, w+1, h) or \
                   existCore(board, word, word_pos+1, maze, w-1, h) or \
                   existCore(board, word, word_pos+1, maze, w, h+1) or \
                   existCore(board, word, word_pos+1, maze, w, h-1)
                    
        maze[h][w] = 0
        return flag    
    
    if not board:
        return False

    if not board[0]:
        return False
    
    maze = [[0 for i in range(len(board[0]))] for j in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            res = existCore(board, word, 0, maze, j, i)
            if res:
                return res
    
    return False


if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(exist(board, word))


