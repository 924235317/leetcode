def findMin(nums):
    def findMinCore(nums, l, r):
        if l == r:
            return nums[l]
        if r - l == 1:
            return min(nums[l], nums[r])

        if nums[l] < nums[r]:
            return nums[l]
        
        m = l + (r - l) // 2
        if nums[m] < nums[l]:
            return findMinCore(nums, l, m)
        elif nums[m] > nums[r]:
            return findMinCore(nums, m, r)
        else:
            #return min(findMinCore(nums, l, m), findMinCore(nums, m, r))
            return min(nums[l:r+1])

    return findMinCore(nums, 0, len(nums) - 1)

if __name__ == "__main__":

    nums = [3, 1, 3, 3, 3 ]
    print(findMin(nums))
        
        
