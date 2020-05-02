from listnode import *

def insertionSortList(head):
    if not head or not head.next:
        return head

    
    dummy = ListNode(-2**31)
    dummy.next = head

    cur = head.next
    pre = head
    while cur:
        pre_head = dummy
        cur_head = dummy.next
        while cur_head.val <= cur.val and cur_head != cur:
            pre_head = cur_head
            cur_head = cur_head.next
        
        if cur_head != cur:
            pre.next = cur.next
            pre_head.next = cur
            cur.next = cur_head
            cur = pre.next
        else:
            pre = cur
            cur = pre.next 
    
    return dummy.next


if __name__ == "__main__":
    l = [5,2,3,3,1]
    l = list2node(l)
    print_node(l)
    l = insertionSortList(l)
    print_node(l)


    
