def deleteNode(root, key):
    def core(node):
        if not node.left:
            return node.right
        else:
            tmp = node.left
            while tmp.right:
                tmp = tmp.right
            
            tmp.right = node.right
        return node.left

    if not root:
        return root

    queue = list()
    dummy = TreeNode(-1)
    dummy.left = root

    queue.append(dummy)
    while queue:
        cur = queue.pop(0)

        if cur.left:
            if cur.left.val == key:
                cur.left = core(cur.left)
                break
            else:
                queue.append(cur.left)
        if cur.right:
            if cur.right.val == key:
                cur.right = core(cur.right)
                break
            else:
                queue.append(cur.right)

    return dummy.left
