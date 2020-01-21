def hasCycle(head: ListNode) -> bool:
    if not head:
        return False

    slow = head
    fast = head.next

    while slow and fast:
        if slow == fast:
            return True

        if not fast.next:
            return False

        fast = fast.next.next
        slow = slow.next

    return False
