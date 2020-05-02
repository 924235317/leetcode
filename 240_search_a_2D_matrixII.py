def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix or not matrix[0]:
        return False
    
    width = len(matrix[0])
    height = len(matrix)
    
    h = 0
    w = width - 1
    while h < height and w >=0:
        if matrix[h][w] == target:
            return True
        elif matrix[h][w] < target:
            h += 1
        else:
            w -= 1
    
    return False
