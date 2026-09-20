valorA = int(input("Digite o valor de A: "))
print("Valor de A = ", valorA)

if (type(valorA) == int):
    print("Valor de A aceito.")

valorB = int(input("Digite o valor de B: "))
print("Valor de B = ", valorB)

if (type(valorB) == int):
    print("Valor de B aceito.")

if (valorA>valorB):
    print(valorA , " > " , valorB, " Proposição verdadeira (a > b).")

else:
    print(valorA, " < " , valorB, " Proposição Falsa (a > b).") 
