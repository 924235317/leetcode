class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
def connect(self, root: Node) -> Node:
    if not root:
        return root

    tmp = list()
    tmp.append(root)
    tmp.append(None)
    last = None
    
    while tmp:
        cur = tmp.pop(0)
        if last:
            last.next = cur
        last = cur
        if cur is None:
            if len(tmp) > 0:
                tmp.append(None)
        else:
            if cur.left: 
                tmp.append(cur.left)
            if cur.right:
                tmp.append(cur.right)
            

        
        
