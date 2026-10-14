
anuncios = []
proximo_id = 1

opcao = 0

while opcao != 5:
    print("\n===== OLX - MENU =====")
    print("1. Criar anúncio")
    print("2. Ver anúncios")
    print("3. Modificar anúncio")
    print("4. Deletar anúncio")
    print("5. Sair")

    opcao = int(input("Escolha uma opção: "))

    # CREATE
    if opcao == 1:
        anuncio = {}

        anuncio["id"] = proximo_id
        anuncio["titulo"] = input("Título: ")
        anuncio["descricao"] = input("Descrição: ")
        anuncio["preco"] = float(input("Preço: "))
        anuncio["categoria"] = input("Categoria: ")
        anuncio["vendedor"] = input("Vendedor: ")
        anuncio["localizacao"] = input("Localização: ")

        anuncios = anuncios + [anuncio]
        proximo_id += 1

        print("Anúncio cadastrado com sucesso!")

    # READ
    elif opcao == 2:
        if len(anuncios) == 0:
            print("Não existem anúncios cadastrados.")
        else:
            for anuncio in anuncios:
                print("\n--------------------")
                print("ID:", anuncio["id"])
                print("Título:", anuncio["titulo"])
                print("Descrição:", anuncio["descricao"])
                print("Preço: R$", anuncio["preco"])
                print("Categoria:", anuncio["categoria"])
                print("Vendedor:", anuncio["vendedor"])
                print("Localização:", anuncio["localizacao"])

    # UPDATE
    elif opcao == 3:
        id_busca = int(input("Digite o ID do anúncio: "))
        encontrado = False

        for anuncio in anuncios:
            if anuncio["id"] == id_busca:
                encontrado = True

                print("Deixe um campo vazio para manter o valor atual.")

                titulo = input("Novo título: ")
                if titulo != "":
                    anuncio["titulo"] = titulo

                descricao = input("Nova descrição: ")
                if descricao != "":
                    anuncio["descricao"] = descricao

                preco = input("Novo preço: ")
                if preco != "":
                    anuncio["preco"] = float(preco)

                categoria = input("Nova categoria: ")
                if categoria != "":
                    anuncio["categoria"] = categoria

                vendedor = input("Novo vendedor: ")
                if vendedor != "":
                    anuncio["vendedor"] = vendedor

                localizacao = input("Nova localização: ")
                if localizacao != "":
                    anuncio["localizacao"] = localizacao

                print("Anúncio atualizado!")
                break

        if encontrado == False:
            print("Anúncio não encontrado.")

    # DELETE
    elif opcao == 4:
        id_busca = int(input("Digite o ID do anúncio que deseja excluir: "))
        encontrado = False
        indice = 0

        while indice < len(anuncios):
            if anuncios[indice]["id"] == id_busca:
                encontrado = True
                anuncios = (
                    anuncios[:indice] + anuncios[indice + 1:]
                )
                print("Anúncio removido com sucesso!")
                break

            indice += 1

        if encontrado == False:
            print("Anúncio não encontrado.")

    elif opcao == 5:
        print("Encerrando o programa...")

    else:
        print("Opção inválida!")
