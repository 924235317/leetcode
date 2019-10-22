def generate(numRows: int) -> list:
    if numRows < 1:
        return []

    res = [[1]]
    for i in range(1, numRows):
        pre = res[-1]
        tmp = [1]
        for j in range(len(pre)-1):
            tmp.append(pre[j] + pre[j+1])
        tmp.append(1)
        res.append(tmp)
    
    return res

if __name__ == "__main__":
    numRows = 7
    print(generate(numRows))
