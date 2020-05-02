def compareVersion(version1, version2):
    if not version1 and not version2:
        return 0

    v1 = version1.split(".") if version1 else []
    v2 = version2.split(".") if version2 else []
 
    len_v1 = len(v1)
    len_v2 = len(v2)

    if len_v1 > len_v2:
        for i in range(len_v1 - len_v2):
            v2.append("0")
    else:
        for i in range(len_v2 - len_v1):
            v1.append("0")

    for i in range(len(v1)):
        if int(v1[i]) > int(v2[i]):
            return 1
        elif int(v1[i]) < int(v2[i]):
            return -1

    return 0



if __name__ == "__main__":
    version1 = "1.1.1"
    version2 = "1.1"
    print(compareVersion(version1, version2))
        
