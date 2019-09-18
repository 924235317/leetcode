def twoSum(nums: list, target: int) -> list:
    if len(nums) < 2:
        return []

    h = dict()
    for i, num in enumerate(nums):
        num_to_find = target - num
        if num_to_find in h.keys():
            return [h[num_to_find], i]
        else:
            h[num] = i

    return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))
