def addBinary(a: str, b: str) -> str:
    def add(a: str, b: str) -> int:
        return ord(a) + ord(b) - 2 * ord("0")
    
    idx1 = len(a) - 1
    idx2 = len(b) - 1
    f = 0
    res = ""
    
    while idx1 >= 0 and idx2 >= 0:
        tmp = add(a[idx1], b[idx2]) + f
        if tmp == 0:
            res = "0" + res
            f = 0
        elif tmp == 1:
            res = "1" + res
            f = 0
        elif tmp == 2:
            res = "0" + res
            f = 1
        elif tmp == 3:
            res = "1" + res
            f = 1
        idx1 -= 1
        idx2 -= 1

    while idx1 >= 0:
        tmp = add(a[idx1], str(f))
        if tmp == 0:
            res = "0" + res
            f = 0
        elif tmp == 1:
            res = "1" + res
            f = 0
        elif tmp == 2:
            res = "0" + res
            f = 1
        idx1 -= 1

    while idx2 >= 0:
        tmp = add(b[idx2], str(f))
        if tmp == 0:
            res = "0" + res
            f = 0
        elif tmp == 1:
            res = "1" + res
            f = 0
        elif tmp == 2:
            res = "0" + res
            f = 1
        idx2 -= 1
        

    if f == 1:
       res = "1" + res

    return res
            

if __name__ == "__main__":
    a = "111"
    b = "111"
    print(addBinary(a, b))
