__author__ = 'Paulo Stocker - STK <stkstocker@gmail.com>'
'''Construir um programa que efetue o c�lculo do
sal�rio l�quido de um professor. Para fazer este
programa, voc� dever� possuir alguns dados, tais
como: valor da hora aula, n�mero de horas trabalhadas
no m�s e percentual de desconto do INSS. Em primeiro
lugar, deve-se estabelecer qual ser� o seu sal�rio
bruto para efetuar o desconto e ter o valor do sal�rio
l�quido.'''
print("Digite o valor da hora aula")
valhora = float(input())
print("Digite o numero de horas trabalhadas")
numhoras = float(input())
print("Digite o percentual de desconto do INSS")
percdesc = float(input())
salbruto = valhora * numhoras
print("O valor do salario bruto e: ", salbruto)
valdesc = (salbruto * percdesc) / 100
salliq = salbruto - valdesc
print("O valor do salario liquido e: ", salliq)
