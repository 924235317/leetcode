def countSmaller(nums):
    def binary_search(nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                l = m + 1
            elif nums[m] < target:
                r = m - 1
        return l
        
    if not nums:
        return []

    length = len(nums)
    tmp = [nums[-1]]
    res = [0 for i in range(length)]
    for i in range(length - 2, -1, -1):
        idx = binary_search(tmp, nums[i])
        print(idx, nums[i], tmp)
        if idx == -1:
            res[i] = 0
            tmp.append(nums[i])
        else:
            res[i] = len(tmp) - idx
            tmp.insert(idx, nums[i])
    
    print("tmp", tmp)
    return res

           
def countSmaller2(nums):
    if not nums:
        return []

    length = len(nums)
    res = [0 for i in range(length)]

    for i in range(length - 1, -1, -1):
        for j in range(i + 1, length):
            if nums[j] < nums[i]:
                res[i] += 1
    return res

def countSmaller3(nums):
    def mergeSort(nums, l, r, res):
        if r - l < 1:
            return

        m = l + (r - l) // 2
        mergeSort(nums, l, m, res)
        mergeSort(nums, m + 1, r, res)

        p1 = l
        p2 = m + 1
        tmp = [[None, None] for i in range(r - l + 1)]
        cur = 0
        while p1 <= m and p2 <= r:
            if nums[p1] <= nums[p2]:
                tmp[cur] = nums[p1]
                p1 += 1
            else:
                for i in range(p1, m + 1):
                    res[nums[i][1]] += 1
                tmp[cur] = nums[p2]
                p2 += 1

            cur += 1
        
        while p1 <= m:
            tmp[cur] = nums[p1]
            p1 += 1
            cur += 1

        while p2 <= r:
            tmp[cur] = nums[p2]
            p2 += 1
            cur += 1

        for i in range(l, r + 1):
            nums[i] = tmp[i - l]


    res = [0 for i in range(len(nums))]
    nums_idxs = list(zip(nums, range(len(nums))))
    mergeSort(nums_idxs, 0, len(nums) - 1, res)
    return res


if __name__ == "__main__":
    nums = [5,4,1,6,2]
    print(nums)
    print(countSmaller3(nums))
