from listnode import *

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    dummy = ListNode(-1)
    head = dummy
    while l1 and l2:
        if l1.val >= l2.val:
            head.next = l2
            head = head.next
            l2 = l2.next
        else:
            head.next = l1
            head = head.next
            l1 = l1.next
    
    if l1:
        head.next = l1

    if l2:
        head.next = l2

    return dummy.next

if __name__ == "__main__":
    l1 = [1,2,4]
    l2 = [1,3,4]
    l1 = list2node(l1)
    l2 = list2node(l2)
    print_node(l1)
    print_node(l2)
    print_node(mergeTwoLists(l1, l2))
