def findMin(nums):
    def findMinCore(nums, l, r):
        if l == r:
            return nums[l]

        if r - l == 1:
            return min(nums[l], nums[r])

        if nums[l] < nums[r]:
            return nums[l]

        m = l + (r - l) // 2

        if nums[m] > nums[r]:
            return findMinCore(nums, m, r)
        elif nums[m] < nums[l]:
            return findMinCore(nums, l, m)
        

    return findMinCore(nums, 0, len(nums) - 1)

if __name__ == "__main__":
    nums = [6, 7, 8, 1]
    print(findMin(nums))

    



