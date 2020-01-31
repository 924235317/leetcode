def findMode(root: TreeNode) -> List[int]:
    #params - cur_max, pre, cur_num
    def findModeCore(root, res, params):
        if not root:
            return
        
        findModeCore(root.left, res, params)
        if root.val == params[1]:
            params[2] += 1
        else:
            params[1] = root.val
            params[2] = 1
        
        if params[2] > params[0]:
            params[0] = params[2]
            res.clear()
            res.append(root.val)
            params[0] = params[2]
        elif params[0] == params[2]:
            res.append(root.val)
            
        findModeCore(root.right, res, params)
    
    res = list()
    params = [-1, -2**31, -2]
    findModeCore(root, res, params)
    return res
