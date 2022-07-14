#Calculadora para uso pessoal
from ast import While
from funcoes.calcular import Calcular

Cal_ligado = True
valor_primário = int(input(': '))
operação = input('[+], [-], [/], [*], [Exit]: ')
valor_secundario = int(input(': '))
if operação == '+':
    função = Calcular(valor_primário, valor_secundario)
    função.soma()
    while Cal_ligado:
        operação = input('[+], [-], [/], [*], [Exit]: ')
        valor_secundario = int(input(': '))
        if operação == '+':
            função.valor_secundario = valor_secundario
            função.soma()
        elif operação == '-':
            função.valor_secundario = valor_secundario
            função.subtração()
        elif operação == '*':
            função.valor_secundario = valor_secundario
            função.multiplicação()
        elif operação == '/':
            função.valor_secundario = valor_secundario
            função.divisão()





