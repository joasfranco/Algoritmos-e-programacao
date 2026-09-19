# Algoritmos-e-programacao
CRUD de Anúncios - OLX

## IDEIA:

Programa inspirado em plataformas de compra e venda, como a OLX, com o objetivo de permitir que o usuário cadastre, visualize, modifique e delete anúncios de produtos.

## ESBOÇO:

### Onde os dados serão guardados?

Os dados dos anúncios serão armazenados em uma estrutura de dados, contendo as informações necessárias para identificar e gerenciar cada anúncio.

--> Estrutura dos anúncios:

- titulo --> Título do anúncio
- descricao --> Descrição do produto anunciado
- preco --> Preço do produto
- categoria --> Categoria do produto
- vendedor --> Nome do vendedor
- localizacao --> Localização do anúncio

--> Variáveis de identidade:

- anuncio --> Estrutura responsável por guardar as informações de cada anúncio
- tituloAnuncio --> Variável que identifica o título do anúncio
- precoAnuncio --> Variável que guarda o preço do produto
- categoriaAnuncio --> Variável que identifica a categoria do produto
- idAnuncio --> Identificador único de cada anúncio

--> Variáveis de fluxo do programa:

- opcao --> Variável que guarda o número da funcionalidade que o usuário deseja acessar
- resposta --> Variável utilizada para armazenar respostas do usuário
- busca --> Variável utilizada para armazenar o termo pesquisado pelo usuário

## Como o app tomará decisões de fluxo?

--> Escolher as funcionalidades do programa:

- Estrutura de repetição While, usada para apresentar o menu ao usuário e repetir as funcionalidades até que o usuário escolha a opção "5. Sair".

- Estrutura de decisão if/else, usada para acessar cada funcionalidade escolhida pelo usuário.

### --> Criar anúncio?

- Estrutura de decisão if/else, usada para receber as informações do produto e criar um novo anúncio.

- O programa solicita informações como título, descrição, preço, categoria e localização.

### --> Ver anúncios:

- Estrutura de repetição, usada para percorrer os anúncios cadastrados e apresentar suas informações ao usuário.

- Caso não existam anúncios cadastrados, o programa informa que não existem anúncios disponíveis.

### --> Modificar anúncio:

- Estrutura de decisão if/else, usada para verificar se o anúncio informado pelo usuário existe.

- Se o anúncio existir, o programa permite atualizar suas informações.

- Caso o anúncio não seja encontrado, o programa informa que o anúncio não existe.

### --> Deletar anúncio:

- Estrutura de decisão if/else, usada para verificar o anúncio que o usuário deseja remover.

- Caso o anúncio exista, ele será removido da estrutura de dados.

- Caso contrário, o programa informa que o anúncio não foi encontrado.

### --> Buscar anúncio:

- Estrutura de repetição usada para percorrer os anúncios cadastrados.

- O programa compara o termo informado pelo usuário com os títulos ou informações dos anúncios.

- Os anúncios encontrados são apresentados ao usuário.

## Bibliotecas:

- Não foram utilizadas bibliotecas externas. O projeto utiliza recursos próprios do Python para realizar as operações do CRUD.

## CRUD:

O projeto utiliza as quatro operações básicas de um CRUD:

- Create --> Criar novos anúncios
- Read --> Visualizar anúncios cadastrados
- Update --> Modificar informações de anúncios
- Delete --> Deletar anúncios

## Menu do programa:

1. Criar anúncio
2. Ver anúncios
3. Modificar anúncio
4. Deletar anúncio
5. Sair
