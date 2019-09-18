from listnode import *

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2:
        return None

    flag = 0
    dummy = ListNode(-1)
    head = dummy
    
    while l1 or l2 or flag:
        tmp = 0
        if l1:
            tmp += l1.val
            l1 = l1.next
        if l2:
            tmp += l2.val
            l2 = l2.next
        if flag:
            tmp += flag
            
        flag = tmp // 10
        tmp = tmp % 10
        head.next = ListNode(tmp)
        head = head.next

    return dummy.next

if __name__ == "__main__":
    l1 = [2, 4, 3, 4]
    l2 = [5, 6, 4]
    l1 = list2node(l1)
    l2 = list2node(l2)
    print_node(l1)
    print_node(l2)
    print_node(addTwoNumbers(l1, l2))
    
