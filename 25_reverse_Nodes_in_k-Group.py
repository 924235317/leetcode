from listnode import *

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    
    dummy = ListNode(-1)
    dummy.next = head
    pre = dummy

    while True:
        r = head
        c = 1
        while r and c < k:
            r = r.next
            c += 1
        if c == k and r:
            count = 1
            while head and head.next and count < k:
                tmp = pre.next
                pre.next = head.next
                head.next = head.next.next
                pre.next.next = tmp
                count += 1
            pre = head
            head = head.next
        else:
            return dummy.next

if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9,10, 11]
    k = 3
    head = list2node(l)
    print_node(head)
    print_node(reverseKGroup(head, k))

