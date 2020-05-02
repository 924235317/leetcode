import TreeNode

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def distanceK(root, target, K: int):
    def dfs(root, ve):
            if not root:
                return 

            if root not in ve:
                ve[root] = list()

            if root.left:
                ve[root].append(root.left)
                if root.left not in ve:
                    ve[root.left] = list()
                ve[root.left].append(root)
                dfs(root.left, ve)

            if root.right:
                ve[root].append(root.right)
                if root.right not in ve:
                    ve[root.right] = list()
                ve[root.right].append(root)
                dfs(root.right, ve)

        ve = dict()
        dfs(root, ve)

        queue = list()
        queue.append([target, 0])
        
        res = list()
        memo = dict()
        while queue:
            top, k = queue.pop(0)
            
            if top in memo:
                continue
            
            memo[top] = 1
            if k == K:
                # print("aaa", top.val)
                res.append(top.val)
                continue
            
            for node in ve[top]:
                queue.append([node, k + 1])

        return res
