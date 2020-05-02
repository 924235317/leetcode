def minSubArrayLen(s: int, nums: list) -> int:
    length = len(nums)
    if length < 1:
        return 0
    if length == 1:
        return 0 if nums[0] < s else 1
    
    l = 0
    min_len = length + 1
    cur_sum = 0
    for r in range(length):
        cur_sum += nums[r]
        while cur_sum >= s:
            min_len = min(min_len, r - l + 1)
            cur_sum -= nums[l]
            l += 1
            
    
    return min_len if min_len != length + 1 else 0
