def singleNumber(nums):
    if len(nums) < 3:
        return []

    different_bits = 0
    mask = 1
    for num in nums:
        different_bits = different_bits ^ num

    while (mask & different_bits) == 0:
        mask = mask << 1

    a = 0
    b = 0
    for num in nums:
        if num & mask:
            a = a ^ num
        else:
            b = b ^ num

    return [a, b]


if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 5]
    print(singleNumber(nums))
