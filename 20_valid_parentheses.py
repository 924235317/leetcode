def isValid(s:str) -> bool:
    if len(s) <=0:
        return True
        
    if len(s) % 2 != 0:
        return False

    #if s[0] not in "[{(":
    #    return False

    p = list()
    for i in range(len(s)):
        print(s[i])
        if s[i] in "{[(":
            p.append(s[i])
        elif s[i] in "}])":
            if s[i] == "}":
                if len(p) > 0 and p[-1] == "{":
                    p.pop(-1)
                else:
                    return False
            elif s[i] == "]":
                if len(p) > 0 and p[-1] == "[":
                    p.pop(-1)
                else:
                    return False
            elif s[i] == ")":
                if len(p) > 0 and p[-1] == "(":
                    p.pop(-1)
                else:
                    return False
        else:
            return False
        
    if len(p) != 0:
        return False
    return True


if __name__ == "__main__":
    s = "{[}]()"
    print(isValid(s))
