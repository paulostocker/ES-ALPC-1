__author__ = 'Paulo Stocker - STK <stkstocker@gmail.com>'
print("Digite a altura")
altura = float(input())
print("Digite o sexo: [M]asc ou [F]eminino")
sexo = input()
if sexo == "M" or sexo == "m":
    print("Sexo Masculino...")
    pesoideal = (72.7 * altura) - 58
else:
    print("Sexo Feminino")
    pesoideal = (62.1 * altura) - 44.7
print("O seu peso ideal e: ", pesoideal)
