def getPermutation(n: int, k: int) -> str:
    def getPermutationCore(nums: list, k: int, total: int, res: list):
        if len(nums) == 0:
            return
        next_total = int(total // len(nums))
        idx = int(k // next_total)
        next_k = k - idx * next_total
        #res += str(nums.pop(idx))
        res.append(str(nums.pop(idx)))
        getPermutationCore(nums, next_k, next_total, res)
    
    total = 1
    for i in range(1, n+1):
        total *= i

    res = list()
    nums = list(range(1, n + 1))
    getPermutationCore(nums, k-1, total, res)
    res = "".join(res)
    return res

    
if __name__ == "__main__":
    n = 4
    k = 19
    print(getPermutation(n, k))
