## unsolved

def fullJustify(words: list, maxWidth: int) -> list:
    
    cur_count = 0
    res = list()
    tmp = list()
    for w in words:
        if cur_count + len(w) > maxWidth:
            res.append(tmp)
            tmp = list()
            cur_count = 0

        tmp.append(w)
        tmp.append(" ")
        cur_count += len(w) + 1

    if cur_count > 0:
        res.append(tmp)
    
    return res

if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."] 
    maxWidth = 16
    print(fullJustify(words, maxWidth))

            
