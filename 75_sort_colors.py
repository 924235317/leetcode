#def sortColors(nums: list) -> None:
#    def swap(nums: list, idx1: int, idx2: int):
#        print("sawp: {} -> {}, {} -> {}".format(idx1, idx2, nums[idx1], nums[idx2]))
#        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
#        print("after swap {}".format(nums))
#
#
#    if len(nums) <= 1:
#        return
#
#    idx_0 = -1
#    idx_2 = len(nums)
#    
#    idx = 0
#    while idx < idx_2:
#        if nums[idx] == 0:
#            idx_0 += 1
#            swap(nums, idx, idx_0)
#        elif nums[idx] == 2:
#            while idx_2 > idx and nums[idx_2-1] == 2:
#                idx_2 -= 1
#            if idx_2 <= idx:
#                break
#            idx_2 -= 1
#            swap(nums, idx, idx_2)
#            if nums[idx] == 0:
#                idx_0 += 1
#                swap(nums, idx_0, idx)
#        idx += 1

def sortColors(nums: list) -> None:
    def swap(nums: list, idx1: int, idx2: int):
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

    if len(nums) <= 1:
        return

    idx_0 = 0 
    idx_2 = len(nums) - 1
    
    idx = 0
    while idx <= idx_2:
        if nums[idx] == 0:
            swap(nums, idx, idx_0)
            idx_0 += 1
        elif nums[idx] == 2:
            swap(nums, idx, idx_2)
            idx_2 -= 1
            idx -= 1
        idx += 1

if __name__ == "__main__":
    nums = [2,0,2,1,1,0, 2,2,2]
    #nums = [0,2]
    sortColors(nums)
    print(nums)
