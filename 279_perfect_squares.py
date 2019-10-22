def numSquares(self, n: int) -> int:
    queue = list()
    visited = [False for i in range(n)]
    
    queue.append([n, 0])
    while queue:
        cur, step = queue.pop(0)
        for i in range(cur+1):
            a = cur - i * i
            if a < 0:
                break
            if a == 0:
                return step + 1
            
            if not visited[a-1]:
                visited[a-1] = True
                queue.append([a, step+1])
