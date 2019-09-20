def findSubstring(s: str, words: list) -> list:
    if not s or not words:
        return []    

    d1 = dict()
    for word in words:
        if word not in d1:
            d1[word] = 0
        d1[word] += 1

    s_len = len(s)
    words_len = len(words)
    word_len = len(words[0])
    res = list()
    
    for i in range(s_len-words_len*word_len+1):
        cur_d = dict()
        flag = True
        for j in range(i, i+words_len*word_len, word_len):
            tmp = s[j:j+word_len]
            if tmp not in d1:
                flag = False
                break
            if tmp not in cur_d:
                cur_d[tmp] = 0
            cur_d[tmp] += 1
            
            if cur_d[tmp] > d1[tmp]:
                flag = False
                break
        
        if flag:
            res.append(i)

    return res


if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    print(findSubstring(s, words))


