def findBottomLeftValue(self, root: TreeNode) -> int:
    queue = list()
    queue.append([root, 0])
    
    res = None
    cur_level = -1
    while queue:
        node, level = queue.pop(0)
        if node.left:
            queue.append([node.left, level + 1])
        if node.right:
            queue.append([node.right, level + 1])
        
        if cur_level < level:
            res = node.val
            cur_level = level
    
    return res
