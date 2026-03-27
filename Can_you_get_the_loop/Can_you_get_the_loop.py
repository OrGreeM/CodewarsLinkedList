def loop_size(node):

    slow = node
    fast = node

    slow = slow.next
    fast = fast.next.next

    while fast is not None and slow != fast:
        slow = slow.next
        fast = fast.next.next

    if fast is None:
        return 0

    current = slow
    i = 1

    current = current.next
    while current != slow:
        current = current.next
        i += 1
    return i
