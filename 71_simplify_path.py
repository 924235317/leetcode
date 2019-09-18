def simplifyPath(path: str) -> str:
    def list2path(l: list) -> str:
        tmp = list()
        for ll in l:
            if ll == "/.":
                continue
            elif ll == "/..":
                if len(tmp) < 1:
                    continue
                else:
                    tmp.pop(-1)
            else:
                tmp.append(ll)
        
        if len(tmp) < 1:
            return "/"

        res = "" 
        for tt in tmp:
            res += tt

        return res


    if len(path) < 1:
        return ""
    l = 0
    r = l + 1
    length = len(path)

    tmp = list()
    while r < length:
        if path[r] == "/":
            if r - l > 1:
                tmp.append(path[l:r])
                l = r
            elif r - l == 1:
                l = r
        r += 1

    if r - l > 1:
        tmp.append(path[l:r])
       
    return list2path(tmp)
    

if __name__ == "__main__":
    path = "/a/.."
    print(simplifyPath(path))
