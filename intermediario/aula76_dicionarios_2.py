# Manipulando chaves e valores

person = {}

##
##

chave = 'name'
surname = 'surname'

person[chave] = 'Wendher'
person[surname] = 'Gerson'

print(person[chave])

person[chave] = 'Maria'

del person[surname]
print(person)
print(person[chave])

if person.get(surname) is None:
    print('NAO EXISTE')
else:
    print(person[surname])

# print('isso nao vai')