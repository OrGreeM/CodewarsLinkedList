
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    probe = head

    if head is None or head.next is None:
        return head

    while probe is not None:
        if probe.next is not None and probe.data == probe.next.data:
            probe.next = probe.next.next
        else:
            probe = probe.next
    return head
