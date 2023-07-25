# funcoes decoradoras e decoradores
# decorar = adicionar / remover / restringir / alternar
# funcoes decoradas sao funcoes que decoram outras funcoes
# decoradores sao usados para fazer o python usar as funcoes decoradas em outras funcoes
# decoradores sao Syntax Sugar (acucar sintatico)


def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        result = func(*args, **kwargs)
        print("Eae")
        return result
    return interna


@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def e_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError("Parametro deve ser uma string")


invercao = inverte_string("123")
print(invercao)
