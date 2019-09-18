def permuteUnique(nums: list) -> list:
    def permutUniqueCore(nums: list, tmp: list, res:list, pos_list: list):
        length = len(nums)
        if len(tmp) == length:
            t = list()
            for tt in tmp:
                t.append(tt)
            res.append(t)
            return

        for i in range(length):
            if pos_list[i] == 1:
                continue
            elif i > 0 and nums[i] == nums[i-1] and pos_list[i-1] != 1:
                continue
            else:
                tmp.append(nums[i])
                pos_list[i] = 1
                permutUniqueCore(nums, tmp, res, pos_list)
                tmp.pop(-1)
                pos_list[i] = 0
        
        return res

    res = list()
    tmp = list()
    pos_list = [0] * len(nums)
    return permutUniqueCore(nums, tmp, res, pos_list)

if __name__ == "__main__":
    nums = [1, 1, 2]
    print(permuteUnique(nums))
