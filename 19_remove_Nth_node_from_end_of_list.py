from listnode import *

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    if not head:
        return None

    dummy = ListNode(-1)
    dummy.next = head
    p = dummy
    l = head
    r = head
    for i in range(n):
        if not r:
            return head
        r = r.next

    while r:
        p = l
        l = l.next
        r = r.next

    p.next = l.next
    
    return dummy.next


if __name__ == "__main__":
    l = [1,2,3,4,5]
    n = 2
    head = list2node(l)
    print_node(head)
    print_node(removeNthFromEnd(head, n))
