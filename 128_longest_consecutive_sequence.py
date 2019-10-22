def longestConsecutive(nums: list) -> int:
    nums = set(nums)
    res = 0
    i = 0
    l = len(nums)
    while nums:
        cur = nums.pop()
        smaller = cur - 1
        greater = cur + 1
        i_s = 0
        i_g = 0

        while smaller in nums:
            nums.remove(smaller)
            smaller -= 1
            i_s += 1
        while greater in nums:
            nums.remove(greater)
            greater += 1
            i_g += 1
        res = max(res, i_g+i_s+1)

    return res

if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(nums))
