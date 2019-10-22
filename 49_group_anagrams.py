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

def groupAnagrams2(strs: list) -> list:
    m = dict()
    for s in strs:
        tmp = "".join(sorted(s))
        if tmp not in m:
            m[tmp] = list()
        m[tmp].append(s)
    
    return list(m.values())
            

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams2(strs))
