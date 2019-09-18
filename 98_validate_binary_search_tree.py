from treenode import *

def isValidBST(root: TreeNode) -> bool:
    def isValidBSTCore(root: TreeNode, min_node: TreeNode, max_node: TreeNode) -> bool:
        if not root:
            return True

        if (min_node and root.val <= min_node.val) or (max_node and root.val >= max_node.val):
            return False

        return isValidBSTCore(root.left, min_node, root) and isValidBSTCore(root.right, root, max_node)

    return isValidBSTCore(root, None, None)


