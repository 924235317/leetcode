class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

def list2randomnode(l):
    dummy = Node(-1, None, None)
    head = dummy
    for ll in l:
        new = Node(ll[0], None, None)
        head.next = new
        head = head.next

    head = dummy.next
    idx = 0
    while head:
        if l[idx][1] is not None:
            p = dummy.next
            for i in range(l[idx][1]):
                p = p.next

            head.random = p
        
        head = head.next
        idx += 1
    return dummy.next

def printnode(root):
    head = root
    print("================")
    while head:
        print(head.val, head)
        if head.random:
            print([head.random.val, head.random])
        else:
            print([None, None])
        head = head.next

def copyRandomList(head: Node) -> Node:
    if not head:
        return None

    dummy = Node(-1, head, None)
    new_head = None
    while head:
        new = Node(head.val, head.next, None) 
        head.next = new
        head = new.next
    
    head = dummy.next
    dummy_head = Node(-1, head.next, None)
    cur = dummy_head.next
    while cur and head:
        if head.random:
            cur.random = head.random.next

        head = cur.next
        cur = cur.next.next if cur.next else cur.next

    head = dummy.next
    cur = dummy_head.next
    while cur:
        if cur.next:
            head.next = cur.next 
            cur.next = cur.next.next
            head = head.next
        else:
            head.next = None
        cur = cur.next
    
    head = dummy.next
    return dummy_head.next

if __name__ == "__main__":
    l = [[1, 2], [2, 0], [3, None]]
    root = list2randomnode(l)
    printnode(root)
    r = copyRandomList(root)
    printnode(root)
    printnode(r)
