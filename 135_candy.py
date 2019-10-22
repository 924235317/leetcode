def candy(ratings: list) -> int:
    if len(ratings) < 1:
        return 0

    length = len(ratings)
    right_idxs = [length-1 for i in range(length)]
    left_idxs = [0 for i in range(length)]
    res = 0 

    l = 0
    r = 0
    while l <= r and r < length-1:
        if ratings[r] <= ratings[r+1]:
            for i in range(l, r+1):
                right_idxs[i] = r
            l = r + 1
        r += 1
    l = length - 1
    r = length - 1
    while l <= r and l > 0:
        if ratings[l] <= ratings[l-1]:
            for i in range(r, l-1, -1):
                left_idxs[i] = l
            r = l - 1
        l -= 1
    
    for i in range(length):
        res += max(abs(right_idxs[i]-i), abs(left_idxs[i]-i)) + 1

    return res

def candy2(ratings: list) -> int:
    if len(ratings) < 1:
        return 0

    length = len(ratings)
    idxs = [length-1 for i in range(length)]
    res = 0 

    l = 0
    r = 0
    while l <= r and r < length-1:
        if ratings[r] <= ratings[r+1]:
            for i in range(l, r+1):
                idxs[i] = r
            l = r + 1
        r += 1
    l = length - 1
    r = length - 1
    while l <= r and l > 0:
        if ratings[l] <= ratings[l-1]:
            for i in range(r, l-1, -1):
                res += max(abs(idxs[i]-i), abs(l-i)) + 1
            r = l - 1
        l -= 1
    
    #for i in range(length):
    #    res += max(abs(right_idxs[i]-i), abs(left_idxs[i]-i)) + 1

    return res


if __name__ == "__main__":
    ratings = [1, 0, 2]
    print(candy2(ratings))
