class Node(object):

    def __init__(self, data):

        self.data = data

        self.next = None



class Context(object):

    def __init__(self, source, dest):

        self.source = source

        self.dest = dest



def move_node(source, dest):
    if source is None:
        raise ValueError


    source_head = source.next

    dest_head = source
    dest_head.next = dest

    return Context(source_head, dest_head)
