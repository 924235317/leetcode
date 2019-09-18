from random import randint

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
    
def gen_random_list(n):
    dummy = ListNode(-1)
    idx = dummy
    for i in range(n):
        idx.next = ListNode(randint(1, 10))
        print(11111, idx.next.val)
        idx = idx.next
        
    return dummy.next

def print_list(l):
    head = l
    while head is not None:
        print(head.val)
        head = head.next


def partition(head: ListNode, x: int) -> ListNode:
    if not head or head.next is None:
        return head

    dummy_less = ListNode(-1)
    dummy_more = ListNode(-1)
    idx_less = dummy_less
    idx_more = dummy_more
    
    while head is not None:
        #print(1, head.val)
        if head.val < x:
            idx_less.next = head
            idx_less = idx_less.next
        else:
            idx_more.next = head
            idx_more = idx_more.next
        
        head = head.next
    idx_more.next = None
    idx_less.next = dummy_more.next
    return dummy_less.next


if __name__ == "__main__":
    l = gen_random_list(10)
    print_list(l)
    print("----------------")
    l = partition(l, 7)
    print_list(l)
    
            
