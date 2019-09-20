def generateParenthesis(n: int) -> list:
    def generateParenthesisCore(res: list, s: str, l: int, r: int):
        
        if l == 0 and r == 0:
            res.append(s)
            return

        if l > 0:
            generateParenthesisCore(res, s+"(", l-1, r)

        if r > l:
            generateParenthesisCore(res, s+")", l, r-1)

    res = list()
    s = ""
    generateParenthesisCore(res, s, n, n)
    return res


if __name__ == "__main__":
    n = 3
    print(generateParenthesis(n))
