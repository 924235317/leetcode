def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0

    w = len(matrix[0])
    h = len(matrix)

    dp = [[0 if matrix[j][i] == "0" else 1 for i in range(w)] for j in range(h)]

    max_res = 1
    for ww in range(1, w):
        for hh in range(1, h):
            if matrix[hh][ww] == "1":
                dp[hh][ww] = min(dp[hh - 1][ww], dp[hh][ww - 1], dp[hh - 1][ww - 1]) + 1
                max_res = max(dp[hh][ww], max_res)

    for i in range(h):
        print(matrix[i])
    print()
    for i in range(h):
        print(dp[i])
    return max_res**2


if __name__ == "__main__":
    matrix = [["0","1","1","0","1"],["1","1","0","1","0"],["0","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["0","0","0","0","0"]]

    print(maximalSquare(matrix))
