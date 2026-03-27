class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head

    dummyNode = Node()
    dummyNode.next = head

    prev = dummyNode
    curr = head

    while curr and curr.next:
        first = curr
        second = curr.next
        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
        curr = first.next

    return dummyNode.next
