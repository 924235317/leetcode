def firstMissingPositive(nums: list) -> int:
    length = len(nums)
    for i in range(length):
        while nums[i] > 0 and nums[i] <= length and nums[nums[i] - 1] != nums[i]:
            tmp = nums[i]
            nums[i] = nums[nums[i]-1]
            nums[tmp-1] = tmp
            #nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
    
    for j in range(length):
        if nums[j] != j + 1:
            return j + 1
    return length + 1

if __name__ == "__main__":
    nums = [1,2,3]
    print(firstMissingPositive(nums))
