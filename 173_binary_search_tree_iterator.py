from treenode import *
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = list()
        
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        top = self.stack.pop()
        if top.right:
            t = top.right
            while t:
                self.stack.append(t)
                t = t.left
        return top.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
