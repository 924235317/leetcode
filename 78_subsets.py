def subsets(nums: list) -> list:
    def subsetsCore(nums: list, k:int, pos: int, tmp: list, res: list):
        if k == 0:
            t = list()
            for tt in tmp:
                t.append(tt)
            res.append(t)
            return 

        for i in range(pos+1, len(nums)):
            tmp.append(nums[i])
            subsetsCore(nums, k-1, i, tmp, res)
            tmp.pop(-1)


    res = list()
    for k in range(len(nums)+1):
        tmp = list()
        subsetsCore(nums, k, -1, tmp, res)

    return res


if __name__ == "__main__":
    nums = [1,1,2]
    print(subsets(nums))
                 
