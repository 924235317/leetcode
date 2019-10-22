from treenode import *

def pathSum(root: TreeNode, sum: int) -> list:
    def pathSumCore(root, sum, res, tmp):
        if not root:
            return
        if root and not root.left and not root.right and root.val == sum:
            res.append(tmp+[root.val])
            return
        
        if root.left:
            pathSumCore(root.left, sum-root.val, res, tmp+[root.val])
        if root.right:
            pathSumCore(root.right, sum-root.val, res, tmp+[root.val])
    
    res = list()
    tmp = list()
    pathSumCore(root, sum, res, tmp)
    return res

if __name__ == "__main__":
    l = [5,4,8,11,None,13,4,7,2,None,None,None, None,5,1]
    target = 22
    root = list2treenode(l)
    print_treenode(root)
    print(pathSum(root, target))
