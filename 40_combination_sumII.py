def combinationSum2(candidates: list, target: int) -> list:
    def combinationSumCore(candidates, target, l, tmp, res, tag):
        if target == 0:
            res.append([t for t in tmp])
            return

        for i in range(l, len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1] and not tag[i-1]:
                continue
            if candidates[i] > target:
                break
            tmp.append(candidates[i])
            tag[i] = True
            combinationSumCore(candidates, target-candidates[i], i+1, tmp, res, tag)
            tag[i] = False
            tmp.pop(-1)


    if not candidates:
        return []

    candidates.sort()

    tmp = list()
    res = list()
    tag = [False for i in range(len(candidates))]
    combinationSumCore(candidates, target, 0, tmp, res, tag)
    return res

if __name__ == "__main__":
    candidates = [1,2,2,2,3]
    target = 7
    print(combinationSum2(candidates, target))
