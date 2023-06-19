# Truthy and Falsy Values, Mutable and Immutable Types
# Mutable: [] {} set()
# Immutable: () "" 0 0.0 None False range(0, 10)

lst = []
dict_ = {}
set_ = set()
tuple_ = ()
string = ''
integer = 0
float_ = 0.0
none = None
false = False
interval = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'Test |', falsy('test'))
print(f'{lst=} |', falsy(lst))
print(f'{dict_=} |', falsy(dict_))
print(f'{set_=} |', falsy(set_))
print(f'{tuple_=} |', falsy(tuple_))
print(f'{string=} |', falsy(string))
print(f'{integer=} |', falsy(integer))
print(f'{float_=} |', falsy(float_))
print(f'{none=} |', falsy(none))
print(f'{false=} |', falsy(false))
print(f'{interval=} |', falsy(interval))

