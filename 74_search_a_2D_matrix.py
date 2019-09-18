def searchMatrix(matrix: list, target: int) -> bool:
    if len(matrix) < 1:
        return False
    if len(matrix[0]) < 1:
        return False
    row, col = len(matrix), len(matrix[0])
    total_nums= row * col - 1
    print(total_nums)

    left = 0
    right = total_nums 
    while left <= right:
        m = (left + right) // 2
        r = m // col
        c = m % col
        if target > matrix[r][c]:
            left = m + 1
        elif target < matrix[r][c]:
            right = m - 1
        else:
            return True


    return False


if __name__ == "__main__":
    matrix = [[1, 3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]]
    target = 3
    print(matrix)
    print(searchMatrix(matrix, target))
