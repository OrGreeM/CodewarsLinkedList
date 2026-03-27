class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise ValueError

    head1 = head
    head2 = head.next

    curr1 = head1
    curr2 = head2

    while curr1 and curr2:
        curr1.next = curr2.next
        curr1 = curr1.next

        if curr1:
            curr2.next = curr1.next
            curr2 = curr2.next

    return Context(head1, head2)
