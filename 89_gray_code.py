def grayCode(n: int) -> list:
    if n < 0:
        return []

    res = [0]
    for i in range(0, n):
        for j in range(len(res)-1, -1, -1):
            res.append(res[j] + (1 << i))

    return res

if __name__ == "__main__":
    n = 4
    print(grayCode(n))
