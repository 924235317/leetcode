def longestMountain(A: list) -> int:
    if len(A) < 3:
        return 0

    max_l = 0
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] > A[i+1]:
            l = r = i
            while l > 0 and A[l] > A[l-1]:
                l -= 1
            while r < (len(A) - 1) and A[r] > A[r+1]:
                r += 1

            print(A[l:r+1])
            max_l = max(max_l, r-l+1)
    return max_l

def longestMountain1(A: list) -> int:
    if len(A) < 3:
        return 0
    
    length = len(A)
    down = [0 for i in range(length)]
    up = [0 for i in range(length)]
    max_l = 0

    for i in range(length-2, -1, -1):
        if A[i] > A[i+1]:
            down[i] = down[i+1] + 1

    for i in range(1, length-1):
        if A[i] > A [i-1]:
            up[i] = up[i-1] + 1

        if down[i] > 0 and up[i] > 0:
            max_l = max(max_l, down[i]+up[i]+1)

    return max_l

if __name__ == "__main__":
    A = [0,1,0]
    print(longestMountain(A))
    print(longestMountain1(A))
            
