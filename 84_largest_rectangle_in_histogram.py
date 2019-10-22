def largestRectangleArea(heights: list) -> int:
    heights.append(0)

    max_rec = 0
    stack = list()
    for i in range(len(heights)):
        while stack and heights[stack[-1]] >= heights[i]:
            idx = stack.pop(-1)
            l = i-stack[-1]-1 if stack else i
            max_rec = max(max_rec, heights[idx]*l)
        stack.append(i)

    return max_rec

if __name__ == "__main__":
    heights = [2, 1, 2]

    print(largestRectangleArea(heights))
