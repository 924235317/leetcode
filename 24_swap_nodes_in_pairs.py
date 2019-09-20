from listnode import *

def swapPairs(head: ListNode) -> ListNode:
    
    dummy = ListNode(-1)
    dummy.next = head
    pre = dummy
    while head and head.next:
        pre.next = head.next
        head.next = head.next.next
        pre.next.next = head

        pre = head
        head = head.next
    return dummy.next

if __name__ == "__main__":
    l = [1,2,3,4, 5]
    l = list2node(l)
    print_node(l)
    print_node(swapPairs(l))
        
