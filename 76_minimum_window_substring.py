def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""

    target = dict()
    find = dict()
    count = 0

    for tt in t:
        if not tt in target:
            target[tt] = 0
        target[tt] += 1
    
    l = 0
    flag = False
    min_str = s
    for r in range(len(s)):
        if s[r] in target:
            if s[r] not in find:
                find[s[r]] = 0
            if find[s[r]] < target[s[r]]:
                count += 1
            find[s[r]] += 1
        
        print(s[l:r+1])
        if count == len(t):
            flag = True
            while l < r:
                if not s[l] in target:
                    l += 1
                elif find[s[l]] > target[s[l]]:
                    find[s[l]] -= 1
                    l += 1
                else:
                    break
            min_str = s[l:r+1] if len(min_str) > r-l+1 else min_str
    return min_str if flag else ""


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    
    print(minWindow(s, t))
