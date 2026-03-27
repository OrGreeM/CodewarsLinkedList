
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    node = Node(data)
    node.next = head
    head = node

    return head

def build_one_two_three():
    head = None

    for i in range(3, 0, -1):
        head = push(head, i)
