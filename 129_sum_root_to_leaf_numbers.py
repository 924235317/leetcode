from treenode import *

res = 0

def sumNumbers(root: TreeNode) -> int:
    global res
    def sumNumbersCore(root, cur):
        global res
        cur = cur * 10 + root.val
        if not root.left and not root.right:
            res += cur

        if root.left:
            sumNumbersCore(root.left, cur)
        if root.right:
            sumNumbersCore(root.right, cur)

    if not root:
        return 0

    cur = 0
    sumNumbersCore(root, cur)
    return res



if __name__ == "__main__":
    l = [4,9,0,5,1]
    root = list2treenode(l)
    print_treenode(root)
    print(sumNumbers(root))

        
