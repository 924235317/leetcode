from listnode import *

def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head:
        return None
    
    if head.next == None:
        return head
    
    length = 1
    last_node = head
    while last_node.next != None:
        last_node = last_node.next
        length += 1
    last_node.next = head

    true_k = k % length
    pre_node = last_node
    pos_move = length - true_k
    for i in range(pos_move):
        pre_node = head
        head = head.next
    pre_node.next = None
    return head


if __name__ == "__main__":
    l = [1,2,3,4]
    head = list2node(l)
    print_node(head)

    t = rotateRight(head, 3)
    print_node(t)
