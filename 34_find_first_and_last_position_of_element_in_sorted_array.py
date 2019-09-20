def searchRange(nums: list, target: int) -> list:
    def searchLeft(nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        print(1, l, r)
        return l

    def searchRight(nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1

        print(2, l, r)
        return r


    l = searchLeft(nums, target)
    r = searchRight(nums, target)

    return [l, r] if l <= r else [-1, -1]


if __name__ == "__main__":
    nums = [1,2,2,2,3,3,3,3,3,4,5]
    target = 3
    print(nums, target)
    print(searchRange(nums, target))
