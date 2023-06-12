"""
iteravel: str, range,etc (__iter__)
iterador: quem sabe entregar um valor por vez
next: me entregue o proximo valor
iter: me entregue seu iterador
"""
# texto = iter('wendher') # __iter__

# print(next(texto)) #__next__()
# print(next(texto)) #__next__()
# print(next(texto)) #__next__()
# print(next(texto)) #__next__()
# print(next(texto)) #__next__()
# print(next(texto)) #__next__()
# print(next(texto)) #__next__()

# for letra in texto

texto = 'Wendher' # iterável
iterador = iter(texto) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

for letra in texto:
    print(letra)