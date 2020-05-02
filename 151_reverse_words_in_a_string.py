def reverseWords(s):
    def core(s):
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s
            
    
    if not s:
        return s
    
    while s and s[0] == " ":
        s = s[1:]

    while s and s[-1] == " ":
        s = s[: -1]

    slow = 0
    fast = 0
    start = 0
    end = 0
    while fast < len(s):
        if s[fast] == " ":
            end = fast
            while fast + 1 < len(s) and s[fast + 1] == " ":
                fast += 1
            s[start: end + 1] = core(s[start: end + 1])
            start = fast + 1
            end = fast + 1
            
        print(s, slow, fast)
        print(s[0])
        s[slow] = s[fast]
        slow += 1
        fast += 1

    return core(s)


if __name__ == "__main__":
    s = "  blue   sky   "
    print(reverseWords(s))


    
