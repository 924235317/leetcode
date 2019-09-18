def combine(n: int, k: int) -> list:
    def combineCore(n: int, k: int, pos: int, tmp: list, res: list):
        if k == 0:
            t = list()
            for tt in tmp:
                t.append(tt)
            res.append(t)
            return

        for i in range(pos+1, n+1):
            tmp.append(i)
            combineCore(n, k-1, i, tmp, res)
            tmp.pop(-1)

    tmp = list()
    res = list()
    combineCore(n, k, 0, tmp, res)
    return res


if __name__ == "__main__":
    n = 4
    k = 2
    print(combine(n, k))
