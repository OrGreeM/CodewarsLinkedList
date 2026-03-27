
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    new_node = Node(data)

    if head is None or data <= head.data:
        new_node.next = head
        return new_node

    probe = head
    prev_probe = None

    while probe is not None and data > probe.data:
        prev_probe = probe
        probe = probe.next

    new_node.next = probe
    prev_probe.next = new_node

    return head
