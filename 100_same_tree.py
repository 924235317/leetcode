from treenode import *

def isSameTree(p: TreeNode, q: TreeNode) -> bool
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False
