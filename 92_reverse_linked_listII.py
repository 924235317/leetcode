from listnode import *

def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    if not head or not head.next:
        return head

    dummy = ListNode(-1)
    dummy.next = head
    pre = dummy
    cur = head
    for i in range(m):
        pre = cur
        cur = cur.next

    for i in range(n-m):
        tmp = pre.next
        pre.next = cur.next
        cur.next = cur.next.next
        pre.next.next = tmp
        

    return dummy.next

if __name__ == "__main__":
    l = [5,4,3,2,1]
    head = list2node(l)
    print_node(head)
    head = reverseBetween(head, 1, 4)
    print_node(head)
