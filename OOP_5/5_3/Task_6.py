class InfiniteSolutionsError(Exception):
    pass


class NoSolutionsError(Exception):
    pass


def find_roots(*nums):
    a, b, c = nums
    if a == 0:
        if b == 0:
            if c == 0:
                raise InfiniteSolutionsError('InfiniteSolutionsError')
            else:
                raise NoSolutionsError('NoSolutionsError')
        else:
            return -c / b
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            raise NoSolutionsError('NoSolutionsError')
        else:
            x1 = (-b - d ** 0.5) / (2 * a)
            x2 = (-b + d ** 0.5) / (2 * a)
            if x1 > x2:
                return x2, x1
            else:
                return x1, x2


print(find_roots(0, 0, 1))
