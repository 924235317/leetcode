def nextPermutation(nums:list) -> None:
    def swap(nums: list, idx1: int, idx2: int) -> None:
        tmp = nums[idx1]
        nums[idx1] = nums[idx2]
        nums[idx2] = tmp

    def reverse(nums: list, idx1: int, idx2: int) -> None:
        while idx1 < idx2:
            swap(nums, idx1, idx2)
            idx1 += 1
            idx2 -= 1

    if len(nums) <= 1:
        return nums

    idx = 0
    idx2 = 0
    for i in range(len(nums) - 2, -1, -1):
        if nums[i + 1] > nums[i]:
            idx = i
            break

    if idx == 0 and nums[idx] >= nums[idx + 1]:
        reverse(nums, 0, len(nums) - 1)
        return

    for j in range(len(nums) - 1, idx -1, -1):
        if nums[j] > nums[idx]:
            idx2 = j
            break
   
    swap(nums, idx, idx2)
    reverse(nums, idx + 1, len(nums) - 1)


if __name__ == "__main__":
    nums = [3, 2, 1]
    nextPermutation(nums)
    print(nums)
