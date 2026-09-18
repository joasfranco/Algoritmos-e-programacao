
baseMisto ='pao'
recheio1 = 'presunto'
recheio2 = 'queijo'


num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

soma = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2

if(num1 % 2 == 0):
    print("O primeiro numero e par!")
else:
    print("O primeiro numero e impar!")

if(num2 % 2 == 0):
    print("O segundo numero e par!")
else:
    print("O segundo numero e impar!")

print("SOMA: ", soma)
print("SUBTRACAO: ", subtracao)
print("DIVISAO: ", divisao)
print("MULTIPLICACAO: ", multiplicacao)
