def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
    def findFrequentTreeSumCore(root, d):
        if not root:
            return 0
        
        left = findFrequentTreeSumCore(root.left, d)
        right = findFrequentTreeSumCore(root.right, d)
        
        s = root.val + left + right
        
        if not s in d:
            d[s] = 0
        
        d[s] += 1
        
        return s
    
    d = dict()
    findFrequentTreeSumCore(root, d)
    res = list()
    max_f = 0
    
    for key, value in d.items():
        if value > max_f:
            res = [key]
            max_f = value
        elif value == max_f:
            res.append(key)
    
    return res
