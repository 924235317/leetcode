class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def buildTree(preorder: list, inorder: list) -> TreeNode:
    if not preorder or not inorder:
        return None

     node_val = preorder.pop(0)
     root = TreeNode(node_val)
     inorderIndex = inorder.index(node_val)

     root.left = self.buildTree(preorder, indorder[0: inorderIndex+1])
     root.right = self.buildTree(preorder, indorder[inorderIndex+1:])

     return root
