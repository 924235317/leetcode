def plusOne(digits: list) -> list:
    def reverse(digits: list) -> list:
        l = 0
        r = len(digits) - 1
        while l < r:
            digits[r], digits[l] = digits[l], digits[r]
            r = r - 1
            l = l + 1
        return digits
    
    if len(digits) < 1:
        return []

    res = list()
    flag = 1
    for i in range(len(digits)-1, -1, -1):
        tmp = digits[i] + flag
        if tmp == 10:
            res.append(0)
            flag = 1
        else:
            res.append(tmp)
            flag = 0
    if flag == 1:
        res.append(1)
    print(res)
    
    return reverse(res)

if __name__ == "__main__":
    digits = [4,3,2,1]
    print(plusOne(digits))
