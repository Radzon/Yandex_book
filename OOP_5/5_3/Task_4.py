def only_positive_even_sum(*args):
    if any(type(i) is int for i in args):
        raise TypeError
    elif any(i > 0 and i % 2 == 0 for i in args):
        raise ValueError
    else:
        return sum(args)