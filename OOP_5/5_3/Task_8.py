class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name):
    ru_alf = 'abcdefghijklmnopqrstuvwxyz_1234567890'
    if not isinstance(name, str):
        raise TypeError
    elif not all(i.lower() in ru_alf for i in name):
        raise BadCharacterError('BadCharacterError ')
    elif name[0].isdigit():
        raise StartsWithDigitError('StartsWithDigitError')
    return name


# print(username_validation("$user_45$"))
print(username_validation("45_user"))