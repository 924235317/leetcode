def maximumGap(nums):
    if len(nums) < 2:
        return 0

    if len(nums) == 2:
        return abs(nums[0] - nums[1])

    max_val = max(nums)
    min_val = min(nums)

    diff = (max_val - min_val) + 1
    length = diff if diff < len(nums) else diff // len(nums)
    bucket = [[None, None] for i in range((max_val - min_val) // length + 1)]
    for num in nums:
        n = (num - min_val) // length
        print(n)
        bucket[n][0] = num if not bucket[n][0] else min(num, bucket[n][0])
        bucket[n][1] = num if not bucket[n][1] else max(num, bucket[n][1])

    max_gap = 0
    last = None
    for b in bucket:
        if not b[0]:
            continue

        if not last:
            max_gap = max(b[1] - b[0], max_gap)
        else:
            max_gap = max(b[1] - b[0], max_gap, b[0] - last)
        last = b[1]

    return max_gap

if __name__ == "__main__":
    nums = [1, 3, 100]
    print(maximumGap(nums))
