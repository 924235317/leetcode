from treenode import *

def buildTree(inorder: list, postorder: list) -> TreeNode:
    if not inorder or not postorder:
        return None

    tmp = postorder.pop(-1)
    node = TreeNode(tmp)
    inorder_idx = inorder.index(tmp)

    node.right = buildTree(inorder[inorder_idx+1:], postorder)
    node.left = buildTree(inorder[:inorder_idx], postorder)

    return node


if __name__ == "__main__":
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    root = buildTree(inorder, postorder)
    print_treenode(root)
