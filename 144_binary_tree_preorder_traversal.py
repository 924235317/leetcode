from treenode import *

def inorderTraversal(root: TreeNode) -> list:
    if not root:
        return []

    res = list()
    stack = list()

    while True:
        while root:
            stack.append(root)
            res.append(root.val)
            root = root.left
        if not stack:
            return res

        node = stack.pop()
        root = node.right
