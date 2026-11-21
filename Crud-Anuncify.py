anuncios = []

while True:
    print("\n=== ANUNCIFY ===")
    print("1 - Cadastrar | 2 - Listar | 3 - Buscar | 4 - Sair")
    op = input("Opção: ").strip()

    if op == "1":
        titulo = input("Título: ").strip()
        preco_txt = input("Preço: ").strip().replace(",", ".")
        if not titulo or not preco_txt:
            print("Título e preço são obrigatórios.")
            continue
        try:
            preco = float(preco_txt)
        except ValueError:
            print("Preço inválido.")
            continue
        if preco < 0:
            print("Preço não pode ser negativo.")
            continue
        categoria = input("Categoria: ").strip() or "Geral"
        anuncios.append({"titulo": titulo, "preco": preco, "categoria": categoria})
        print("Anúncio cadastrado!")

    elif op == "2":
        if not anuncios:
            print("Nenhum anúncio cadastrado.")
            continue
        for i, item in enumerate(anuncios):
            print(f"[{i}] {item['titulo']} | R$ {item['preco']:.2f} | {item['categoria']}")

    elif op == "3":
        if not anuncios:
            print("Nenhum anúncio para buscar.")
            continue
        termo = input("Buscar por título ou categoria: ").strip().lower()
        if not termo:
            print("Digite um termo para buscar.")
            continue
        encontrados = [
            item for item in anuncios
            if termo in str(item.get("titulo", "")).lower()
            or termo in str(item.get("categoria", "")).lower()
        ]
        if not encontrados:
            print("Nenhum anúncio encontrado.")
        else:
            for item in encontrados:
                print(f"- {item['titulo']} (R$ {item['preco']:.2f}) [{item['categoria']}]")

    elif op == "4":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")
