def X(self, a, b):
    R = []
    for a1 in a:
        for b1 in b:
            R.append(a1+b1)
    return R

def subsetsWithDup(nums: list) -> list:
    cnt={}
    for n in nums:
       if n not in cnt:
           cnt[n] = 0
       cnt[n]+=1
    R = [[]]
    for key in cnt:
        R = self.X(R, [[key] * i for i in range(cnt[key]+1)])
    return R


def subsetsWithDup(nums: list) -> list:
    res = [[]]
    nums.sort()
    for i in range(len(nums)):
        if i == 0 or nums[i] == nums[i-1]:
            l = len(res)
        for j in range(len(res)-l, len(res)):
            res.append(res[j] + [nums[i]])

    return res

if __name__ == "__main__":
    nums = [1,2,2]
    print(subsetsWithDup(nums))
    
