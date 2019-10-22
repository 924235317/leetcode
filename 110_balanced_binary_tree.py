def isBalanced(self, root: TreeNode) -> bool:
    def depth(root):
        if not root:
            return 0
        
        l_depth = depth(root.left)
        r_depth = depth(root.right)
        return max(l_depth, r_depth) + 1
    
    if not root:
        return True
    
    l_depth = depth(root.left)
    r_depth = depth(root.right)
    
    if abs(l_depth - r_depth) <= 1:
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    else:
        return False

def isBalanced(self, root: TreeNode) -> bool:
    def depth(root):
        if not root:
            return 0
        
        l = depth(root.left)
        r = depth(root.right)
        
        if abs(l - r) > 1 or l == -1 or r == -1:
            return -1
        else:
            return max(l, r) + 1
      
    d = depth(root)
    return True if d != -1 else False
