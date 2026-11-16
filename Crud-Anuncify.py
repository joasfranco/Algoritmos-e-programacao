# CRUD de anúncios - Anuncify (só variáveis, if/elif/else e while)
anuncio1 = anuncio2 = anuncio3 = ""  # cada anúncio é um texto só, vazio = espaço livre
opcao = ""

while opcao != "5":
    print("\n--- Anuncify ---\n1. Criar anúncio\n2. Ver anúncios\n3. Modificar anúncio\n4. Deletar anúncio\n5. Sair")
    opcao = input("Escolha: ")
    num = ""

    if opcao == "1":
        if anuncio1 == "":
            num = "1"
        elif anuncio2 == "":
            num = "2"
        elif anuncio3 == "":
            num = "3"
        else:
            print("Não tem mais espaço, delete um anúncio antes.")
    elif opcao == "3" or opcao == "4":
        num = input("Qual anúncio (1, 2 ou 3)? ")
        existe = (num == "1" and anuncio1 != "") or (num == "2" and anuncio2 != "") or (num == "3" and anuncio3 != "")
        if existe == False:
            print("Esse anúncio não existe.")
            num = ""
    elif opcao == "2":
        if anuncio1 + anuncio2 + anuncio3 == "":
            print("Não existem anúncios cadastrados.")
        if anuncio1 != "":
            print("1 -", anuncio1)
        if anuncio2 != "":
            print("2 -", anuncio2)
        if anuncio3 != "":
            print("3 -", anuncio3)
    elif opcao != "5":
        print("Opção inválida.")

    if num != "":  # criar, modificar e deletar terminam aqui
        texto = ""
        if opcao == "4":
            if input("Tem certeza que quer deletar? (s/n): ") != "s":
                print("Exclusão cancelada.")
                num = ""
        else:
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            preco = input("Preço: ")
            if titulo == "" or preco == "":
                print("Título e preço são obrigatórios, o anúncio não foi salvo.")
                num = ""
            else:
                texto = (titulo + " | " + descricao + " | R$ " + preco + " | " + input("Categoria: ")
                         + " | " + input("Vendedor: ") + " | " + input("Localização: "))

    if num == "1":  # só grava se não deu erro lá em cima (num continua preenchido)
        anuncio1 = texto
    elif num == "2":
        anuncio2 = texto
    elif num == "3":
        anuncio3 = texto
    if num != "":
        print("Feito!")
