def generateMatrix(n: int) -> list:
    
    matrix = [[0 for i in range(n)] for j in range(n)]

    l = 0
    r = n - 1
    t = 0
    b = n - 1

    num = 1
    while l <= r and t <= b:
        for ll in range(l, r+1):
            matrix[t][ll] = num
            num += 1

        for tt in range(t+1, b+1):
            matrix[tt][r] = num
            num += 1

        for rr in range(r-1, l-1, -1):
            matrix[b][rr] = num
            num += 1

        for bb in range(b-1, t, -1):
            matrix[bb][l] = num
            num += 1

        l += 1
        r -= 1
        t += 1
        b -= 1

    return matrix

def print_matrix(matrix):
    for m in matrix:
        print(m)

if __name__ == "__main__":
    n = 6
    print_matrix(generateMatrix(n))
