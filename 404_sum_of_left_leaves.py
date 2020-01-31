def sumOfLeftLeaves(root):
    if not root:
        return 0

    s = 0
    if root.left and not root.left.left and not root.left.right:
        s += root.left.val

    s += sumOfLeftLeaves(root.right)
    s += sumOfLeftLeaves(root.left)
    return s
