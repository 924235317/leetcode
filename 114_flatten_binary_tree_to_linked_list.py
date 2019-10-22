from treenode import *

def flatten(root: TreeNode) -> None:
    def flattenCore(root):
        if root and not root.left and not root.right:
            return root

        if root.left and root.right:
            tmp = root.right
            t = flattenCore(root.left)
            root.right = root.left
            t.right = tmp
            root.left = None
            return flattenCore(tmp)
        elif root.left:
            t = flattenCore(root.left)
            root.right = root.left
            root.left = None
            return t
        elif root.right:
            root.left = None
            return flattenCore(root.right)
    
    if not roort:
        return None
    t = flattenCore(root)
    t.right = None


if __name__ == "__main__":
    l = [1,2,3,4,5]
    root = list2treenode(l)
    print_treenode(root)
    flatten(root)
    print_treenode(root)
