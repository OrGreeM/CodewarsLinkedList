class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



def get_nth(node, index):
    if index <0:
        raise IndexError
    while node is not None and index > 0:
        node = node.next
        index -= 1

    if node is None:
        raise IndexError
    return node
