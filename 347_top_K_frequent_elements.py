def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        print(freq)
        res = list()
        for num in freq:
            if not res:
                res.append(num)
            else:
                l, r = 0, len(res) - 1
                while l <= r:
                    m = l + (r - l) // 2
                    if freq[num] < freq[res[m]]:
                        l = m + 1
                    else:
                        r = m - 1
                    
                res.insert(l, num)
                if len(res) > k:
                    res.pop(-1)
        return res
        
