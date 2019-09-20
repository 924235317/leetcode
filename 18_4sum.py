def fourSum(nums: list, target: int) -> list:
    
    if len(nums) < 4:
        return []
    
    nums.sort()
    length = len(nums)
    res = list()
    for i in range(length-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, length-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            l = j + 1
            r = length - 1
            while l < r:
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
    return res


if __name__ == "__main__":
    nums = [-3,-2,-1,0,0,1,2,3] 
    target = 0
    print(fourSum(nums, target))
   
