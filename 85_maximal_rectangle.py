def maximalRectangle(matrix: list) -> int:
    def maximalRectangleCore(heights):
        stack = list()
        res = 0
        heights.append(0)
        print(heights)

        for i in range(len(heights)):
           if stack and heights[i] < heights[i-1]:
               while stack and heights[i] < heights[stack[-1]]:
                   idx = stack.pop()
                   l = i-stack[-1]-1 if stack else i
                   res = max(res, l*heights[idx])
           stack.append(i)
        return res

    w = len(matrix[0])
    h = len(matrix)

    tmp = [[0 for i in range(w)] for j in range(h)]
    for i in range(h):
        for j in range(w):
            if i == 0:
                tmp[i][j] = int(matrix[i][j])
            else:
                if matrix[i][j] == "1":
                    tmp[i][j] = tmp[i-1][j] + 1
                else:
                    tmp[i][j] = 0
    res = 0
    for i in range(h):
        res = max(res,maximalRectangleCore(tmp[i]))

    return res

def maximalRectangle2(matrix: list) -> int:
    def maximalRectangleCore(heights):
        stack = list()
        res = 0
        heights.append(0)

        for i in range(len(heights)):
            if stack and heights[i] < heights[i-1]:
                while stack and heights[i] < heights[stack[-1]]:
                    idx = stack.pop()
                    l = i-stack[-1]-1 if stack else i
                    res = max(res, l*heights[idx])
            stack.append(i)
        return res

    w = len(matrix[0])
    h = len(matrix)

    tmp = [0 for i in range(w)]
    for j in range(w):
        tmp[j] = int(matrix[0][j])
    res = maximalRectangleCore(tmp)

    for i in range(1, h):
        for j in range(w):
            if matrix[i][j] == "0":
                tmp[j] = 0
            else:
                tmp[j] += 1
            
        res = max(res, maximalRectangleCore(tmp))

    return res
                    
    

if __name__ == "__main__":
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    #matrix = [["0","1"]]
    print(maximalRectangle(matrix))
