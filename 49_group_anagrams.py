def groupAnagrams(strs: list) -> list:

    def list2str(l: list) -> str:
        res = ""
        for ll in l:
            res += str(ll)
        return res
    
    tmp = dict()
    res = list()
    for s in strs:
        t = [0] * 26
        for ss in s:
            t[ord(ss) - ord("a")] += 1

        str_t = list2str(t)
        if str_t in tmp.keys():
            tmp[str_t].append(s)
        else:
            tmp[str_t] = [s]
    res = list(tmp.values())
    return res
            

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))
