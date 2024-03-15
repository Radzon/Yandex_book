def merge(*args):
    check_iter(args[0], args[1])
    check_type_data(args[0], args[1])
    check_sort(args[0], args[1])
    queue_1 = list(args[0])
    queue_2 = list(args[1])
    sequence = []
    while queue_1 and queue_2:
        if queue_1[0] > queue_2[0]:
            sequence.append(queue_2.pop(0))
        else:
            sequence.append(queue_1.pop(0))
    sequence.extend(queue_1)
    sequence.extend(queue_2)
    return tuple(sequence)


def check_iter(a, b):
    if not (hasattr(a, '__iter__') and hasattr(b, '__iter__')):
        raise StopIteration


def check_type_data(a, b):
    if type(a[0]) is type(b[0]):
        if not all(type(a[0]) is type(i) for i in a):
            raise TypeError
        elif not all(type(b[0]) is type(i) for i in b):
            raise TypeError
    else:
        raise TypeError


def check_sort(*queues):
    for queue in queues:
        if list(queue) != sorted(queue):
            raise ValueError
    return True
