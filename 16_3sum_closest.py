def threeSumClosest(nums: list, target: int) -> int:
    
    nums.sort()
    closet_sum = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            s = nums[l] + nums[r] + nums[i]
            if s == target:
                return target
            elif s < target:
                l += 1
            else:
                r -= 1
            
            if abs(closet_sum-target) > abs(s-target):
                closet_sum = s

    return closet_sum
            

if __name__ == "__main__":
    nums = [-1,2,1,-4]
    target = 2
    print(threeSumClosest(nums, target))
