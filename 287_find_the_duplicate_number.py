# O(n) space O(n) time
def findDuplicate(nums: list) -> int:
    length = len(nums)
    m = [0 for i in range(length+1)]

    for num in nums:
        if m[num] == 1:
            return num
        else:
            m[num] = 1

def findDuplicate2(nums:list) -> int:
    l = 1
    r = len(nums) - 1

    count = 0
    while l < r:
        m = (l + r) // 2
        for num in nums:
            if num <= m:
                count += 1

        if count > m:
            r = m
        else:
            l = m + 1
        count = 0

    return l


if __name__ == "__main__":
    nums = [1, 1, 3, 4, 2]
    print(findDuplicate(nums))
    print(findDuplicate2(nums))

