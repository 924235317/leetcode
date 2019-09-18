def binary_search(nums: list, left: int, right: int, target: int) -> int:
    res = -1
    if left > right:
        return res 
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            res = mid
            break
    return res


def searchCore(nums: list, left: int, right: int, target: int) -> int:
    if len(nums) < 1:
        return -1

    if left == right:
        return left if nums[left] == target else -1

    m = (left + right) // 2
    res = -1
    if nums[m] == target:
        return m
    elif nums[m] > nums[left]:
        res = binary_search(nums, left, m - 1, target)
        if res == -1:
            res = searchCore(nums, m + 1, right, target)
    elif nums[m] < nums[left]:
        res = binary_search(nums, m + 1, right, target)
        if res == -1:
            res = searchCore(nums, left, m - 1, target)
    else:
        res = searchCore(nums, m + 1, right, target)
    
    return res

def search(nums: list, target: int) -> int:
    return searchCore(nums, 0, len(nums)-1, target)


if __name__ == "__main__":
    nums = [1, 3]
    target = 0
    idx = search(nums, target)

    print(idx, nums[idx])
            
