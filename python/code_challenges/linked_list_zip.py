from data_structures.linked_list import LinkedList


def zip_lists(list_a, list_b):
    zipped = LinkedList()
    current_a = list_a.head
    current_b = list_b.head
    reversal = []
    while current_a or current_b:
        if current_a:
            reversal.append(current_a.value)
            current_a = current_a.next
        if current_b:
            reversal.append(current_b.value)
            current_b = current_b.next

    for value in reversed(reversal):
        zipped.insert(value)

    return zipped
