class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
def connect(self, root: Node) -> Node:
    if not root:
        return root

    start = root
    dummy = Node(-1, None, None, None)
    pre = dummy
    while start:
        cur = start
        while cur:
            if cur.left:
                pre.next = cur.left
                pre = cur.left
            if cur.right:
                pre.next = cur.right
                pre = cur.right
            cur = cur.next

        start = dummy.next
        pre = dummy
        dummy.next = None
    return root
