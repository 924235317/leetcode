def longestCommonPrefix(strs: list) -> str:
    if len(strs) < 1:
        return ""

    res = ""
    for i in range(len(strs[0])):
        tmp = strs[0][i]
        for j in range(len(strs)):
            if len(strs[j]) <= i:
                return res

            if strs[j][i] != tmp:
                return res

        res += tmp

    return res

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix(strs))
    
