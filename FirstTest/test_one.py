# Primeiro programa estudando Software Testing em python #
# Autor: Rafael Willian #
# Ferramentas: Python 2.7, PyTest e virtualenv#

def func(x):
    return x + 1

def test_answer(): #Essa função será executada para fins de teste
    assert func(3) == 4 # No caso de a condição ser falsa, o programa indica falha