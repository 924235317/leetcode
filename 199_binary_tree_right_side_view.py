def rightSideView(root: TreeNode) -> List[int]:
    if not root:
        return [] 
    l = list()
    res = list()
    l.append([root, 0])
    while l:
        top_node, top_d = l.pop(0)
        if top_node.left:
            l.append([top_node.left, top_d+1])
        if top_node.right:
            l.append([top_node.right, top_d+1])
        if l and l[0][1] != top_d or not l:
                res.append(top_node.val)

    return res

global_level = -1

def rightSideView(root: TreeNode) -> List[int]:
    def dfs(root, res, level)
        global global_level
        if not root:
            return

        if global_level < level:
            res.append(root.val)
            global_level += 1
    
        dfs(root.right, res, level + 1)
        dfs(root.left, res, level + 1)


    if not root:
        return [] 
    res = list()
    dfs(root, res, 0)

    return res
