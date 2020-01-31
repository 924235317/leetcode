def rob(nums):
    def rob_core(nums, memo, idx):
        if idx >= len(nums):
            return 0

        if memo[idx] != -1:
            return memo[idx]
        
        rob_it = rob_core(nums, memo, idx + 2) + nums[idx]
        not_rob_it = rob_core(nums, memo, idx + 1)

        res = max(rob_it, not_rob_it)
        memo[idx] = res
        return res

    
    if not nums:
        return 0

    memo = [-1 for i in range(len(nums))]
    return rob_core(nums, memo, 0)


if __name__ == "__main__":
    nums = [1,2,3,1]
    print(rob(nums))
