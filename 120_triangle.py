
min_sum = 2 ** 31 - 1
res = None
def minimumTotal(triangle: list) -> list:
    global min_sum
    global res
    def minimumTotalCore(triangle, tmp, cur_sum, row, col):
        print(row, col, cur_sum)
        global min_sum
        global res
        if row >= len(triangle):
            if cur_sum < min_sum:
                min_sum = cur_sum
                res = [t for t in tmp]
            return

        cur_num = triangle[row][col]
        tmp.append(cur_num)
        minimumTotalCore(triangle, tmp, cur_sum+cur_num, row+1, col)
        minimumTotalCore(triangle, tmp, cur_sum+cur_num, row+1, col+1)
        tmp.pop(-1)
        

    tmp = list()
    minimumTotalCore(triangle, list(), 0, 0, 0)
    return res


def minimumTotal2(triangle: list) -> list:
    dp = [[0 for i in range(len(triangle[-1]))] for j in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for row in range(1, len(triangle)):
        for col in range(len(triangle[row])):
            if col == 0:
                dp[row][col] = dp[row-1][col] + triangle[row][col]
            elif col == len(triangle[row]) - 1:
                dp[row][col] = dp[row-1][col-1] + triangle[row][col]
            else:
                dp[row][col] = min(dp[row-1][col-1], dp[row-1][col]) + triangle[row][col]
    return min(dp[-1])


def minimumTotal3(triangle: list) -> list:
    dp = [0 for i in range(len(triangle[-1]))]
    dp[0] = triangle[0][0]
    for row in range(1, len(triangle)):
        for col in range(len(triangle[row])-1, -1, -1):
            if col == 0:
                dp[col] = dp[col] + triangle[row][col]
            elif col == len(triangle[row]) - 1:
                dp[col] = dp[col-1] + triangle[row][col]
            else:
                dp[col] = min(dp[col-1], dp[col]) + triangle[row][col]
    return min(dp)

if __name__ == "__main__":
    #triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    triangle = [[-1],[-3,-4]]

    print(minimumTotal3(triangle))
