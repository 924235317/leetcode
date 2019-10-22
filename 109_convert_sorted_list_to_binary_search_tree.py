from listnode import *
from treenode import *

def sortedListToBST(head: ListNode) -> TreeNode: 
    
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)

    slow = head
    quick = head.next.next

    while quick and quick.next:
        slow = slow.next
        quick = quick.next.next

    
    tmp = slow.next
    node = TreeNode(tmp.val)
    
    slow.next = None
    node.left = sortedListToBST(head)
    node.right = sortedListToBST(tmp.next)

    return node

if __name__ == "__main__":
    l = [-10,-3,0,5,9]
    l = list2node(l)
    print_node(l)
    root = sortedListToBST(l)
    print_treenode(root)
