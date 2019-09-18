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

if __name__ == "__main__":
    s = "abcdabbcaddsfsfoeijfojj"
    print(s)
    print(lengthOfLongestSubstring(s))

        
