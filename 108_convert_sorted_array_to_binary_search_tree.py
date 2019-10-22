from treenode import *

def sortedArrayToBST(nums: list) -> TreeNode:
    if not nums:
        return None

    if len(nums) == 1:
        return TreeNode(nums[0])

    l = 0
    r = len(nums)-1
    m = (l+r) // 2
    node = TreeNode(nums[m])
    node.left = sortedArrayToBST(nums[0:m])
    node.right = sortedArrayToBST(nums[m+1:])

    return node


if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    print(nums)
    root = sortedArrayToBST(nums)

    print_treenode(root)

