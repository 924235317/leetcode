def findPeakElements(nums):
    length = len(nums)
    if length < 2:
        return 0

    if nums[0] > nums[1]:
        return 0

    if nums[length - 1] > nums[length - 2]:
        return length - 1


    for i in range(1, length - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i

def findPeakElement(self, nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    while(left < right):
        mid = int(left + (right - left) / 2)
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == "__main__":
    nums = [1,2,3,1]
    print(findPeakElements(nums))
