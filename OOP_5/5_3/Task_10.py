import hashlib


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password, min_length=8, possible_chars='abcdefghijklmnopqrstuvwxyz1234567890',
                        at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError
    if len(password) < min_length:
         raise MinLengthError('MinLengthError')
    if not all(i.lower() in possible_chars for i in password):
        raise PossibleCharError('PossibleCharError')
    if not at_least_one:
        raise NeedCharError('NeedCharError')
    return hashlib.sha256(password.encode()).hexdigest()


print(password_validation(
    "$uNri$e_777",
    min_length=6,
    at_least_one=lambda char: char in "!@#$%^&*()_"
))
