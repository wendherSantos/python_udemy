# funcoes decoradoras e decoradores
# decorar = adicionar / remover / restringir / alternar
# funcoes decoradas sao funcoes que decoram outras funcoes
# decoradores sao usados para fazer o python usar as funcoes decoradas em outras
# funcoes


def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        result = func(*args, **kwargs)
        return result

    return interna


def inverte_string(string):
    return string[::-1]


def e_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError("Parametro deve ser uma string")


inverte_string_checando_parametro = criar_funcao(inverte_string)
invercao = inverte_string_checando_parametro(123)
print(invercao)
