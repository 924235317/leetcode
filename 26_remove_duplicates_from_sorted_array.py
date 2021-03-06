def removeDuplicates(nums: list) -> int:
    if len(nums) < 1:
        return 0
    if len(nums) <= 1:
        return len(nums)

    idx = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[idx-1]:
            nums[idx] = nums[i]
            idx += 1

    return idx

if __name__ == "__main__":
    nums = [1,1,1,2,3,4,4,4,4,4,5]
    print(nums)
    res = removeDuplicates(nums)
    print(res, nums[:res], nums)
