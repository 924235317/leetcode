def removeElement(nums: list, val: int) -> int:
    l = 0
    r = len(nums)

    while l < r:
        if nums[l] == val:
            r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        else:
            l += 1

    return r

if __name__ == "__main__":
    nums = [3,2,2,1,1,4,5]
    val = 2

    print(nums[:removeElement(nums, val)])
         
