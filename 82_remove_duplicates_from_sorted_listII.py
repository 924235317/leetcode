from listnode import *

def deleteDuplicates(head: ListNode) -> ListNode:
    if not head:
        return None
    
    dummy = ListNode(-1)
    dummy.next = head

    pre = dummy
    cur = head

    while cur and cur.next:
        if cur.next.val == cur.val:
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            cur = cur.next
            pre.next = cur
        else:
            pre = cur
            cur = cur.next

    return dummy.next

if __name__ == "__main__":  
    l = [1,1,2,3,3,3,4,5,5,5]
    head = list2node(l) 
    print_node(head)
    head = deleteDuplicates(head)
    print_node(head)
