# Programa estudando Software Testing em python #
# Autor: Rafael Willian #
# Ferramentas: Python 2.7, PyTest e virtualenv #

def fatorial(n):
    i = 1
    value = 1
    # Adicionando as duas linhas abaixo test_fatorial_negatico conclui exito #
    #if n < 0:
    #    return 0
    # Colocando a condicao do while como i <= n os fatoriais de 3 e 4 concluem exito#
    while i < n:
        value = value * i
        i = i + 1
    return value

def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorial1():
    assert fatorial(1) == 1

def test_fatorial_negativo():
    assert fatorial(-1) == 0

def test_fatorial3():
    assert fatorial(3) == 6

def test_fatorial4():
    assert fatorial(4) == 24