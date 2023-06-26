import importlib

import aula98_module

print(aula98_module.variavel)

for i in range(10):
    importlib.reload(aula98_module)
    print(i)

print('end')