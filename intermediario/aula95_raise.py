# raise - lançando exceçoes (erros)

def no_zero_accept(d):
    if d == 0:
        raise ZeroDivisionError('ERROR: You are trying to divide by 0.')
    return True

def must_be_int_or_float(n):
    type_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'ERROR: "{n}" must be int or float!\n'
            f'The "{type_n.__name__}" that was sent.'
        )
    return True

def division(n, d):
    must_be_int_or_float(n)
    must_be_int_or_float(d)
    no_zero_accept(d)
    return n / d

print(division(1, '0'))