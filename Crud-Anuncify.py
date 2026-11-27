anuncios = []


def menu():
    print("\n--- ANUNCIFY ---")
    print("1. Criar anúncio")
    print("2. Ver anúncios")
    print("3. Modificar anúncio")
    print("4. Deletar anúncio")
    print("5. Sair")


def criar_anuncio(lista):
    titulo = input("Título: ").strip()
    descricao = input("Descrição: ").strip()
    preco = input("Preço: ").strip()
    categoria = input("Categoria: ").strip()
    vendedor = input("Vendedor: ").strip()
    localizacao = input("Localização: ").strip()

    if titulo == "" or preco == "":
        print("Título e preço são obrigatórios.")
        return

    anuncio = {
        "titulo": titulo,
        "descricao": descricao,
        "preco": preco,
        "categoria": categoria,
        "vendedor": vendedor,
        "localizacao": localizacao,
    }
    lista.append(anuncio)
    print("Anúncio criado!")


def ver_anuncios(lista):
    if len(lista) == 0:
        print("Nenhum anúncio cadastrado.")
        return

    for i in range(len(lista)):
        item = lista[i]
        print(
            f"{i + 1} - {item['titulo']} | R$ {item['preco']} | "
            f"{item['categoria']} | {item['localizacao']} | {item['vendedor']}"
        )


def modificar_anuncio(lista):
    if len(lista) == 0:
        print("Nenhum anúncio para modificar.")
        return

    ver_anuncios(lista)
    escolha = input("Qual número do anúncio? ").strip()

    if not escolha.isdigit():
        print("Digite um número válido.")
        return

    idx = int(escolha) - 1
    if idx < 0 or idx >= len(lista):
        print("Anúncio não encontrado.")
        return

    item = lista[idx]
    novo_titulo = input(f"Novo título ({item['titulo']}): ").strip()
    novo_preco = input(f"Novo preço ({item['preco']}): ").strip()
    nova_localizacao = input(f"Nova localização ({item['localizacao']}): ").strip()

    if novo_titulo != "":
        item["titulo"] = novo_titulo
    if novo_preco != "":
        item["preco"] = novo_preco
    if nova_localizacao != "":
        item["localizacao"] = nova_localizacao

    print("Anúncio atualizado!")


def deletar_anuncio(lista):
    if len(lista) == 0:
        print("Nenhum anúncio para deletar.")
        return

    ver_anuncios(lista)
    escolha = input("Qual número do anúncio para deletar? ").strip()

    if not escolha.isdigit():
        print("Digite um número válido.")
        return

    idx = int(escolha) - 1
    if idx < 0 or idx >= len(lista):
        print("Anúncio não encontrado.")
        return

    confirmacao = input("Tem certeza que quer deletar? (s/n): ").strip()
    if confirmacao == "s":
        del lista[idx]
        print("Anúncio deletado!")
    else:
        print("Exclusão cancelada.")


def main():
    opcao = ""
    while opcao != "5":
        menu()
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            criar_anuncio(anuncios)
        elif opcao == "2":
            ver_anuncios(anuncios)
        elif opcao == "3":
            modificar_anuncio(anuncios)
        elif opcao == "4":
            deletar_anuncio(anuncios)
        elif opcao == "5":
            print("Saindo...")
        else:
            print("Opção inválida.")


main()
