class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    string = []
    while node is not None:
        string.append(str(node.data))
        node = node.next

    string.append(str(node))

    return ' -> '.join(string)
