def threeSum(nums: list) -> list:
    if not nums:
        return []

    nums.sort()
    res = list()
    for i in range(len(nums)-2):
        if nums[i] == nums[i-1] and i > 0:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                print(l, r)
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while r > l and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1

    return res

if __name__ == "__main__":
    nums = [0, 0, 0]
    print(threeSum(nums))
