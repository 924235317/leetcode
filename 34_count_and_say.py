def countAndSay(n: int) -> str:
    if n == 0 or n == 1:
        return "1"
    
    ss = ""
    s = countAndSay(n-1)
    pre = None
    count = 0
    for i, _s in enumerate(s):
        if not pre:
            pre = _s
            count += 1
        else:
            if _s != pre:
                ss += "{}{}".format(count, pre)
                pre = _s
                count = 1
            else:
                count += 1
    
    ss += "{}{}".format(count, pre)
    return ss

if __name__ == "__main__":
    n = 10 
    print(countAndSay(n))
