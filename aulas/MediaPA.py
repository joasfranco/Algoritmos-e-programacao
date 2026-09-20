def calcular_media():

    qtd_notas = int(input("Quantas notas você deseja inserir? "))

    if qtd_notas <= 0:
        print("A quantidade de notas deve ser maior que zero.")
        return

    notas = []

    
    for i in range(1, qtd_notas + 1):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)


    maior_nota = max(notas)
    media = sum(notas) / len(notas)

   
    if media >= 7.0:
        status = "Aprovado"
    elif media < 5.0:
        status = "Reprovado"
    else:
        status = "Substitutiva"

    
    print("\n--- RESULTADO ---")
    print(f"Maior nota: {maior_nota:.2f}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")



calcular_media()
