def singleNumber(nums: list) -> int:
    res = 0
    for num in nums:
        res ^= num

    return res

if __name__ == "__main__":
    nums = [1,2,4,4,2]
    print(singleNumber(nums))
