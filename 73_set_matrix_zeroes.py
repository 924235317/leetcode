def setZeroes(matrix: list) -> None:
    row, col = len(matrix), len(matrix[0])

    row_flag = False
    col_flag = False
    for i in range(row):
        if matrix[i][0] == 0:
            row_flag = True
            break

    for i in range(col):
        if matrix[0][i] == 0:
            col_flag = True
            break

    for h in range(1, row):
        for w in range(1, col):
            if matrix[h][w] == 0:
                matrix[0][w] = 0
                matrix[h][0] = 0
    
    for h in range(1, row):
        for w in range(1, col):
            if matrix[0][w] == 0 or matrix[h][0] == 0:
                matrix[h][w] = 0

    if row_flag:
        for i in range(row):
            matrix[i][0] = 0

    if col_flag:
        for i in range(col):
            matrix[0][i] = 0

if __name__ == "__main__":
    matrix =[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

    setZeroes(matrix)
    print(matrix)
