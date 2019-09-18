def search(nums: list, target: int) -> bool:
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if target == nums[m]:
            return True

        if nums[m] == nums[l]:
            l += 1
        elif nums[m] == nums[r]:
            r -= 1
        elif nums[m] < nums[l]:
            if target > nums[m] and target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
        else:
            if target < nums[m] and target >= nums[l]:
                r = m - 1
            else:
                l = m + 1
        
    return False


if __name__ == "__main__":
    nums =[1,2]
    target = 2
    print(search(nums, target))
