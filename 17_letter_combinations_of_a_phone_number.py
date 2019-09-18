def letterCombinations(digits: str) -> list:
    dic = {'2': ['a', 'b', 'c'], 
           '3': ['d', 'e', 'f'],
           '4': ['g', 'h', 'i'],
           '5': ['j', 'k', 'l'],
           '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'],
           '8': ['t', 'u', 'v'],
           '9': ['w', 'x', 'y', 'z']}

    if not digits:
        return []

    res = [""]
    for d in digits:
        tmp = list()
        for s in dic[d]:
            for r in res:
                tmp.append(r+s)
        res = tmp

    return res


if __name__ == "__main__":
    digits = "322"
    print(letterCombinations(digits))

