def combinationSum(candidates: list, target: int) -> list:
    def combinationSumCore(candidates, target, l, tmp, res):
        print(tmp)
        if target == 0:
            res.append([t for t in tmp])
            return 
        
        for i in range(l, len(candidates)):
            if candidates[i] > target:
                return
            tmp.append(candidates[i])
            combinationSumCore(candidates, target-candidates[i], i, tmp, res)
            tmp.pop(-1)

    if not candidates:
        return []

    candidates.sort()
    res = list()
    tmp = list()
    combinationSumCore(candidates, target, 0, tmp, res)
    return res


if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    print(combinationSum(candidates, target))

