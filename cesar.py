import sys
import string

frase = 'aol pualyula? pz aoha aopun zapss hyvbuk? ovtly zptwzvu'
alfabeto = string.ascii_lowercase
resultado = ''
rotacao = 7
for letra in frase:
    if letra in alfabeto:
        posicao= alfabeto.find(letra)
        posicao= (posicao - rotacao) % 26
        resultado = resultado + alfabeto[posicao]
return resultado


