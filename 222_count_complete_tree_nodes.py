def countNodes(root):
    if not root:
        return 0
    
    lh, rh = 0, 0
    left, right = root, root
    while left.left:
        left = left.left
        lh += 1

    while right.right:
        right = right.right
        rh += 1

    if lh == rh:
        return 2 ** (lh + 1) - 1

    else:
        return 1 + countNodes(root.left) + countNodes(root.right)
