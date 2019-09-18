def trap(height: list) -> int:
    length = len(height)
    left = [0] * length
    right = [0] * length
    res = [0] * length

    tmp = 0
    for i in range(length):
        tmp = max(tmp, height[i])
        left[i] = tmp

    tmp = 0
    for j in range(length-1, -1, -1):
        tmp = max(tmp, height[j])
        right[j] = tmp

    for m in range(length):
        res[m] = min(left[m], right[m]) - height[m]

    return sum(res)

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(height))
