def permute(nums: list) -> list:
    def permuteCore(nums:list, tmp: list, pos_list: list, res:list):
        if len(tmp) == len(nums):
            t = list()
            for tt in tmp:
                t.append(tt)
            res.append(t)
            return

        for i in range(len(nums)):
            if pos_list[i] == 1:
                continue

            tmp.append(nums[i])
            pos_list[i] = 1
            permuteCore(nums, tmp, pos_list, res)
            tmp.pop(-1)
            pos_list[i] = 0

    if len(nums) <= 1:
        return nums
    
    nums.sort()
    tmp = list()
    pos_list = [0] * len(nums)
    res = list()
    
    permuteCore(nums, tmp, pos_list, res)
    return res


if __name__ == "__main__":
    nums = [1,2,3]
    res = permute(nums)
    print(res)

