def reverseString(s:str, l:int, r:int) -> str:
    if len(s) <= 1:
        return s
    
    res = ""
    for i in range(r, l-1, -1):
        res += s[i]

    return res

def reverseWords(s:str) -> str:
    if len(s) <= 1:
        return s
    tmp = ""
    for i in range(len(s)):
        if i > 0 and s[i-1] == " " and s[i] == " ":
            continue
        tmp += s[i]
    
    if tmp[0] == " ":
       tmp = tmp[1:]
    print(tmp)
    l = 0
    r = 0
    res = ""
    while r < len(tmp):
        if r > 0 and tmp[r] == " " and l < r:
            res += reverseString(tmp, l, r-1)
            res += " "
            l = r + 1
        r += 1
    res += reverseString(tmp, l, r-1)
    res = reverseString(res, 0, len(res)-1)
    if res[0] == " ":
        res = res[1:]
    return res



if __name__ == "__main__":
    s = "   a key    must  "
    ss = reverseWords(s)
    print(ss)
