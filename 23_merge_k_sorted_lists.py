from listnode import *

def mergeKLists(lists: list) -> ListNode:
    def merge(list1: list, list2: list) -> ListNode:
        if not list1:
            return list2

        if not list2:
            return list1

        dummy = ListNode(-1)
        p = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next

            p = p.next

        p.next = list1 if list1 else list2
        return dummy.next

    if len(lists) < 1:
        return []
    
    if len(lists) == 1:
        return lists[0]
    
    half = len(lists) // 2
    p1 = mergeKLists(lists[:half])
    p2 = mergeKLists(lists[half:])

    return merge(p1, p2)


if __name__ == "__main__":
    lists = [[1,4,5],[1,3,4],[2,6]]
    lists = [list2node(i) for i in lists]
    print_node(mergeKLists(lists))
