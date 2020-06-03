# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/submissions/

def procura_palavra(frase, palavra_busca):
    palavras = frase.split(" ")
    for index, uma_palavra in enumerate(palavras):
        if palavra_busca in uma_palavra and palavra_busca[0] == uma_palavra[0]:
            return index + 1
    return -1
    
def primeiro_teste():
    frase = "bom dia para todos"
    palavra = "pa"
    resultado = procura_palavra(frase, palavra)
    esperado = 3
    assert resultado == esperado

def segundo_teste(): 
    frase = "love"
    palavra = "love"
    resultado = procura_palavra(frase, palavra)
    esperado = 1@Lucbm
    assert resultado == esperado

def terceiro_teste(): 
    frase = "i am tired"
    palavra = "you"
    resultado = procura_palavra(frase, palavra)
    esperado = -1
    assert resultado == esperado

def quarto_teste(): 
    frase = "hellohello hellohellohello"
    palavra = "ell"
    resultado = procura_palavra(frase, palavra)
    esperado = -1
    assert resultado == esperado

def quinto_teste(): 
    frase = "hellohello hellohelloheiiillo"
    palavra = "hei"
    resultado = procura_palavra(frase, palavra)
    esperado = -1
    assert resultado == esperado
    
primeiro_teste()
segundo_teste()
terceiro_teste()
quarto_teste()
quinto_teste()