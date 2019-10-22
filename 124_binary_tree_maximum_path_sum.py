from treenode import *

max_sum = -2**31

def maxPathSum(root: TreeNode) -> int:
    global max_sum
   
    def maxPathSumCore(root, cur_sum):
        global max_sum
        if not root:
            return 0

        left_sum = max(maxPathSumCore(root.left, cur_sum), 0)
        right_sum = max(maxPathSumCore(root.right, cur_sum), 0)
        max_sum = max(max_sum, root.val+left_sum+right_sum)

        return root.val + max(left_sum, right_sum)
    
    if not root:
        return 0

    cur_sum = 0
    maxPathSumCore(root, cur_sum)
    return max_sum


if __name__ == "__main__":
    #l = [-10,9,20,None,None,15,7]
    l = [2, -1]
    t = list2treenode(l)
    print_treenode(t)
    print(maxPathSum(t))

    

