import numpy as np


def majorityElement(nums):
        
    length = len(nums)
    if length == 1:
        return nums[0]
    nums.sort()
    print(nums)
    head = 0
    counter = 0
    for tail in range(length):
        if counter >= length / 2.:
            return nums[head]
        if nums[head] == nums[tail]:
            counter += 1
        else:
            head = tail
            counter = 0
    return nums[head]

def majorityElement2(nums):
    n = None
    counter = 0
    for num in nums:
        if n is None:
            n = num
            counter = 1
        elif n == num:
            counter += 1
        else:
            if counter == 0:
                n = num
                counter = 1
            else:
                counter -= 1
    return n


if __name__ == "__main__":
    nums = np.random.randint(8, 10, 11)
    print(nums)
    num = majorityElement2(nums)
    print(num)
