def rotate(nums, k):
    def reverse(nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    length = len(nums)
    k = k % len(nums)
    reverse(nums, 0, length - 1 - k)
    reverse(nums, length - k, length - 1)
    reverse(nums, 0, length - 1)



if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    rotate(nums, 2)
    print(nums)

