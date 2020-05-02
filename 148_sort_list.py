from listnode import *

#useless
def sortList(head):
    def merge(head1, head2):
        print("vvv")
        print_node(head1)
        print_node(head2)
        dummy = ListNode(-1)
        cur = dummy
        while head1 and head2:
            if head1.val > head2.val:
                cur.next = head2
                head2 = head2.next
            else:
                cur.next = head1
                head1 = head1.next
            cur = cur.next

        print_node(head1)
        print_node(head2)
        cur.next = head1 if head1 else head2
        print_node(dummy.next)
        return dummy.next

    def mergeSort(head):
        if not head.next:
            return head
        
        slow = head
        fast = head
        slow_pre = None
        while fast and fast.next:
            slow_pre = slow
            slow = slow.next
            fast = fast.next.next

        slow_pre.next = None
        head1 = mergeSort(head)
        head2 = mergeSort(slow)
        head = merge(head1, head2)
        return head


    if not head:
        return head

    head = mergeSort(head)

    return head


# time limit
def sortList2(head):
    def quickSort(start, end):
        if start == end or not start or not end:
            return
        if start.next == end:
            min_val = min(start.val, end.val)
            max_val = max(start.val, end.val)
            start.val, end.val = min_val, max_val
            return

        tmp = start.val
        mid = start
        equal = start.next
        end = start.next

        while end and end.next:
            if end.val < tmp:
                mid = mid.next
                mid.val, end.val = end.val, mid.val
            elif end.val == tmp:
                equal.val, end.val = end.val, equal.val
                equal = equal.next

            end = end.next
        
        if end.val < tmp:
            mid = mid.next
            mid.val, end.val = end.val, mid.val
        elif end.val == tmp:
            equal = equal.next
            equal.val, end.val = end.val, equal.val

        start.val, mid.val = mid.val, start.val

        if start.val != mid.val:
            quickSort(start, mid)
        if equal.val != end.val:
            quickSort(equal.next, end)
    
    
    if not head or not head.next:
        return head

    end = head
    while end and end.next:
        end = end.next

    quickSort(head, end)
    return head


def sortList3(head):
    def split(head, n):
        for i in range(1, n):
            if not head:
                break
            head = head.next

        if not head:
            return head

        second = head.next
        head.next = None
        return second
    
    
    #merge the two sorted linked list l1 and l2,
    #then append the merged sorted linked list to the node head
    #return the tail of the merged sorted linked list
    def merge(head1, head2, head):
        cur = head
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                cur = head1
                head1 = head1.next
            else:
                cur.next = head2
                cur = head2
                head2 = head2.next

        cur.next = head1 if head1 else head2
        while cur.next:
            cur = cur.next
        
        return cur


    if not head or not head.next:
        return head

    cur = head
    length = 0
    while cur:
        length += 1
        cur = cur.next

    dummy = ListNode(-1)
    dummy.next = head
    step = 1
    while step < length:
        cur = dummy.next
        tail = dummy
        while cur:
            left = cur
            right = split(left, step)
            print_node(left)
            print_node(right)
            cur = split(right, step)
            tail = merge(left, right, tail)
        step *= 2

    return dummy.next

if __name__ == "__main__":
    
    l = [-84,142,41,-17,-71,170,186,183,-21,-76,76,10,29,81,112,-39,-6,-43,58,41,111,33,69,97,-38,82,-44,-7,99,135,42,150,149,-21,-30,164,153,92,180,-61,99,-81,147,109,34,98,14,178,105,5,43,46,40,-37,23,16,123,-53,34,192,-73,94,39,96,115,88,-31,-96,106,131,64,189,-91,-34,-56,-22,105,104,22,-31,-43,90,96,65,-85,184,85,90,118,152,-31,161,22,104,-85,160,120,-31,144,115]

    
    l = [-3,-2,-1, -3,-3, -2,-1 ,-4,1,2,3,4]
    l = [-1,5,3,4,0]
    l = [4,2,1,3]

    l = list2node(l)
    print_node(l)
    l = sortList(l)
    print_node(l)

        
            
       
