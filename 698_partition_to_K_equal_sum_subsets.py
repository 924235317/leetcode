def canPartitionKSubsets(nums, k):
    def canPartitionKSubsetsCore(nums, buckets, target, n):
        for i in range(len(buckets)):
            if buckets[i] + nums[n] > target:
                continue

            buckets[i] += nums[n]
            if n == len(nums) - 1:
                return True
            if canPartitionKSubsetsCore(nums, buckets, target, n + 1):
                return True
            else:
                buckets[i] -= nums[n]
                if buckets[i] == 0:
                    return False
        return False

    nums = sorted(nums)
    nums.reverse()
    target = sum(nums) // k
    if target * k != sum(nums):
        return False

    buckets = [0 for i in range(k)]
    return canPartitionKSubsetsCore(nums, buckets, target, 0)


if __name__ == "__main__":
    #nums = [2,2,2,2,3,4,5]
    #k = 4
    nums = [724,3908,1444,522,325,322,1037,5508,1112,724,424,2017,1227,6655,5576,543]
    k = 4

    print(canPartitionKSubsets(nums, k))
    
