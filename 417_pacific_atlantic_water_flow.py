def pacificAtlantic(matrix):
    def dfs(matrix, memo, w, h, edge_w, edge_h, pre_val):
        print(w, h ,edge_w, edge_h)
        if not (0 <= w <= edge_w) or not (0 <= h <= edge_h) or memo[h][w] == 1:
            return
        
        if matrix[h][w] < pre_val:
            memo[h][w] = 0
            return
        
        memo[h][w] = 1
        dfs(matrix, memo, w - 1, h, edge_w, edge_h, matrix[h][w])
        dfs(matrix, memo, w + 1, h, edge_w, edge_h, matrix[h][w])
        dfs(matrix, memo, w, h - 1, edge_w, edge_h, matrix[h][w])
        dfs(matrix, memo, w, h + 1, edge_w, edge_h, matrix[h][w])

    
    if not matrix or not matrix[0]:
        return []

    h = len(matrix)
    w = len(matrix[0])
    memo_p = [[-1 for i in range(w)] for j in range(h)]
    memo_a = [[-1 for i in range(w)] for j in range(h)]

    for ww in range(w):
        memo_p[0][ww] = -1
        memo_a[h - 1][ww] = -1
        dfs(matrix, memo_p, ww, 0, w - 1, h - 1, -1)
        dfs(matrix, memo_a, ww, h - 1, w - 1, h - 1, -1)

    for hh in range(h):
        memo_p[hh][0] = -1
        memo_a[hh][w - 1] = -1
        dfs(matrix, memo_p, 0, hh, w - 1, h - 1, -1)
        dfs(matrix, memo_a, w - 1, hh, w - 1, h - 1, -1)

    res = list()
    for ww in range(w):
        for hh in range(h):
            if memo_p[hh][ww] == 1 and memo_a[hh][ww] == 1:
                print(ww, hh, memo_p[hh][ww], memo_a[hh][ww])
                res.append([hh, ww])
    
    for i in range(h):
        print(memo_p[i])

    print()
    for i in range(h):
        print(memo_a[i])
        
    return res


if __name__ == "__main__":
    #matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    matrix = [[1,2],[4,3]]
    print(pacificAtlantic(matrix))

