memo = dict()

def rob(root):
    if not root:
        return 0
    
    if root in memo:
        return memo[root]


    rob_it = root.val
    if root.left:
        rob_it += rob(root.left.left) + rob(root.left.right)
    if root.right:
        rob_it += rob(root.right.left) + rob(root.right.right)
    
    not_rob_it = rob(root.left) + rob(root.right)

    res = max(rob_it, not_rob_it)
    memo[root] = res
    return res
