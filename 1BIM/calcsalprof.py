__author__ = 'Paulo Stocker - STK <stkstocker@gmail.com>'

valHora = float(input("Digite o valor da hora aula: "))
numHoras = float(input("Digite o numero de horas trabalhadas: "))
percDesc = float(input("Digite o percentual de desconto do INSS: "))
valBruto = valHora * numHoras
print("O valor do salario bruto e: ", valBruto)
valDesc = (valBruto * percDesc) / 100
valLiq = valBruto - valDesc
print("O valor do salario liquido e: ", valLiq)
