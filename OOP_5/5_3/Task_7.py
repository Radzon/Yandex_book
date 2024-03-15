class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    ru_alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if not isinstance(name, str):
        raise TypeError
    elif not all(i.lower() in ru_alf for i in name):
        raise CyrillicError('CyrillicError')
    elif not name.istitle():
        raise CapitalError('CapitalError')
    return name


n = "Аааа"
print(name_validation(n))
