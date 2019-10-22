def partition(s: str) -> list:
    def isPalindrome(s):
        length = len(s)
        l = (length-1) // 2
        r = l
        if length % 2 == 0:
            r += 1

        while l >= 0 and r < length:
            if not s[l] == s[r]:
                return False
            l -= 1
            r += 1

        return True

    def partitionCore(s, cur, res):
        if len(s) < 1:
            res.append([c for c in cur])
            return
        
        for i in range(len(s)):
            if isPalindrome(s[:i+1]):
                cur.append(s[:i+1])
                partitionCore(s[i+1:], cur, res)
                cur.pop(-1)
        
    cur = list()
    res = list()
    partitionCore(s, cur, res)
    return res


if __name__ == "__main__":
    s = "aab"
    print(partition(s))

    
