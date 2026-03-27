class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:

    ll = list_repr.split(' -> ')[:-1]

    head = None
    for i in reversed(ll):
        head = Node(int(i), head)
    return head
