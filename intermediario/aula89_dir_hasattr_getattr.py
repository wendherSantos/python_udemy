# dir, hasattr e getattr in Python

string = 'Wendher'
method = 'strip'

if hasattr(string, method):
    print(f'There is the {method} method.')
    print(getattr(string, method)())
else:
    print(f'There is no {method} method.')