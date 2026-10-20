# CRUD de anúncios - OLX
# como não dá pra usar lista, cada anúncio tem as suas próprias variáveis
# e o programa guarda no máximo 3 anúncios
# anúncio 1
ocupado1 = False
titulo1 = ""
descricao1 = ""
preco1 = 0
categoria1 = ""
vendedor1 = ""
localizacao1 = ""
 
# anúncio 2
ocupado2 = False
titulo2 = ""
descricao2 = ""
preco2 = 0
categoria2 = ""
vendedor2 = ""
localizacao2 = ""
 
# anúncio 3
ocupado3 = False
titulo3 = ""
descricao3 = ""
preco3 = 0
categoria3 = ""
vendedor3 = ""
localizacao3 = ""
 
opcao = ""
 
while opcao != "5":
    print()
    print("--- OLX ---")
    print("1. Criar anúncio")
    print("2. Ver anúncios")
    print("3. Modificar anúncio")
    print("4. Deletar anúncio")
    print("5. Sair")
    opcao = input("Escolha: ")
    print()
 
    # CRIAR
    if opcao == "1":
        # usa o primeiro espaço que estiver livre
        if not ocupado1:
            print("Criando o anúncio 1")
            titulo1 = input("Título: ")
            descricao1 = input("Descrição: ")
            preco1 = float(input("Preço: "))
            categoria1 = input("Categoria: ")
            vendedor1 = input("Vendedor: ")
            localizacao1 = input("Localização: ")
            ocupado1 = True
            print("Anúncio criado!")
        elif not ocupado2:
            print("Criando o anúncio 2")
            titulo2 = input("Título: ")
            descricao2 = input("Descrição: ")
            preco2 = float(input("Preço: "))
            categoria2 = input("Categoria: ")
            vendedor2 = input("Vendedor: ")
            localizacao2 = input("Localização: ")
            ocupado2 = True
            print("Anúncio criado!")
        elif not ocupado3:
            print("Criando o anúncio 3")
            titulo3 = input("Título: ")
            descricao3 = input("Descrição: ")
            preco3 = float(input("Preço: "))
            categoria3 = input("Categoria: ")
            vendedor3 = input("Vendedor: ")
            localizacao3 = input("Localização: ")
            ocupado3 = True
            print("Anúncio criado!")
        else:
            print("Não tem mais espaço, delete um anúncio antes.")
 
    # VER (e buscar)
    elif opcao == "2":
        busca = input("Buscar pelo título (ENTER mostra todos): ")
        busca = busca.lower()
        achou = False
        print()
 
        if ocupado1 and busca in titulo1.lower():
            print("Anúncio 1")
            print("Título:", titulo1)
            print("Descrição:", descricao1)
            print("Preço: R$", preco1)
            print("Categoria:", categoria1)
            print("Vendedor:", vendedor1)
            print("Localização:", localizacao1)
            print()
            achou = True
 
        if ocupado2 and busca in titulo2.lower():
            print("Anúncio 2")
            print("Título:", titulo2)
            print("Descrição:", descricao2)
            print("Preço: R$", preco2)
            print("Categoria:", categoria2)
            print("Vendedor:", vendedor2)
            print("Localização:", localizacao2)
            print()
            achou = True
 
        if ocupado3 and busca in titulo3.lower():
            print("Anúncio 3")
            print("Título:", titulo3)
            print("Descrição:", descricao3)
            print("Preço: R$", preco3)
            print("Categoria:", categoria3)
            print("Vendedor:", vendedor3)
            print("Localização:", localizacao3)
            print()
            achou = True
 
        if not achou:
            print("Nenhum anúncio encontrado.")
 
    # MODIFICAR
    elif opcao == "3":
        resposta = input("Qual anúncio quer modificar (1, 2 ou 3)? ")
 
        if resposta == "1" and ocupado1:
            print("Digite os novos dados do anúncio 1")
            titulo1 = input("Título: ")
            descricao1 = input("Descrição: ")
            preco1 = float(input("Preço: "))
            categoria1 = input("Categoria: ")
            vendedor1 = input("Vendedor: ")
            localizacao1 = input("Localização: ")
            print("Anúncio modificado!")
        elif resposta == "2" and ocupado2:
            print("Digite os novos dados do anúncio 2")
            titulo2 = input("Título: ")
            descricao2 = input("Descrição: ")
            preco2 = float(input("Preço: "))
            categoria2 = input("Categoria: ")
            vendedor2 = input("Vendedor: ")
            localizacao2 = input("Localização: ")
            print("Anúncio modificado!")
        elif resposta == "3" and ocupado3:
            print("Digite os novos dados do anúncio 3")
            titulo3 = input("Título: ")
            descricao3 = input("Descrição: ")
            preco3 = float(input("Preço: "))
            categoria3 = input("Categoria: ")
            vendedor3 = input("Vendedor: ")
            localizacao3 = input("Localização: ")
            print("Anúncio modificado!")
        else:
            print("Esse anúncio não existe.")
 
    # DELETAR
    elif opcao == "4":
        resposta = input("Qual anúncio quer deletar (1, 2 ou 3)? ")
 
        if resposta == "1" and ocupado1:
            ocupado1 = False
            print("Anúncio 1 deletado!")
        elif resposta == "2" and ocupado2:
            ocupado2 = False
            print("Anúncio 2 deletado!")
        elif resposta == "3" and ocupado3:
            ocupado3 = False
            print("Anúncio 3 deletado!")
        else:
            print("Esse anúncio não existe.")
 
    elif opcao == "5":
        print("Até mais!")
 
    else:
        print("Opção inválida.")
