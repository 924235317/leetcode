def longestPalindrome(s: str) -> str:
    def check(s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l+1:r]

    if not s:
        return ""
    
    length = len(s)
    max_str = ""
    for i in range(length):
        tmp = check(s, i, i)
        max_str = tmp if len(tmp) > len(max_str) else max_str
        tmp = check(s, i, i+1)
        max_str = tmp if len(tmp) > len(max_str) else max_str

    return max_str

if __name__ == "__main__":
    s = "babbad"
    print(longestPalindrome(s))
            
            
