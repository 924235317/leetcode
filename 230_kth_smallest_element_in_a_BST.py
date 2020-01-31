def kthSmallest(self, root: TreeNode, k: int) -> int:
    if not root or self.global_idx > k:
        return self.res
    
    self.kthSmallest(root.left, k)
    self.global_idx += 1
    if self.global_idx == k:
        self.res = root.val
        return self.res
    self.kthSmallest(root.right, k)
    return self.res

def kthSmallest(self, root: TreeNode, k: int) -> int:
    if not root:
        return None

    stack = list()
    cur = root
    while k > 0:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val

        cur = cur.right
