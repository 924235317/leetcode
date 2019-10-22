from treenode import *

def recoverTree(root: TreeNode) -> None:
    def recoverTreeCore(root, first, second, pre):
        if not root:
            return first, second, pre

        first, second, pre = recoverTreeCore(root.left, first, second, pre)
        if not first and pre and pre.val > root.val:
            first = pre
        if first and pre and pre.val > root.val:
            second = root
        pre = root
        first, second, pre = recoverTreeCore(root.right, first, second, pre)
        return first, second, pre
        
    first = None
    second = None
    pre = None
    
    first, second, pre = recoverTreeCore(root, first, second, pre)
    if first and second:
        first.val, second.val = second.val, first.val

if __name__ == "__main__":
    l = [1, 3, None, None, 2] 
    root = list2treenode(l)
    print_treenode(root)
    recoverTree(root)
    print_treenode(root)
