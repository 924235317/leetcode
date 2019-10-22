def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    
    que = list()
    res = list()
    que.append([0, root])
    while len(que) > 0:
        cur = que.pop(0)
        if cur[1]:
            que.append([cur[0]+1, cur[1].left])
            que.append([cur[0]+1, cur[1].right])
            
            if cur[0] > len(res) - 1:
                res.append([cur[1].val])
            else:
                res[cur[0]].append(cur[1].val)
    
    return res 

def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    
    level = list()
    res = list()
    
    level.append(root)
    while level:
        cur_val = list()
        next_level = list()
        for l in level:
            cur_val.append(l.val)
            if l.left:
                next_level.append(l.left)
            if l.right:
                next_level.append(l.right)
        level = next_level
        res.append(cur_val)
    return res
