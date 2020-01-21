def detectCycle(head: ListNode) -> ListNode:
    def hasCycle(head):
        slow = head
        fast = head.next
        
        while slow and fast:
            if slow == fast:
                return slow

            if not fast.next:
                return None

            slow = slow.next
            fast = fast.next.next
        
        return None


    if not head:
        return False

    node_in_cycle = hasCycle(head)
    if not node_in_cycle:
        return -1
    else:
        l = 0
        p = node_in_cycle.next
        while p != node_in_cycle:
            l += 1
            p = p.next
    
    start = head
    end = head
    for i in range(l):
        end = end.next

    while end:
        start = start.next
        end = end.next

    return start

    

