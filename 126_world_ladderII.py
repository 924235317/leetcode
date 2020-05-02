#有错
abc = "abcdefghijklmnopqrstuvwxyz"

def findLadders(beginWord, endWord, wordList):
    global abc
    def bfs(beginWord, endWord, worldList, distance, graph):
        
        q = [[beginWord, 0]]
        while q:
            bw, level = q.pop(0)
            for i in range(len(beginWord)):
                for j in range(26):
                    if abc[j] == bw[i]:
                        continue

                    v = bw[:i] + abc[j] + bw[i + 1:]
                    if v in graph and distance[v] is not None:
                        graph[bw].append(v)
                        distance[v] = min(level + 1, distance[v])
                        q.append([v, level + 1])
                    if v == endWord:
                        break

    def dfs(beginWord, endWord, graph, cur, res):
        if beginWord == endWord:
            res.append([w for w in cur])
        for word in graph[beginWord]:
            cur.append(word)
            dfs(word, endWord, graph, cur, res)
            cur.pop(-1)
            
        
    distance = {v: None for v in wordList}
    distance[beginWord] = None 
    graph = {v: [] for v in wordList}
    graph[beginWord] = []

    bfs(beginWord, endWord, wordList, distance, graph)
    
    print(graph)
    res = []
    cur = [beginWord]
    dfs(beginWord, endWord, graph, cur, res)
    return res


if __name__ == "__main__":
    beginWord = "red"
    endWord = "tax"
    wordList = ["ted","tex","red","tax","tad","den","rex","pee"]

    print(findLadders(beginWord, endWord, wordList))
