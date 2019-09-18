def spiralOrder(matrix: list) -> list:
    if len(matrix) < 1 or len(matrix[0]) < 0:
        return []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    res = list()
    while left <= right and top <= bottom:
        for i in range(left, right+1):
            res.append(matrix[top][i])
        for j in range(top+1, bottom+1):
            res.append(matrix[j][right])
        for i in range(right-1, left-1, -1):
            if top < bottom:
                res.append(matrix[bottom][i])
        for j in range(bottom-1, top, -1):
            if left < right:
                res.append(matrix[j][left])
        top += 1
        bottom -= 1
        right -= 1
        left += 1
    return res


if __name__ == "__main__":
    matrix =[[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    matrix1 =[[1,2,3], [4,5,6], [7,8,9]]
    matrix2 =[[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]]
    matrix3 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    matrix4 = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
    matrix5 = [[3], [2]]
    matrix6 = [[1, 2], [3, 4]]
    print("---------------------------------------")
    print(matrix)
    print(spiralOrder(matrix))
    print("---------------------------------------")
    print(matrix1)
    print(spiralOrder(matrix1))
    print("---------------------------------------")
    print(matrix2)
    print(spiralOrder(matrix2))
    print("---------------------------------------")
    print(matrix3)
    print(spiralOrder(matrix3))
    print("---------------------------------------")
    print(matrix4)
    print(spiralOrder(matrix4))
    print("---------------------------------------")
    print(matrix5)
    print(spiralOrder(matrix5))
    print("---------------------------------------")
    print(matrix6)
    print(spiralOrder(matrix6))


