class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list2node(l: list) -> ListNode:
    head = None
    tmp = head
    for i in range(len(l)):
        if head == None:
            head = ListNode(l[i])
            tmp = head
        else:
            tmp.next = ListNode(l[i])
            tmp = tmp.next
    return head

def print_node(head: ListNode):
    tmp = head
    res = list()
    while tmp is not None:
        res.append(tmp.val)
        tmp = tmp.next

    print(res)
