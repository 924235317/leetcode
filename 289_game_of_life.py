def gameOfLife(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if not board or not board[0]:
        return 
    w = len(board[0])
    h = len(board)
    
    tmp = [[0 for i in range(w + 1)] for j in range(h + 1)]
    
    for hh in range(1, h + 1):
        for ww in range(1, w + 1):
            if hh == 0 and ww == 0:
                tmp[hh][ww] = board[hh - 1][ww - 1]
            elif hh == 0:
                tmp[hh][ww] = tmp[hh][ww - 1] + board[hh - 1][ww - 1]
            elif ww == 0:
                tmp[hh][ww] = tmp[hh - 1][ww] + board[hh - 1][ww - 1]
            else:
                tmp[hh][ww] = tmp[hh][ww - 1] + tmp[hh - 1][ww] - tmp[hh - 1][ww - 1] + board[hh - 1][ww - 1]
    
    for hh in range(1, h  + 1):
        for ww in range(1, w + 1):
            min_w = max(0, ww - 2)
            min_h = max(0, hh - 2)
            max_w = min(w, ww + 1)
            max_h = min(h, hh + 1)
            
            val = tmp[max_h][max_w] - tmp[min_h][max_w] - tmp[max_h][min_w] + tmp[min_h][min_w] - board[hh - 1][ww - 1]   
            if board[hh - 1][ww - 1] == 1 and (val < 2 or val > 3):
                board[hh - 1][ww - 1] = 0
            elif board[hh - 1][ww - 1] == 0 and val == 3:
                board[hh - 1][ww - 1] = 1

def gameOfLife2(board) -> None:
    if not board or not board[0]:
            return 
        w = len(board[0])
        h = len(board)
        for hh in range(h):
            for ww in range(w):
                tmp = 0
                if hh == 0 and ww == 0:
                    # print(1)
                    tmp = board[hh][ww]
                elif hh == 0:
                    # print(2)
                    tmp = board[hh][ww - 1] // 10 + board[hh][ww]
                elif ww == 0:
                    # print(3)
                    tmp = board[hh - 1][ww]  // 10 + board[hh][ww]
                else:
                    tmp = board[hh][ww - 1] // 10 + board[hh - 1][ww] // 10 - board[hh - 1][ww - 1] // 10 + board[hh][ww]
                # print("bb", hh, ww, tmp, board[hh][ww])
                board[hh][ww] = tmp  * 10 + board[hh][ww]
                # print(tmp, board[hh][ww])
        
        # print(board)
        
        for hh in range(h):
            for ww in range(w):
                max_w = min(w - 1, ww + 1)
                max_h = min(h - 1, hh + 1)
                min_h = hh - 2
                min_w = ww - 2
                if min_h < 0 and min_w < 0:
                    val = board[max_h][max_w] // 10
                elif min_h < 0:
                    val = board[max_h][max_w] // 10 - board[max_h][min_w] // 10
                elif min_w < 0:
                    val = board[max_h][max_w] // 10 - board[min_h][max_w] // 10
                else:
                    val = board[max_h][max_w] // 10 - board[min_h][max_w] // 10 - board[max_h][min_w] // 10 + board[min_h][min_w] // 10

                cur_state = board[hh][ww] % 10
                val -= cur_state

                if cur_state == 1 and (val < 2 or val > 3):
                    board[hh][ww] = board[hh][ww] // 10 * 10
                elif cur_state == 0 and val == 3:
                    board[hh][ww] = board[hh][ww] // 10 * 10 + 1

        for hh in range(h):
            for ww in range(w):
                board[hh][ww] = board[hh][ww] % 10
                
