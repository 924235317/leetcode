def lengthOfLongestSubstring(s: str) -> int:
    length = len(s)
    if length <= 1:
        return length

    idxs = [-1 for i in range(256)]
    l = -1
    max_length = 0

    for r in range(len(s)):
        idx = ord(s[r])
        if idxs[idx] > l:
            l = idxs[idx]
        max_length = max(max_length, r - l)
        idxs[idx] = r


    return max_length

def lengthOfLongestSubstring2(s: str) -> int:
    length = len(s)
    if length <= 1:
        return length
    
    hash_set = dict()
    l = 0
    r = 0
    res = 0
    while r < length:
        if s[r] in hash_set:
            l = max(hash_set[s[r]] + 1, l)
        res = max(res, r-l+1)
        hash_set[s[r]] = r
        r += 1
            
    return res

if __name__ == "__main__":
    #s = "abcdabbcaddsfsfoeijfojj"
    s = "abba"
    print(s)
    print(lengthOfLongestSubstring(s))
    print(lengthOfLongestSubstring2(s))

        
