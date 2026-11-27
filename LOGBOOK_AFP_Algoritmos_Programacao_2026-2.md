# 📓 LOGBOOK AFP — Algoritmos e Programação (2026.2)

> **Como usar este arquivo:** copie-o para a raiz do **seu** repositório (ou para `logbook/LOGBOOK.md`) e preencha **direto no GitHub** (botão ✏️ *Edit this file*) ou no VS Code. Ele reúne todos os instrumentos do Protocolo AFP 2026.2 (Logbook Individual — Campos 01 a 04, 06 e 07; Registro de Revisão por Pares — Campo 05; Checkpoint Conceitual; Rubrica de Defesa Técnica).
>
> **Organização:** o Logbook está dividido em **3 grupos de entrega**, cada um com seu prazo. Dentro de cada grupo, os **ciclos de entrega (01 a 12)** continuam os mesmos, com as orientações de preenchimento. Siga a ordem: **Grupo 1 → Grupo 2 → Grupo 3 → Defesa Técnica**.
>
> O `Diario.md` do checklist passa a ser **este arquivo**: o registro de cada ciclo está na seção do ciclo correspondente.

## 📍 Navegação rápida

| Seção | Prazo |
|---|---|
| [👨‍🎓 Identificação](#-identificação) | Hoje |
| [🟢 Grupo 1](#-grupo-1--prazo-segunda-1611-às-23h59) · Registros 01–04, Campos 01 e 02 | **Segunda 16/11, 23h59** |
| [🟠 Grupo 2](#-grupo-2--prazo-sábado-2111-às-23h59) · Registros 05–08, Checkpoint, Campos 03 e 04 | **Sábado 21/11, 23h59** |
| [🔵 Grupo 3](#-grupo-3--prazo-quinta-2611-às-23h59) · Registros 09–12, Campos 05, 06 e 07 | **Quinta 26/11, 23h59** |
| [🏁 Defesa Técnica](#-defesa-técnica--quarta-1811) | **Quarta 18/11** |
| [🆘 Estou atrasado](#-estou-atrasado-no-logbook-e-agora) | — |

---

## 👨‍🎓 Identificação

| Campo | Preencha |
|---|---|
| **Nome do estudante** | Joás franco rodrigues |
| **Curso / Módulo** | Engenharia de software · 2º período |
| **Unidade curricular** | Algoritmos e Programação — UnDB 2026.2 |
| **Professor** | Rondineli Seba Salomão |
| **App-base do meu CRUD** | Sistema de classificados e anúncios de produtos — Anuncify |
| **Link do meu repositório** | https://github.com/joasfranco/Algoritmos-e-programacao |
| **Dupla de revisão (Campo 05)** | Caio rafael e Enzo figueiredo/ Davi gael |
| **Função neste ciclo** | Joás franco · Caio rafael, Davi gael e Enzo figueiredo |

---

## 🧭 Regras de ouro (leia antes de preencher)

1. **Processo, não resultado.** O Logbook mostra *como você pensou*, não só o que funcionou. Registre erros, desvios e dúvidas reais.
2. **Vocabulário técnico.** Use os termos da área (ex.: "laço de repetição", "validação de entrada", "estrutura de dados"). Respostas genéricas ("aprendi Python") não são aceitas.
3. **Todo registro relevante tem 3 âncoras:** o **objeto de conhecimento** mobilizado + a **justificativa técnica** + a **referência/fonte**. *Decisão sem objeto de conhecimento e sem referência é considerada não rastreável e não conta para a avaliação formativa.*
4. **Coerência entre campos.** O Campo 02 deve ser coerente com o Campo 01. *Incoerência é evidência de autoria externa.* O Campo 07 retoma o Campo 01.
5. **IA é permitida e avaliada (Campo 04).** *Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.* Você precisa mostrar o que aceitou **e** o que questionou/descartou, com argumento técnico.
6. **O histórico do Git é a sua evidência.** Faça commits pequenos e frequentes. Nunca reescreva o histórico (`force push`) do arquivo do Logbook.
7. **Campo 01 e Checkpoint são "sem consulta".** Preencha em um bloco contínuo, sem internet, sem material e sem colegas, no tempo indicado (Campo 01: durante o laboratório; Checkpoint: 20 min). Depois **não edite** esses campos — se perceber um erro, corrija em um campo posterior (Campo 03 ou 07), explicando.
8. **Os prazos dos grupos (16/11, 21/11 e 26/11, às 23h59)** valem para o commit no GitHub. O horário do commit é o registro oficial.

### ✅ Padrão de commit do Logbook

```text
docs(logbook): campo 01 — ciclo 02
docs(logbook): registro do ciclo 05
docs(logbook): campo 05 — revisão do CRUD de <colega>
```

---

## 🗓️ Calendário de entregas e Defesa

Os grupos têm **5 dias entre um prazo e outro**. O horário do commit no GitHub é o registro oficial.

| Grupo | Janela de preenchimento | **Prazo** | O que entregar |
|:--:|---|---|---|
| **1** | Qua 11/11 → seg 16/11 | **Segunda 16/11, 23h59** | Identificação · Registros dos Ciclos 01 a 04 · Campo 01 · Campo 02 |
| **2** | Seg 16/11 → sáb 21/11 | **Sábado 21/11, 23h59** | Registros dos Ciclos 05 a 08 · Checkpoint Conceitual · Campo 03 · Campo 04 |
| **3** | Sáb 21/11 → qui 26/11 | **Quinta 26/11, 23h59** | Registros dos Ciclos 09 a 12 · Campo 05 (2 revisões) · Campo 06 · Campo 07 |
| 🏁 | — | **Quarta 18/11** | **Defesa Técnica individual** (Rubrica) |

### Linha do tempo

| Data | Evento |
|---|---|
| Qua 11/11 | **Hoje:** começa o Grupo 1 |
| Seg 16/11 | ✅ Prazo do **Grupo 1** |
| **Qua 18/11** | 🏁 **Defesa Técnica** |
| Sáb 21/11 | ✅ Prazo do **Grupo 2** |
| Qua 25/11 | Avaliação P2 |
| Qui 26/11 | ✅ Prazo do **Grupo 3** |
| Qua 02/12 | Avaliação Substitutiva |
| Qua 09/12 | Avaliação Final |

> ⚠️ **Atenção:** a Defesa Técnica (18/11) acontece **antes** dos prazos dos Grupos 2 e 3. Na defesa você será arguido sobre **o que já estiver registrado e commitado**. Veja a seção [Defesa Técnica](#-defesa-técnica--quarta-1811) para saber o que priorizar até 18/11.

### Ciclos de entrega por grupo

| Ciclo | Data da aula | Tema do ciclo | Grupo | O que preencher |
|:--:|:--:|---|:--:|---|
| 01 | 12/08 | Preparação do laboratório e escolha do projeto | **1** | Registro do Ciclo |
| 02 | 19/08 | Variáveis, tipos de dados, entrada/saída | **1** | Registro + **Campo 01** + **Campo 02** |
| 03 | 26/08 | Operadores, fluxogramas, paradigmas | **1** (registro) · **2** (campos) | Registro (G1) · **Checkpoint**, **Campo 03**, **Campo 04** (G2) |
| 04 | 02/09 | Condicionais: `if`, `elif`, `else` | **1** | Registro do Ciclo |
| 05 | 09/09 | Condicionais aninhadas e operadores lógicos | **2** | Registro do Ciclo |
| 06 | 30/09 | Repetição: `for`, `while`, `break`, `continue` | **2** | Registro do Ciclo (inclui devolutiva da P1) |
| 07 | 07/10 | Listas: armazenamento e iteração | **2** | Registro do Ciclo |
| 08 | 14/10 | Busca e introdução a dicionários/matrizes | **2** | Registro do Ciclo |
| 09 | 21/10 | Atualização e exclusão: CRUD completo | **3** | Registro + **Campo 05** (revisão nº 1) |
| 10 | 28/10 | Modularização: funções | **3** | Registro do Ciclo |
| 11 | 04/11 | Recursividade | **3** | Registro + **Campo 06** |
| 12 | 11/11 | Refatoração e qualidade de código | **3** | Registro + **Campo 05** (revisão nº 2) + **Campo 07** |

---

## 📊 Painel de acompanhamento

Atualize a cada commit (troque ⬜ por ✅).

| Grupo | Item | Prazo | Preenchido | Commit |
|:--:|---|---|:--:|:--:|
| 1 | Identificação | 16/11 | ✅ | ✅ |
| 1 | Registros dos Ciclos 01, 02, 03 e 04 | 16/11 | ✅ | ✅ |
| 1 | Campo 01 — Instrumento de entrada | 16/11 | ✅ | ✅ |
| 1 | Campo 02 — Aprofundamento | 16/11 | ✅ | ✅ |
| 2 | Registros dos Ciclos 05, 06, 07 e 08 | 21/11 | ✅ | ✅ |
| 2 | Checkpoint Conceitual | 21/11 | ⬜ | ⬜ |
| 2 | Campo 03 — Execução e desvios | 21/11 | ✅ | ✅ |
| 2 | Campo 04 — Interação com IA | 21/11 | ✅ | ✅ |
| 3 | Registros dos Ciclos 09, 10, 11 e 12 | 26/11 | ⬜ | ⬜ |
| 3 | Campo 05 — Revisão por pares nº 1 e nº 2 | 26/11 | ⬜ | ⬜ |
| 3 | Campo 06 — Próximos passos | 26/11 | ⬜ | ⬜ |
| 3 | Campo 07 — Evolução conceitual | 26/11 | ⬜ | ⬜ |
| 🏁 | Defesa Técnica | 18/11 | ⬜ | — |

---

## ❓ A questão-problema da AFP

**Título:** *O sistema em produção: diagnosticando as falhas do CRUD que você mesmo construiu.*

> **Enunciado completo (Apêndice A):** _professor(a): cole aqui o enunciado e os anexos liberados conforme o cronograma._

A questão-problema é **a mesma durante todo o semestre**: ela se aplica ao **seu** CRUD, que cresce a cada ciclo. Os **dados com defeito** do seu app chegam em um **lote cumulativo único** e vão expondo problemas diferentes conforme sua estrutura evolui. Seu trabalho é diagnosticar, ajustar o CRUD para tratar cada falha e **registrar o raciocínio** neste Logbook.

---

# 🔁 REGISTRO DO CICLO — modelo (copie em cada ciclo)

Cada ciclo tem sua própria seção abaixo, já com o modelo. Se precisar de espaço extra, acrescente linhas.

```markdown
### Registro do Ciclo NN — DD/MM
1. **Desafio do ciclo (em 1 frase):**
2. **O que implementei (commits / arquivos / links):**
3. **Objeto(s) de conhecimento mobilizado(s) (vocabulário técnico):**
4. **Desvio ou erro encontrado + causa técnica:**
5. **Decisão de ajuste + fonte (livro, doc, vídeo, colega, IA):**
6. **Feedback recebido (professor/colega) e o que mudei por causa dele:**
7. **Próximo passo:**
```

**Como preencher bem:** escreva como se explicasse a um colega que não esteve na aula. O item 3 e o item 5 são os mais importantes: eles ligam o que você fez ao **conteúdo** e à **fonte**.

| ❌ Fraco | ✅ Forte |
|---|---|
| "Aprendi a usar `if`." | "Usei estrutura condicional aninhada para validar a idade antes de cadastrar. Meu erro foi comparar `str` com `int` (resultado de `input()`); corrigi com `int()` (Pense em Python, cap. 2)." |
| "Deu erro e consertei." | "O programa quebrou com `ZeroDivisionError` ao calcular a média de um item sem avaliações. Causa: divisão por `len(lista)` com lista vazia. Ajuste: testar `if len(lista) > 0`." |

---

# 🟢 GRUPO 1 — prazo segunda 16/11 às 23h59

> **Janela:** quarta 11/11 → segunda 16/11. **O que entregar:** Identificação · Registros dos Ciclos 01, 02, 03 e 04 · Campo 01 · Campo 02.
>
> **Sugestão de ordem:** (1) Identificação → (2) **Campo 01 primeiro, sem consulta** → (3) Registros dos Ciclos 01 a 04 → (4) Campo 02, com pesquisa.

**Checklist do Grupo 1**
- [✅] Identificação preenchida (app-base, link do repositório, dupla de revisão)
- [ ] Campo 01: 3 objetos de conhecimento, 3 lacunas, hipótese de até 5 linhas
- [ ] Registros dos Ciclos 01, 02, 03 e 04 com os 7 itens
- [ ] Campo 02: 2 referências com contribuição, hipótese revisada, 3 recursos
- [ ] Commits no GitHub e painel atualizado

## 🟢 CICLO 01 — 12/08 — Preparação do laboratório e escolha do projeto

<details>
<summary>📘 Orientações do Ciclo 01</summary>

- **Hoje não há Campo do Protocolo.** O foco é preparar o ambiente: criar o repositório, configurar o VS Code e escolher o **app-base** do seu CRUD (e, portanto, o *schema* dos seus dados).
- Preencha a **Identificação** (no início deste arquivo) e o **Registro do Ciclo 01**.
- No item 3, registre **o que você já sabia** e o que era novo (Git, GitHub, VS Code). Isso será útil para o Campo 07.
- No item 4, registre qualquer problema de instalação ou configuração e como o resolveu — isso conta como desvio.
- Faça o primeiro commit: `docs(logbook): registro do ciclo 01`.
</details>

#### Registro do Ciclo 01 — 12/08
1. **Desafio do ciclo (em 1 frase):** Configuração do ambiente de desenvolvimento utilizando VS Code, Git e GitHub para a construção de um CRUD inspirado na plataforma OLX
2. **O que implementei (commits / arquivos / links):** Foi realizado a definição do projeto de um CRUD em Python inspirado em uma plataforma de classificados, utilizando a OLX como referência. Também foi planejada a estrutura inicial do repositório e a configuração do ambiente de desenvolvimento no VS Code
3. **Objeto(s) de conhecimento mobilizado(s):** Possuía conhecimentos básicos de Python, com pouca familiaridade com lógica de programação e suas estruturas. Em relação ao Git e GitHub, sabia apenas criar repositórios, mas ainda não dominava outras funcionalidades de controle de versão, como commits e gerenciamento do histórico de alterações.
4. **Desvio ou erro encontrado + causa técnica:** Não foram encontradas dificuldades durante a configuração do ambiente de desenvolvimento. A instalação e a preparação das ferramentas ocorreram normalmente, sem apresentar problemas técnicos.
5. **Decisão de ajuste + fonte:** Decidi organizar o Anuncify em uma pasta específica dentro do repositório Algoritmos-e-programacao, separando os arquivos do projeto das demais atividades. O CRUD será desenvolvido em Python, inspirado na OLX, utilizando Git e GitHub para controlar versões e acompanhar as alterações do código.
6. **Feedback recebido e o que mudei:** Até o momento, não foram recebidos feedbacks externos sobre o projeto. A proposta inicial foi mantida, considerando os requisitos definidos para o sistema de classificados.
7. **Próximo passo:** Começar a aplicar os conhecimentos adquiridos em Python, aprofundando a lógica de programação e desenvolvendo gradualmente as funcionalidades do CRUD inspirado na OLX.

## 🟢 CICLO 02 — 19/08 — Variáveis, tipos de dados e entrada/saída

<details>
<summary>📘 Orientações do Ciclo 02 — Campo 01 (sem consulta) e Campo 02 (pesquisa)</summary>

**Campo 01 — Instrumento de entrada** · *sem consulta · faça primeiro*
- Preencha **antes de tudo**, em um bloco contínuo de cerca de 15 minutos, sem internet, sem material, sem IA e sem colegas, depois de conhecer a questão-problema e a primeira amostra de dados do seu app. Depois do Campo 01 você pode consultar o que quiser.
- **1a.** Liste pelo menos **3 objetos de conhecimento** que você acha que precisa dominar para resolver o problema. Use o vocabulário técnico da área. *Não precisa acertar tudo — o Campo 07 vai mostrar o quanto você evoluiu.*
- **1b.** Liste pelo menos **3 lacunas**: o que você **não sabe** e precisa descobrir, com precisão (ruim: "não sei programar"; bom: "não sei como validar a entrada para impedir que o usuário digite texto onde espero número").
- **1c.** Escreva sua **hipótese inicial** em até 5 linhas: o que você acha que está causando as falhas do CRUD e por quê.
- Faça o commit **logo ao terminar**. Depois, **não edite** o Campo 01.

**Campo 02 — Aprofundamento** · *AV Qualis · segunda 16/11, 23h59*
- Preencha **depois do Campo 01, com pesquisa real**, e seja coerente com ele.
- **2a.** Pelo menos **2 referências** (livro, documentação, vídeo, artigo), cada uma com a **contribuição** concreta para a sua solução. Não basta listar o título.
- **2b.** **Hipótese revisada:** o que mudou em relação ao Campo 01 e **por quê**. Se não mudou nada, explique por que a pesquisa confirmou a hipótese.
- **2c.** **Dimensionamento inicial de recursos** (mínimo 3 itens), com quantidade estimada e justificativa técnica. Exemplos de recursos no seu contexto: horas de estudo, número de casos de teste, módulos/arquivos do projeto, dados de teste, bibliotecas.
</details>

### 🧩 CAMPO 01 — Instrumento de entrada
*Grupo 1 | Prazo segunda 16/11, 23h59 | SEM CONSULTA*

**1a. Objetos de conhecimento identificados (mínimo 3, com vocabulário técnico):**
1. Conhecimento prévio sobre variáveis e sua utilização para armazenar informações durante a execução de um programa.
2. Conhecimento básico sobre tipos de dados, compreendendo a utilização de números inteiros, números decimais e textos.
3. Conhecimento sobre comandos de entrada e saída, como input() e print(), para receber informações do usuário e exibir resultados.


**1b. Lacunas — o que não sei e preciso descobrir (mínimo 3, com precisão técnica):**
1. Aprofundar o conhecimento sobre o tipo de dado char e compreender sua utilização em variáveis.
2. Compreender melhor a conversão de tipos de dados (type casting) e sua importância ao receber informações do usuário.
3. Aprender a utilizar e manipular corretamente os dados recebidos por meio de comandos de entrada, evitando incompatibilidades entre os tipos de dados.

**1c. Hipótese inicial em até 5 linhas — com lógica da área de formação:**

> Minha hipótese inicial era que conseguiria utilizar os conhecimentos básicos sobre variáveis, tipos de dados e entrada/saída para desenvolver as primeiras funcionalidades do meu CRUD em Python. Esperava encontrar dificuldades na utilização de diferentes tipos de dados e na conversão das informações recebidas pelo usuário, principalmente durante o cadastro e armazenamento dos anúncios.

### 🧩 CAMPO 02 — Aprofundamento pós-aula
*AV Qualis — Grupo 1 | Segunda 16/11, 23h59*

> **Preenchido depois do Campo 01, com pesquisa real. Deve ser coerente com o Campo 01. Incoerência = evidência de autoria externa.**

**2a. Aprofundamento dos objetos de conhecimento (mínimo 2 referências com síntese da contribuição para a solução):**

- **Referência 1:** Curso Python #06 – Tipos Primitivos e Saída de Dados, de Gustavo Guanabara (Curso em Vídeo). — **Contribuição:** A aula aprofundou o conhecimento sobre os tipos primitivos do Python, apresentando o tipo bool e explicando melhor a utilização de int(), float() e str(). Também demonstrou como utilizar input() para receber informações do usuário e print() para exibir dados na tela, além da importância da conversão de tipos para trabalhar corretamente com os valores recebidos.
- **Referência 2:**Exercício Python #004 – Dissecando uma Variável, de Gustavo Guanabara (Curso em Vídeo). — **Contribuição:** O exercício demonstrou como analisar uma variável a partir de uma informação digitada pelo usuário, identificando seu tipo primitivo e verificando características do valor recebido. Isso contribuiu para compreender melhor como os dados são armazenados e como suas propriedades podem ser identificadas utilizando recursos do Python.

  Durante o processo de aprendizagem, utilizei o ChatGPT como assistente de aprendizagem para esclarecer dúvidas, reforçar os conteúdos estudados e compreender melhor os conceitos de variáveis, tipos de dados e comandos de entrada e saída em Python.

**2b. Hipótese revisada — o que mudou em relação ao Campo 01 e por quê:** 

> Após o aprofundamento, compreendi melhor a utilização dos tipos primitivos e a importância da conversão de dados em Python. Também percebi que o comando input() recebe informações inicialmente como texto, sendo necessário converter os valores quando se deseja trabalhar com números. Com isso, passei a entender melhor como esses conceitos podem ser aplicados futuramente no cadastro de anúncios do meu CRUD.

**2c. Dimensionamento inicial de recursos (recurso, quantidade estimada, justificativa técnica — mínimo 3 itens):**

| RECURSO / MATERIAL / INSUMO | QUANTIDADE ESTIMADA | JUSTIFICATIVA TÉCNICA |
|---|---|---|
|Aulas de Python | 2 aulas | Revisar os conteúdos de variáveis, tipos de dados e entrada e saída de informações. |
| Estudos e exercícios práticos | 3 dias | Reforçar os conhecimentos adquiridos e praticar os conceitos apresentados nas aulas. |
| Testes de funcionalidades | 2 operações CRUD | Verificar o funcionamento de cadastro, consulta, atualização e exclusão de anúncios. |
| Arquivos do projeto | 1 arquivo Python inicial | Organizar o código e concentrar as primeiras funcionalidades do Anuncify. |
| Repositório GitHub | 1 repositório | Armazenar o projeto e acompanhar sua evolução por meio do histórico de commits. |

#### Registro do Ciclo 02 — 19/08
1. **Desafio do ciclo (em 1 frase):** Aprofundar os conhecimentos sobre variáveis, tipos de dados e comandos de entrada e saída em Python.
2. **O que implementei (commits / arquivos / links):** Realizei estudos e exercícios práticos utilizando o arquivo aula1908PA.py, no qual pratiquei a declaração, inicialização e atribuição de valores a variáveis, além da identificação e utilização de diferentes tipos de dados em Python, como int, float e str.
3. **Objeto(s) de conhecimento mobilizado(s):** Variáveis, atribuição de valores, tipos primitivos (int, float, str e bool), conversão de tipos de dados (type casting) e comandos de entrada e saída (input() e print()).
4. **Desvio ou erro encontrado + causa técnica:** Durante os estudos, percebi a necessidade de aprofundar a compreensão sobre a conversão de tipos de dados, principalmente ao receber informações do usuário por meio do comando input().
5. **Decisão de ajuste + fonte:** Decidi aprofundar os estudos utilizando as aulas do Curso em Vídeo, de Gustavo Guanabara, e o ChatGPT como assistente de aprendizagem, para esclarecer dúvidas e compreender melhor os conceitos apresentados.
6. **Feedback recebido e o que mudei:** Utilizei as explicações e orientações recebidas durante os estudos para reforçar os conceitos que ainda apresentavam dúvidas, principalmente sobre os tipos de dados e a utilização de variáveis.
7. **Próximo passo:** Continuar aprofundando os conhecimentos em Python e começar a aplicar os conceitos estudados no desenvolvimento do CRUD Anuncify, utilizando variáveis e entradas de dados para estruturar o cadastro de anúncios.

## 🟢 CICLO 03 — 26/08 — Operadores, fluxogramas e paradigmas

<details>
<summary>📘 Orientações do Ciclo 03 — Registro (Grupo 1)</summary>

- Neste grupo você preenche **apenas o Registro do Ciclo 03**. O **Checkpoint Conceitual** e os **Campos 03 e 04** deste ciclo estão no **Grupo 2**.
- Item 3: nomeie os **operadores** (aritméticos, relacionais, lógicos) e os **tipos** que usou. Se montou fluxogramas, cite o que o fluxograma ajudou a perceber.
- Item 4: registre erros de precedência de operadores, divisão por zero ou confusão entre `=` e `==`, com a causa técnica.
</details>

#### Registro do Ciclo 03 — 26/08
1. **Desafio do ciclo (em 1 frase):** Compreender e aplicar os operadores da linguagem Python, desenvolver o raciocínio lógico por meio de fluxogramas e conhecer os diferentes paradigmas de programação.
2. **O que implementei (commits / arquivos / links):** Realizei estudos e exercícios práticos envolvendo operadores, expressões e representação de algoritmos por meio de fluxogramas, buscando compreender sua aplicação na construção de soluções computacionais.
3. **Objeto(s) de conhecimento mobilizado(s):** Foram trabalhados operadores aritméticos (+, -, *, /), relacionais (==, !=, >, <, >=, <=) e lógicos (and, or, not), utilizando tipos de dados como int, float e bool. Também foram abordados os fluxogramas, que permitem representar visualmente o fluxo de execução de um algoritmo, e os paradigmas de programação, que apresentam diferentes formas de estruturar e desenvolver soluções computacionais.
4. **Desvio ou erro encontrado + causa técnica:** A principal dificuldade encontrada foi diferenciar os operadores relacionais >= (maior ou igual a) e <= (menor ou igual a). Essa dificuldade ocorreu devido à semelhança visual entre os símbolos e à necessidade de compreender corretamente a direção da comparação lógica realizada por cada operador.
5. **Decisão de ajuste + fonte:** Decidi reforçar o estudo dos operadores relacionais por meio de exemplos práticos e exercícios em Python, buscando compreender melhor suas diferenças e aplicações em expressões condicionais. Utilizei o ChatGPT como ferramenta de apoio para esclarecer dúvidas e consolidar o entendimento desses conceitos.
6. **Feedback recebido e o que mudei:** A partir das explicações e orientações utilizadas durante os estudos, consegui identificar a diferença entre os operadores >= e <=, melhorando a compreensão sobre comparações relacionais e sua aplicação na lógica de programação.
7. **Próximo passo:** Continuar praticando os conceitos de lógica de programação e operadores em Python, buscando aplicar os conhecimentos adquiridos na estruturação das funcionalidades do CRUD Anuncify.

## 🟢 CICLO 04 — 02/09 — Estruturas condicionais: `if`, `elif`, `else`

<details>
<summary>📘 Orientações do Ciclo 04</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 04.
- Conecte **cada condicional** do seu CRUD a uma **regra de negócio** (ex.: "preço não pode ser negativo").
- Se já recebeu o lote de dados com defeito, procure **qual registro quebra qual condição** e registre o item 4 com a **causa técnica** (ex.: valor `None`, texto vazio, número negativo, divisão por zero).
- No item 5, cite a fonte da decisão: livro (*Pense em Python*), documentação ou exercício que você resolveu.
- Compare com o **Campo 02**: o desvio de hoje já estava previsto no seu dimensionamento?
</details>

#### Registro do Ciclo 04 — 02/09
1. **Desafio do ciclo (em 1 frase):** Compreender e aplicar estruturas condicionais em Python para controlar o fluxo de execução do programa e estabelecer regras de negócio para o CRUD Anuncify.
2. **O que implementei (commits / arquivos / links):** Realizei exercícios práticos de programação utilizando o arquivo aula2608PA, no qual pratiquei a aplicação das estruturas condicionais if, elif e else em Python, desenvolvendo a compreensão sobre o controle de fluxo e a tomada de decisões dentro de um programa.
3. **Objeto(s) de conhecimento mobilizado(s):** Foram estudadas as estruturas condicionais if, elif e else, responsáveis pelo controle de fluxo de execução de um programa. Também foram trabalhadas expressões booleanas, operadores relacionais e operadores lógicos, utilizados na avaliação de condições. No contexto do Anuncify, esses conhecimentos podem ser aplicados em regras de negócio, como impedir o cadastro de anúncios com preços negativos e verificar se os campos obrigatórios foram preenchidos.
4. **Desvio ou erro encontrado + causa técnica:** Durante os exercícios, foi identificada uma dificuldade na organização das estruturas condicionais if, elif e else. A causa técnica estava relacionada à indentação incorreta dos blocos de código, fazendo com que determinadas instruções não fossem associadas à condição esperada.
5. **Decisão de ajuste + fonte:** Decidi reforçar o estudo das estruturas condicionais por meio de exercícios práticos em Python e utilizar o ChatGPT como ferramenta de apoio para esclarecer dúvidas sobre a aplicação de if, elif e else em situações reais de programação.
6. **Feedback recebido e o que mudei:** As explicações e orientações utilizadas durante os estudos contribuíram para melhorar minha compreensão sobre o funcionamento das estruturas condicionais e sua aplicação na verificação de informações, como validar preços e campos obrigatórios no cadastro de anúncios.
7. **Próximo passo:** Aprofundar a utilização das estruturas condicionais e começar a aplicá-las no Anuncify, desenvolvendo validações para os dados dos anúncios, como preço, título e descrição

---

# 🟠 GRUPO 2 — prazo sábado 21/11 às 23h59

> **Janela:** segunda 16/11 → sábado 21/11. **O que entregar:** Registros dos Ciclos 05, 06, 07 e 08 · Checkpoint Conceitual · Campo 03 · Campo 04.
>
> ⚠️ O prazo cai num **sábado**: planeje terminar na sexta. Os campos do Ciclo 03 (Checkpoint, 03 e 04) aparecem **primeiro**, porque são a base da investigação.

**Checklist do Grupo 2**
- [ ] Checkpoint Conceitual feito conforme orientação do professor (20 min, sem consulta)
- [ ] Campo 03: 2 achados com objeto, 1 desvio com causa técnica, 1 decisão com fonte
- [ ] Campo 04: ferramenta, pergunta íntegra, resumo, o que aceitei e o que questionei
- [ ] Registros dos Ciclos 05, 06, 07 e 08 com os 7 itens (devolutiva da P1 no ciclo 06)
- [ ] Commits no GitHub e painel atualizado

## 🟠 CICLO 03 (campos) — 26/08 — Checkpoint, Campo 03 e Campo 04

<details>
<summary>📘 Orientações — Checkpoint, Campo 03 e Campo 04 (referentes ao Ciclo 03)</summary>

**Checkpoint Conceitual** · *20 min · sem consulta · conforme orientação do professor*
- Verifica o **seu domínio individual** do conteúdo — não avalia a sua solução. São **3 questões dissertativas**. Quem investiu por conta própria responde com segurança.
- Respostas **genéricas, sem ancoragem técnica, não são aceitas**. Defina o objeto **e** relacione-o ao problema do seu CRUD, explicitando as implicações.
- Critérios: *precisão conceitual*, *relação conteúdo-problema*, *qualidade do raciocínio*.
- Se for insatisfatório, você recebe **feedback escrito em até 48h** e deve ajustar a investigação antes da avaliação somativa.
- Se o professor aplicar o Checkpoint via GitHub, use o arquivo abaixo **só durante os 20 minutos**, com um único commit ao final.

**Campo 03 — Execução e desvios** · *sábado 21/11, 23h59*
- **3a.** Pelo menos **2 achados** que mudaram sua compreensão do problema, cada um com o **objeto de conhecimento** associado.
- **3b.** Pelo menos **1 desvio** em relação ao Campo 02 (o que você planejou e não aconteceu) e a **causa técnica** — não vale "falta de tempo".
- **3c.** Pelo menos **1 decisão de ajuste**, com justificativa e **fonte**, e o objeto de conhecimento mobilizado.

**Campo 04 — Interação com IA** · *sábado 21/11, 23h59 · obrigatório e avaliado*
- Registre **pelo menos uma** interação real com uma IA sobre o seu CRUD.
- **4b.** Transcreva a pergunta **na íntegra** (copie e cole).
- **4c.** Resuma a resposta em **um parágrafo** com as suas palavras.
- **4d.** O que você **aceitou**, ligando ao objeto de conhecimento.
- **4e.** O que você **questionou ou descartou**, com **argumento técnico ou fonte** (teste, documentação, livro). Dica: **rode o código** que a IA sugeriu antes de decidir.
- **Print sem análise crítica = devolução imediata.** Se você aceitou tudo, volte e procure o que verificar.
</details>

### 🧩 CHECKPOINT CONCEITUAL INDIVIDUAL
*20 minutos · sem consulta a qualquer fonte, material ou colega · conforme orientação do professor.*

| | |
|---|---|
| **Nome do estudante** | _…_ |
| **Data de realização** | _…_ |
| **Unidade curricular** | Algoritmos e Programação |
| **Professor(a)** | Rondineli Seba Salomão |

> **INSTRUÇÕES:** Responda individualmente, sem consulta. Você tem 20 minutos. As questões avaliam seu domínio dos objetos de conhecimento do componente — não sua solução para o problema. Respostas genéricas sem ancoragem técnica não são aceitas.

**QUESTÃO 1** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

**QUESTÃO 2** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

**QUESTÃO 3** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

<details>
<summary>🔒 Uso do professor — critérios de avaliação do Checkpoint</summary>

| CRITÉRIO | SATISFATÓRIO | INSATISFATÓRIO |
|---|---|---|
| **Precisão conceitual** | Domínio do objeto de conhecimento, com vocabulário técnico adequado e sem erros conceituais relevantes. | Resposta vaga, com erros conceituais ou sem ancoragem nos objetos de conhecimento do componente. |
| **Relação conteúdo-problema** | Conecta o objeto de conhecimento ao problema trabalhado na AFP. | Responde o objeto de forma isolada, sem relação com o problema do ciclo. |
| **Qualidade do raciocínio** | Raciocínio técnico articulado: relaciona o objeto ao problema e explicita implicações para a investigação. | Apenas define o objeto, sem articular raciocínio ou relação com o problema investigado. |

**RESULTADO:** ☐ Satisfatório ☐ Insatisfatório
**AÇÃO DO PROFESSOR:** Checkpoint insatisfatório gera feedback escrito individualizado até 48h — o aluno ajusta a investigação antes da avaliação somativa.
</details>

### 🧩 CAMPO 03 — Execução e desvios
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59*

**3a. O que descobri que mudou minha compreensão do problema (mínimo 2 achados, com objeto de conhecimento associado):**
1. Percebi que usar uma variável de controle (num) para indicar qual slot ("1", "2" ou "3") será criado, modificado ou excluído — e zerá-la (num = "") quando ocorre erro de validação ou cancelamento — permite centralizar a gravação/atualização no final do laço sem repetir o bloco de escrita em vários ifs. — Objeto de conhecimento: Variáveis de controle, estruturas condicionais (if/elif/else) e fluxo de execução em laço while
2. Compreendi que, sem listas ou dicionários, cada anúncio fica em uma variável individual (anuncio1, anuncio2, anuncio3) concatenando os campos com " | ", o que exige checar explicitamente cada slot com == "" ou != "" e validar campos obrigatórios (titulo == "" ou preco == "") antes de sobrescrever qualquer anúncio existente. — Objeto de conhecimento: Variáveis, operadores relacionais (==, !=) e operadores lógicos (and, or) na validação de estado.
3. Notei que, na opção de listar (opcao == "2"), concatenar anuncio1 + anuncio2 + anuncio3 == "" verifica de forma simples se todos os três espaços estão vazios, mas ainda exige ifs separados para exibir apenas os anúncios não vazios mantendo o número original do slot. — Objeto de conhecimento: Expressões booleanas, concatenação de strings e estruturas condicionais.

**3b. Desvio em relação ao Campo 02 (ao menos 1 — causa técnica):**
- **Desvio:** No Campo 02, eu havia planejado testar separadamente cada operação do CRUD (criar, ver, modificar e deletar) e verificar casos de erro isolados; durante a execução do código no while, acabei testando a validação de campos obrigatórios (titulo == "" ou preco == "") e o cancelamento da exclusão (!= "s") dentro do mesmo fluxo encadeado, sem rodar um teste isolado para o caso em que os três slots (anuncio1, anuncio2, anuncio3) já estão ocupados e o usuário tenta criar um quarto anúncio.
- **Causa técnica:**O desvio ocorreu porque, com apenas três variáveis fixas para os anúncios, o estado dos slots dependia da sequência anterior de criações e exclusões no mesmo laço while; como os testes foram feitos em sequência sem preencher os três espaços antes de testar a criação, o caminho do else ("Não tem mais espaço, delete um anúncio antes.") ficou sem verificação isolada.

**3c. Decisão de ajuste (ao menos 1) com justificativa e fonte:**
- **Decisão:** Adotei a validação prévia da existência do anúncio nas opções "3" e "4" usando a expressão booleana existe = (num == "1" and anuncio1 != "") or (num == "2" and anuncio2 != "") or (num == "3" and anuncio3 != ""), limpando num = "" quando existe == False, e passei a exigir confirmação explícita (!= "s") antes de apagar o anúncio.
- **Fonte:** Curso Python #06 – Tipos Primitivos e Saída de Dados e Exercício Python #004 – Dissecando uma Variável, de Gustavo Guanabara (Curso em Vídeo), com apoio do ChatGPT como assistente de aprendizagem para reforçar os conceitos de variáveis, tipos primitivos e entrada/saída em Python.

**Objeto de conhecimento mobilizado nesta decisão:** Estruturas condicionais (if/elif/else), operadores lógicos (and, or), variáveis de controle e laço de repetição while.

### 🧩 CAMPO 04 — Interação com IA
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59 | OBRIGATÓRIO*

> **Obrigatório e avaliado. Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.**

**4a. Ferramenta:** Verdent (modelo GPT, OpenAI)  **Data:** 13/09/2026

**4b. Pergunta formulada (transcrita integralmente):**

> 4b. Pergunta formulada (transcrita integralmente):
Como posso organizar o controle de criação, alteração e exclusão de anúncios em variáveis separadas (anuncio1, anuncio2, anuncio3) usando if/elif/else e while sem que uma entrada inválida ou exclusão cancelada grave ou apague dados por engano?

**4c. Resposta da IA (resumida em parágrafo):**

> A IA sugeriu usar uma variável de controle para identificar qual anúncio será manipulado e limpá-la quando ocorrer validação inválida ou cancelamento, deixando a gravação final condicional ao fato de essa variável continuar válida; também comentou sobre checar campos vazios e confirmar antes de apagar, além de apontar limitações de escalabilidade ao manter variáveis individuais em vez de uma estrutura composta.

**4d. O que aceitei — com referência ao objeto de conhecimento do componente:**

> Aceitei a lógica de usar uma variável de controle (num) que só permanece preenchida quando as condições são atendidas e volta a "" quando há falha de validação (titulo == "" ou preco == ""), inexistência do anúncio ou cancelamento da exclusão (!= "s"), evitando alterações indevidas no bloco final. Isso se apoia nos objetos de conhecimento de variáveis, tipos primitivos (str, bool), operadores relacionais/lógicos (==, !=, and, or), estruturas condicionais (if/elif/else) e laços de repetição (while), reforçados nas aulas Curso Python #06 – Tipos Primitivos e Saída de Dados e Exercício Python #004 – Dissecando uma Variável (Gustavo Guanabara — Curso em Vídeo).

**4e. O que questionei ou descartei — com argumento técnico ou fonte:**

> Questionei e descartei sugestões de alterar a estrutura de dados do programa para coleções/estruturas mais avançadas neste momento, pois o recorte do projeto na disciplina trabalhava com variáveis simples, if/elif/else e while, e a prioridade era dominar o fluxo condicional, a verificação de estado de cada variável (anuncio1, anuncio2, anuncio3) e o tipo/conteúdo das entradas obtidas com input() antes de avançar para outras estruturas. Argumento técnico e fonte: manter o escopo restrito aos objetos de conhecimento estudados evita introduzir recursos não trabalhados no código e permite validar com precisão o comportamento das expressões booleanas e do controle de fluxo no laço while, com base nas aulas de Gustavo Guanabara (Curso Python #06 e Exercício Python #004) e na prática de testar cada caminho condicional no código.

## 🟠 CICLO 05 — 09/09 — Condicionais aninhadas e operadores lógicos

<details>
<summary>📘 Orientações do Ciclo 05</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 05.
- Registre **qual combinação de condições** (`and`, `or`, `not`) você precisou e **por que** uma condicional aninhada ou um operador lógico foi a melhor escolha.
- Descreva **pelo menos um caso de teste** que você usou para provar a lógica (entrada → resultado esperado → resultado obtido).
- **Atenção à P1 (23/09):** reveja o Logbook até aqui. Complete itens em branco e confirme se os commits estão em dia.
- Na semana de 16/09 (Nivelamento / Peer Instruction), reserve 10 minutos para atualizar este arquivo.
</details>

#### Registro do Ciclo 05 — 09/09
1. **Desafio do ciclo (em 1 frase):** Garantir que as validações e buscas de anúncios no Anuncify combinem múltiplas condições com clareza sem alterar ou apagar registros indevidamente.
2. **O que implementei (commits / arquivos / links):** Ajustes na verificação de existência de anúncio e na validação de campos obrigatórios no código do CRUD (anuncio1, anuncio2, anuncio3 com if/elif/else e while). 
3. **Objeto(s) de conhecimento mobilizado(s):** Condicionais aninhadas (if/elif/else), operadores lógicos (and, or, not), expressões booleanas e laço de repetição while.
4. **Desvio ou erro encontrado + causa técnica:** Ao verificar se um anúncio existia antes de modificar ou deletar (opcao == "3" ou "4"), combinar o número escolhido com o estado do respectivo slot (!= "") exigiu atenção à precedência e ao agrupamento com parênteses em (num == "1" and anuncio1 != "") or (num == "2" and anuncio2 != "") or (num == "3" and anuncio3 != ""); sem agrupar corretamente cada par, a condição avaliaria combinações falsas entre número do anúncio e conteúdo das variáveis.
5. **Decisão de ajuste + fonte:** Utilizei or entre as três verificações compostas por and para testar cada slot de forma independente e limpar num = "" quando existe == False, além de exigir confirmação != "s" antes de deletar — com base nas aulas Curso Python #06 – Tipos Primitivos e Saída de Dados e Exercício Python #004 – Dissecando uma Variável (Gustavo Guanabara — Curso em Vídeo) e no apoio do ChatGPT.
6. **Feedback recebido e o que mudei:** Reforcei os testes de casos de borda (entrada num = "2" quando anuncio2 == "", título/preço vazios e resposta diferente de "s" na exclusão) para confirmar que num é zerado e o bloco final não grava dados indevidos.
7. **Próximo passo:** Continuar praticando o uso de condições aninhadas (if/elif/else dentro de outras estruturas condicionais) e operadores lógicos (and, or, not) nas operações do CRUD (anuncio1, anuncio2, anuncio3), testando os caminhos internos de validação e cancelamento para garantir que cada decisão aninhada leve ao estado esperado dentro do laço while.

## 🟠 CICLO 06 — 30/09 — Devolutiva da P1 + repetição: `for`, `while`, `break`, `continue`

<details>
<summary>📘 Orientações do Ciclo 06</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 06.
- Use o item 6 para registrar a **devolutiva da P1**: o que errou e **qual conceito** estava faltando. Esses erros alimentam o **Campo 07c** (conceitos corrigidos). *Anote já, para não esquecer.*
- Registre **por que escolheu `for` ou `while`** em cada laço do seu CRUD (cadastro em lote, listagem, menu).
- Item 4: se um laço ficou infinito ou pulou itens, descreva a **causa técnica** (condição de parada, incremento, `break` fora de lugar).
</details>

#### Registro do Ciclo 06 — 30/09
1. **Desafio do ciclo (em 1 frase):** Garantir o controlo correto das repetições e das condições de paragem no CRUD de anúncios (Anuncify) sem provocar laços infinitos, encerramentos indevidos ou perda de dados.
2. **O que implementei (commits / arquivos / links):** Revisão do laço principal do menu (while opcao != "5") e das verificações de estado dos anúncios (anuncio1, anuncio2, anuncio3) no código do CRUD.
3. **Objeto(s) de conhecimento mobilizado(s):** Estruturas de repetição (for, while), controlo de fluxo (break, continue), condições de paragem e variáveis de controlo (opcao, num).
4. **Desvio ou erro encontrado + causa técnica:** Na execução do laço principal do menu (while), a utilização ou o posicionamento inadequado de instruções de interrupção/fluxo ou a atualização incorreta da condição de paragem pode encerrar o menu antes do previsto ou repetir a mesma condição sem avançar o estado; no meu fluxo com anuncio1, anuncio2 e anuncio3, o controlo baseia-se na condição do while e na limpeza da variável num (num = "") quando há falha ou cancelamento.
5. **Decisão de ajuste + fonte:** Mantive o while opcao != "5" para o menu contínuo (uma vez que o número de interações do utilizador não é fixo à partida) e controlei a interrupção de operações inválidas ou canceladas via num = "" e condicionais, com base nas aulas Curso Python #06 – Tipos Primitivos e Saída de Dados e Exercício Python #004 – Dissecando uma Variável (Gustavo Guanabara — Curso em Vídeo) e no apoio do ChatGPT.
6. **Feedback recebido (inclui devolutiva da P1) e o que mudei:** Neste ciclo, o professor Rondineli ainda não havia realizado a devolutiva formal da avaliação P1. Entretanto, durante as aulas, acompanhei as dúvidas apresentadas pelos colegas e as explicações fornecidas pelo professor, utilizando essas orientações gerais para compreender melhor os conteúdos trabalhados. Não recebi feedback individual específico sobre meu CRUD neste ciclo. A partir dessas orientações gerais e da revisão do laço while no Anuncify (anuncio1, anuncio2, anuncio3), reforcei a verificação da condição de saída e a limpeza da variável de controle num = "" quando ocorre entrada inválida ou cancelamento, evitando alterações ou exclusões indevidas.
7. **Próximo passo:** Aprofundar o uso de laços de repetição (while e for) para validar entradas inválidas sem interromper o fluxo do menu e iniciar o estudo de listas em Python, visando substituir as variáveis individuais (anuncio1, anuncio2, anuncio3) por uma estrutura capaz de armazenar e percorrer múltiplos anúncios de forma dinâmica no CRUD.

## 🟠 CICLO 07 — 07/10 — Listas: armazenamento e iteração

<details>
<summary>📘 Orientações do Ciclo 07</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 07.
- Justifique **por que seus dados cabem em uma lista** e como você os percorre (iteração).
- Item 4: erros típicos — índice fora do intervalo, alterar a lista enquanto percorre, confundir cópia com referência. Registre qual deles aconteceu e a causa técnica.
- Item 3: nomeie as **operações de lista** que usou (adicionar, remover, ordenar, fatiar…).
</details>

#### Registro do Ciclo 07 — 07/10
1. **Desafio do ciclo (em 1 frase):** Substituir as variáveis fixas (anuncio1, anuncio2, anuncio3) por uma lista no CRUD Anuncify, permitindo armazenar múltiplos anúncios e percorrê-los de forma iterativa sem erros de índice ou alteração indevida durante a iteração.
2. **O que implementei (commits / arquivos / links):** Estruturação da lista de anúncios no CRUD e laços de iteração para exibir, consultar, atualizar e remover registros.
3. **Objeto(s) de conhecimento mobilizado(s):** Listas em Python, iteração (for e while), indexação, fatiamento e operações de lista (adicionar, remover, consultar/alterar elementos).
4. **Desvio ou erro encontrado + causa técnica:** Ao percorrer a lista de anúncios para exibir ou remover itens, ocorreu risco de erro de índice fora do intervalo (IndexError) ou de pular/alterar elementos de forma inesperada quando a condição de parada ou a posição acessada não acompanhava o tamanho atual da lista. A causa técnica esteve na gestão da indexação e da condição de iteração em relação às alterações no tamanho da estrutura durante a execução.
5. **Decisão de ajuste + fonte:** Passei a armazenar os anúncios em uma lista em vez de variáveis isoladas (anuncio1, anuncio2, anuncio3) para lidar com uma coleção ordenada de tamanho variável e percorrê-la com iteração, verificando os limites dos índices antes de acessar ou remover posições para evitar erros de índice fora do intervalo ou alterações indevidas durante o percurso. Fonte: Curso Python #16 - Tuplas, Curso Python #17 - Listas (Parte 1) e Curso Python #17 - Listas (Parte 2), de Gustavo Guanabara (Curso em Vídeo), com apoio do ChatGPT.
6. **Feedback recebido e o que mudei:** A partir das orientações gerais em aula e da revisão prática do CRUD, reforcei a validação dos índices/posições antes de modificar ou excluir anúncios, evitando acessos inválidos ou remoções acidentais.
7. **Próximo passo:** Avançar para o estudo de consulta/busca e organização de cada anúncio com estruturas mais estruturadas (como dicionários) no Ciclo 08, tratando falhas de busca por chave, tipo ou item inexistente.

## 🟠 CICLO 08 — 14/10 — Busca/consulta e introdução a dicionários e matrizes

<details>
<summary>📘 Orientações do Ciclo 08</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 08.
- Explique **por que cada item do seu catálogo virou um dicionário** (chave → valor) em vez de uma lista de valores soltos.
- Item 4: registre **qual busca falhou** (item inexistente, tipo diferente — `"2"` ≠ `2`, chave com maiúscula errada) e a causa técnica.
- Se usou o lote de dados defeituoso, registre **qual registro** quebrou a busca.
- Item 5: cite a fonte (*Pense em Python*, cap. 11, ou outra).
</details>

#### Registro do Ciclo 08 — 14/10
1. **Desafio do ciclo (em 1 frase):** Estruturar cada anúncio do Anuncify como um dicionário (chave -> valor) para tornar a busca e a consulta de atributos mais claras, legíveis e independentes de posições fixas em listas de valores soltos.
2. **O que implementei (commits / arquivos / links):** Refatorei a estrutura de representação dos anúncios no código do CRUD Anuncify para utilizar dicionários com chaves nomeadas para os atributos do anúncio (como título, descrição, preço, categoria, vendedor e localização), organizei a coleção/catálogo de registros e implementei/ajustei a rotina de busca/consulta para localizar anúncios pelos campos/chaves e tratar entradas ou correspondências inválidas sem quebrar o laço principal do menu (while). (Se você tiver o nome do arquivo .py ou o hash/mensagem do commit no repositório, coloque aqui também.)
3. **Objeto(s) de conhecimento mobilizado(s):** Dicionários em Python (chave -> valor), acesso a valores por chave, listas/matrizes, iteração (for e while), estruturas condicionais (if/elif/else), validação/normalização de entradas e operações de busca/consulta.
4. **Desvio ou erro encontrado + causa técnica:** Durante a busca/consulta de anúncios, ocorreram falhas quando a entrada digitada divergia no formato/tipo ou na grafia em relação aos dados armazenados (por exemplo, diferença de maiúsculas/minúsculas ou espaços extras na string buscada, comparação de valores de tipos diferentes como texto e número — ex.: "2" vs 2 — ou tentativa de consultar uma chave/valor inexistente). A causa técnica foi a comparação direta sem padronização prévia dos textos/tipos e a ausência de verificação explícita da existência da chave ou do registro antes de ler/exibir o resultado.
5. **Decisão de ajuste + fonte:** Adotei dicionários (chave -> valor) para cada anúncio em vez de manter apenas listas de valores soltos porque cada anúncio possui atributos identificados por nome (como título, preço e categoria), o que evita confundir a ordem/posição de um campo com seu significado e facilita consultar ou validar propriedades específicas; na busca, passei a padronizar/validar o critério antes de comparar e a tratar casos sem correspondência com mensagem amigável. Fonte: aulas de Gustavo Guanabara (Curso Python #16 - Tuplas, Curso Python #17 - Listas (Parte 1) e Curso Python #17 - Listas (Parte 2) — Curso em Vídeo), Pense em Python (cap. 11) e apoio do ChatGPT.
6. **Feedback recebido e o que mudei:** A partir das explicações em aula e dos testes práticos de consulta no CRUD, reforcei o tratamento de buscas sem retorno ou com formatação diferente para que o programa exiba o aviso adequado e retorne ao menu principal sem erro em tempo de execução.
7. **Próximo passo:** Implementar a atualização e a exclusão de anúncios na estrutura com dicionários, mantendo a validação de entradas e a consistência dos dados no CRUD.

---

# 🔵 GRUPO 3 — prazo quinta 26/11 às 23h59

> **Janela:** sábado 21/11 → quinta 26/11. **O que entregar:** Registros dos Ciclos 09, 10, 11 e 12 · Campo 05 (duas revisões por pares) · Campo 06 · Campo 07.
>
> ⚠️ O prazo vem **um dia depois da P2 (25/11)**. Os Campos 06 e 07 dependem de todo o Logbook: deixe-os para o final, mas **adiante o rascunho do 6c e do 7a/7b antes da Defesa (18/11)**.

**Checklist do Grupo 3**
- [ ] Registros dos Ciclos 09, 10, 11 e 12 com os 7 itens
- [ ] Campo 05: duas revisões (Ciclos 09 e 12), blocos 5a a 5e
- [ ] Campo 06: decisão autônoma, lacuna com plano, pergunta da banca com 5 linhas ou mais
- [ ] Campo 07: 7a a 7e, com 3 objetos, 2 equívocos corrigidos e transferência
- [ ] Coerência entre Campo 01 e Campo 07
- [ ] Painel de acompanhamento completo

## 🔵 CICLO 09 — 21/10 — Atualização e exclusão: CRUD completo

<details>
<summary>📘 Orientações do Ciclo 09 — Registro + Campo 05 (revisão por pares nº 1)</summary>

- Neste ciclo seu CRUD ficou **completo** (Create, Read, Update, Delete). Preencha o Registro do Ciclo 09.
- **Item 4:** *atualizar* ou *excluir* item inexistente, e excluir durante um laço (a lista muda de tamanho e itens são pulados) são erros comuns.
- **Campo 05 — Registro de Revisão por Pares.** Você passa a ser **revisor** do CRUD de um colega.
  - Cada revisão tem **um registro** (copie a seção do Campo 05) com o nome e o link do repositório revisado.
  - **Revise o processo, não só o código:** o que foi decidido, em que objeto de conhecimento se apoia, com que fonte.
  - **5a:** liste as etapas da revisão (ex.: rodar o CRUD, testar com o lote de dados com defeito, ler o código, registrar achados, devolver feedback).
  - **5b:** liste os insumos que usou (lote de dados, casos de teste, `requisitos.md`) com quantidade planejada, utilizada e variação.
  - **5c:** diga se a solução do colega atende ao critério (Sim/Parcialmente/Não) e **qual critério** usou (ex.: requisito do `requisitos.md`).
  - **5d:** riscos da revisão (ex.: não conseguir rodar o código do colega) e como mitigou.
  - **5e:** registre **cada decisão técnica** da revisão com **data, responsável, objeto de conhecimento e fundamentação/referência**. *Sem objeto e sem referência, não é rastreável.*
  - Feedback ao colega: **específico e respeitoso** (o que está bom, o que quebrou, como reproduzir, sugestão).
</details>

#### Registro do Ciclo 09 — 21/10
1. **Desafio do ciclo (em 1 frase):** Concluir o CRUD do Anuncify implementando a atualização e a exclusão de anúncios na estrutura de lista de dicionários sem quebrar índices nem deixar registros inconsistentes.
2. **O que implementei (commits / arquivos / links):** Operações de atualização (Update) e exclusão (Delete) de anúncios integradas ao fluxo do CRUD no repositório do Anuncify (com validação de existência do registro antes de alterar ou remover). Repositório:https://github.com/joasfranco/Algoritmos-e-programacao/blob/main/Crud-Anuncify.py
3. **Objeto(s) de conhecimento mobilizado(s):** Listas, índices, atribuição de valores, remoção de elementos(como del ou filtragem/remoção por condição), busca por ID e estruturas condicionais if/else para localizar registros e confirmar exclusão.
4. **Desvio ou erro encontrado + causa técnica:** Ocorreu falha ao tentar atualizar/excluir um anúncio inexistente ou ao remover itens durante uma iteração sobre a lista. A causa técnica foi tentar acessar/remover um elemento sem validar previamente sua existência ou alterar o tamanho da lista enquanto o laço avançava por índice, deslocando posições e pulando ou estourando limites.
5. **Decisão de ajuste + fonte:** Passei a validar a existência do anúncio antes de aplicar alterações ou exclusões e a evitar remoção direta que altere o índice durante a varredura do laço, apoiando-me nas aulas de Gustavo Guanabara (Curso em Vídeo — Python) e no apoio do ChatGPT.
6. **Feedback recebido e o que mudei:** Não recebi feedbacks neste ciclo; a partir da revisão prática do CRUD com lista e dicionários, reforcei a validação de existência antes de alterar ou remover registros e evitei mutar a lista durante laços de percurso, exibindo mensagens claras para itens inexistentes ou exclusões não confirmadas.
7. **Próximo passo:** Planejava evoluir o CRUD com o uso de listas e laços de repetição para manipular registros de forma mais flexível, evitando repetição de trechos repetitivos e reduzindo falhas na atualização e exclusão. Embora o fluxo básico já estivesse funcional, buscava estruturar melhor o código e as validações para tornar as operações mais seguras, limpas e fáceis de manter nas etapas seguintes.
### 🧩 CAMPO 05 — Registro de Revisão por Pares
*Adaptação do **Logbook do Time** (Apêndice C) para o CRUD individual. Documento atualizado pelo **revisor**. Cada decisão técnica relevante deve ter associado o objeto de conhecimento correspondente.*

> ⚠️ **Nota de adaptação:** o Apêndice C original prevê Gestor, Responsável Técnico, Analista de Qualidade e Comunicador. Como o CRUD é **individual** e os alunos atuam como **revisores**, mantive os blocos 5a a 5e e troquei os papéis por **Autor** (dono do CRUD) e **Revisor** (você). *Pendente de validação do professor/NDE.*

> **O Logbook de revisão é um registro de conhecimento em ação.** Cada decisão técnica relevante deve estar associada ao objeto de conhecimento que a fundamenta, à justificativa técnica e à referência utilizada. Registros sem esse vínculo não são aceitos.

#### Revisão nº 1

| | |
|---|---|
| **Autor do CRUD revisado** | Enzo figueiredo |
| **Repositório revisado** | [](https://github.com/enzofigueiredo09/Algoritmos-e-Programa-o/blob/main/1%C2%B0%20Prazo%20do%20CRUD%20(1511)) |
| **Revisor** | Joás franco rodrigues |
| **Unidade curricular / Semestre** | Algoritmos e Programação · 2026.2 |
| **Ciclo / data** | _Ciclo 09 · 26/11_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO — análise técnica de cada etapa:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 1. Inspeção do código-fonte e arquitetura de dados | Revisor / Autor | _26/11_ | ☑ Concluída ☐ Em andamento ☐ Com desvio | Estrutura modularizada em funções com lista de dicionários (ingressos) e matriz (parques_horarios); ausência de requisitos.md.|
| 2. Execução do fluxo CRUD e verificação de entradas | Revisor / Autor | _26/11_ | ☑ Concluída ☐ Em andamento ☐ Com desvio | Operações básicas operacionais, mas int(input(...)) não trata exceção ValueError em entradas não numéricas. |
| 3. Teste de limites, índices e mutação de lista | Revisor / Autor | _26/11_ | ☑ Concluída ☐ Em andamento ☐ Com desvio | Verificação de intervalo (1 <= numero <= len(lista_ingressos)) funcional; remoção via .pop() ocorre sem confirmação explícita. |
| 4. Diagnóstico técnico e rastreabilidade das decisões | Revisor / Autor | _26/11_ | ☑ Concluída ☐ Em andamento ☐ Com desvio |Falhas mapeadas por objeto de conhecimento, justificativa técnica e fonte. |
| 5. Devolutiva técnica estruturada ao autor | Revisor / Autor | _26/11_ | ☑ Concluída ☐ Em andamento ☐ Com desvio | Feedback objetivo entregue com reprodução do erro e recomendações de robustez. |

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| Código-fonte do CRUD (crud.py) | 1 | 1 | 0 | Analisado quanto à modularização, estruturas de dados, indexação e controle de fluxo. |
| Casos de teste (cenários válidos, limites e inválidos) | 6 | 6 | 0 | Avaliaram criação, leitura, atualização por índice, exclusão via .pop(), consulta matricial e entradas inválidas. |
| Especificação de requisitos (requisitos.md) | 1 | 0 | -1 | Arquivo ausente; os requisitos funcionais foram inferidos a partir do menu e das rotinas implementadas. |

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:**validação de tipos e limites de índice, consistência de estruturas compostas (lista de dicionários e lista aninhada/matriz) e tratamento de entradas inválidas.
- **A solução atende?** ☐ Sim ☑ Parcialmente ☐ Não

**5d. GESTÃO DE RISCOS:**
- **Risco:** Exceção não tratada (ValueError) na conversão int(input(...)) interrompendo o laço while True da função main(), além de deleção destrutiva sem confirmação do usuário.
- **Estratégia de mitigação:** Executar testes de entrada inválidas sem alterar o código original e propor validação prévia de string numérica / confirmação condicional antes de .pop().

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| _26/11/26_ | Validar se a entrada é numérica antes de invocar int() para prevenir ValueError em tempo de execução. | Revisor | Tipos primitivos, conversão de tipos e validação de entrada | Documentação oficial do Python — Built-in Functions (int(), input()) e Tratamento de Erros |
| _DD/MM/AA_ | Condicionar lista_ingressos.pop(numero - 1) a confirmação explícita do usuário antes da mutação da lista. | Revisor | Estruturas condicionais (if/else) e mutabilidade de listas | Pense em Python (Downey) e aulas de Algoritmos e Programação (2026.2) |
| _DD/MM/AA_ | Normalizar strings de entrada (.strip().title()) para reduzir inconsistências em chaves/valores de dicionários. | Revisor | Manipulação de strings e dicionários | Documentação oficial do Python — String Methods |
| _DD/MM/AA_ | Adotar as operações do menu e do CRUD como critério funcional na ausência de requisitos.md. | Revisor | Verificação funcional e engenharia de requisitos | Protocolo / Logbook AFP 2026.2 — Campo 05 |
| _DD/MM/AA_ | Preservar a representação em lista de dicionários e matriz de horários pela adequação ao escopo atual. | Revisor | Listas, matrizes (listas aninhadas) e dicionários | Aulas de Algoritmos e Programação (2026.2) |

> **IMPORTANTE:** Decisão registrada sem objeto de conhecimento associado e sem referência é considerada **não rastreável** e não conta para a avaliação formativa. O vínculo entre processo e conteúdo é obrigatório em todas as decisões relevantes.

## 🔵 CICLO 10 — 28/10 — Modularização: funções

<details>
<summary>📘 Orientações do Ciclo 10</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 10.
- Explique **como dividiu** o CRUD em funções (`cadastrar()`, `buscar()`, `alterar()`, `excluir()`, `listar()`, `menu()`) e **por que** cada função tem aquela responsabilidade.
- Item 4: erros típicos — variável fora de escopo, função sem `return`, parâmetro na ordem errada.
- Compare o código **antes e depois** da refatoração: o que ficou mais claro? Registre no item 6 o feedback do colega que fez a *peer review*.
</details>

#### Registro do Ciclo 10 — 28/10
1. **Desafio do ciclo (em 1 frase):** Modularizar o CRUD do Anuncify em funções com responsabilidades bem definidas, reduzindo repetição e controlando escopo, parâmetros, retornos e feedback da revisão por pares.
2. **O que implementei (commits / arquivos / links):** Refatoração do CRUD para funções dedicadas (como cadastro, busca, listagem, atualização, exclusão e menu), substituindo blocos repetitivos no fluxo principal e ajustando a passagem de parâmetros e retornos.
3. **Objeto(s) de conhecimento mobilizado(s):** Modularização e definição de funções (def), escopo de variáveis (local vs. global), passagem de parâmetros e argumentos, retorno de valores (return), listas, dicionários e controle de fluxo.
4. **Desvio ou erro encontrado + causa técnica:** Ocorreram problemas típicos de modularização, como tentar usar variável local fora do seu escopo, chamar função sem return esperando valor ou passar parâmetros em ordem trocada, alterando valores no campo errado ou deixando o chamador sem o resultado esperado.
5. **Decisão de ajuste + fonte:**Separei cada operação em função própria — menu para navegação, cadastro para criar registros, busca para localizar itens, listagem para exibir, atualização para alterar campos e exclusão para remover — definindo parâmetros explícitos e retornos claros, com base nas aulas de Gustavo Guanabara (Curso em Vídeo — Python) e no apoio do ChatGPT.
6. **Feedback recebido e o que mudei:** A partir da peer review do colega, reforcei a validação de entradas/índices dentro das funções e deixei o retorno e o estado da lista mais previsíveis, evitando alterações indevidas ou falhas silenciosas.
7. **Próximo passo:** Avançar para o estudo de recursividade no Ciclo 11, avaliando onde o problema pode ser decomposto com caso base e passo recursivo sem gerar loop infinito.

## 🔵 CICLO 11 — 04/11 — Recursividade

<details>
<summary>📘 Orientações do Ciclo 11 — Registro + Campo 06 (Grupo 3)</summary>

- Preencha o Registro do Ciclo 11 (caso base, chamada recursiva, pilha de execução).
- **Campo 06 — Próximos passos para a defesa** · *individual · quinta 26/11, 23h59*. Prepare-se para a **Defesa Técnica de quarta 18/11**: como o prazo é posterior à defesa, **adiante pelo menos o 6c** (pergunta da banca e resposta) e leve-o para a arguição.
  - **6a.** Uma **decisão técnica que você defende com plena autonomia**: algo que aprendeu e **é exclusivamente seu**, que nenhum colega consegue explicar por você.
  - **6b.** Uma **lacuna técnica real** e um **plano de ação** com passos e datas para saná-la antes da defesa.
  - **6c.** Uma **pergunta que a banca pode fazer** (nível de Avaliação ou Criação) e a sua **resposta fundamentada em, no mínimo, 5 linhas**, com o objeto de conhecimento e a fonte.
  - Dica: leia a **Rubrica de Defesa Técnica** (no Encerramento) e escolha uma pergunta que teste *aplicação*, *evolução* ou *transferência*.
</details>

#### Registro do Ciclo 11 — 04/11
1. **Desafio do ciclo (em 1 frase):** Compreender e aplicar recursividade (caso base, chamada recursiva e pilha de execução) em problemas divisíveis em subproblemas menores sem gerar loop infinito ou RecursionError.
2. **O que implementei (commits / arquivos / links):** Exercícios e testes práticos de funções recursivas e análise de casos aplicáveis no escopo do meu Crud.
3. **Objeto(s) de conhecimento mobilizado(s):** Recursividade, caso base, passo recursivo, pilha de chamadas (call stack), retorno de valores (return) e estruturas condicionais (if/else).
4. **Desvio ou erro encontrado + causa técnica:** Ocorreram casos de recursão sem caso base adequado ou com passo recursivo que não converge para o caso base, esgotando a pilha de chamadas e provocando RecursionError, além de esquecer o return na chamada recursiva e perder o resultado empilhado.
5. **Decisão de ajuste + fonte:** Definir sempre um caso base explícito e garantir que cada chamada recursiva avance em direção a ele retornando o valor acumulado, apoiando-me em Pense em Python (Downey), na documentação oficial do Python e nas aulas de Algoritmos e Programação.
6. **Feedback recebido e o que mudei:** A partir das verificações práticas e orientações de aula, passei a preferir laços iterativos para operações lineares simples do CRUD (como menus e varreduras diretas) e reservar recursividade para estruturas ou problemas naturalmente hierárquicos/divisíveis, com caso base bem delimitado.
7. **Próximo passo:** Refatorar e elevar a qualidade do código no Ciclo 12 — eliminando duplicações, melhorando nomes e organização das funções, tratando entradas inválidas e revisando a robustez do CRUD frente a casos de teste e dados defeituosos.

### 🧩 CAMPO 06 — Próximos passos para a defesa
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

**6a. Decisão técnica que defendo com plena autonomia — o que aprendi que é exclusivamente meu e não consigo transferir para nenhum colega:**

> A escolha de implementar o CRUD do Anuncify usando apenas recursos nativos do Python, sem bibliotecas externas e sem listas estruturadas inicialmente, organizando os anúncios em variáveis explícitas e controlando o limite de 3 vagas, a existência dos registros e a limpeza das variáveis na exclusão.

**6b. Lacuna técnica e plano de ação para saná-la:**

- **Lacuna:** Armazenamento volátil apenas em memória (sem persistência em arquivo/banco), limite fixo de 3 anúncios e ausência de listas estruturadas na versão apresentada na defesa, além da necessidade de tornar o tratamento de entradas inválidas ainda mais robusto._
- **Plano de ação (passos e datas):** Até 18/11: Revisar o fluxo de criação, consulta, alteração e exclusão no Anuncify e ensaiar a defesa de cada decisão técnica e limitação do projeto. Até 26/11: Consolidar o registro no Logbook AFP com o Campo 06 preenchido, registrando os próximos passos de evolução do sistema (como migração para estruturas mais escaláveis e persistência de dados).

**6c. Pergunta que a banca pode fazer — com resposta fundamentada (mínimo 5 linhas):**

- **Pergunta:** Como você declarou e utilizou as variáveis no Anuncify para gerenciar o ciclo de vida dos anúncios (criar, consultar, modificar e excluir) sem usar listas estruturadas ou bibliotecas externas, e quais limitações essa escolha traz?
- **Resposta:**

> No Anuncify, as variáveis foram declaradas diretamente em Python — por tipagem dinâmica, no momento da atribuição — para representar tanto os dados de cada anúncio (como título, descrição, preço, categoria, vendedor e localização) quanto o controle do estado e das vagas disponíveis. Na criação (Create), os valores recebidos via entrada são atribuídos às variáveis após checar o limite máximo de 3 anúncios; na consulta (Read), os registros ativos são lidos para exibição ou sinalizam base vazia; na alteração (Update), a existência do anúncio é verificada antes de sobrescrever seus campos; e na exclusão (Delete), o registro ativo é localizado e suas variáveis são limpas para liberar espaço a um novo cadastro. Essa abordagem permitiu focar na lógica, nas condicionais e no controle de fluxo usando apenas recursos nativos da linguagem, mas impõe restrições claras: limite de 3 anúncios, ausência de listas estruturadas e dados mantidos apenas em memória (sem persistência).

**Objeto de conhecimento mobilizado:** Variáveis, tipos de dados, atribuição, estruturas condicionais, estruturas de repetição e controle de fluxo em Python.
**Fonte:** DOWNEY, Allen B. Pense em Python: Pense como um cientista da computação. Capítulo 10 — Listas; explicações do professor Rondineli Seba Salomão durante a aula sobre buscas.

## 🔵 CICLO 12 — 11/11 — Refatoração e qualidade de código

<details>
<summary>📘 Orientações do Ciclo 12 — Registro + Campo 05 (revisão nº 2) + início do Campo 07</summary>

- Preencha o Registro do Ciclo 12. Registre o que revisou: código duplicado, nomes ruins, funções grandes, comentários desnecessários, lógica confusa.
- **Campo 05 — Revisão por pares nº 2.** Foque em **qualidade**: o CRUD do colega resiste aos casos de teste (mínimos, máximos, inválidos, entradas vazias) e ao **lote de dados com defeito**? Use a seção abaixo (copie o bloco *Revisão nº 1* do Ciclo 09 e preencha novamente).
- **Campo 07 — Evolução conceitual** · *individual · quinta 26/11, 23h59.* Comece agora, enquanto a memória do semestre está fresca; leve o rascunho de 7a e 7b para a Defesa de 18/11. Dicas por item:
  - **7a.** Releia o **Campo 01** e resuma o que você *pensava* e *achava que sabia*. Seja honesto, mesmo se o Campo 01 estiver "errado".
  - **7b.** Pelo menos **3 objetos de conhecimento** na tabela: o que você *não dominava*, o que *aprendeu e consegue demonstrar* e a **evidência** (em qual Campo ou ciclo do Logbook aparece).
  - **7c.** Pelo menos **2 equívocos corrigidos**, dizendo **o que os corrigiu** (Fechamento Teórico, pesquisa, *Peer Review*, arguição, devolutiva da P1).
  - **7d.** **Transferência:** um exemplo concreto de aplicar o que aprendeu em um **contexto diferente** do CRUD (outra área do seu curso ou outro tipo de sistema).
  - **7e.** Avaliação honesta do que **ainda não domina** e vai aprofundar.
</details>

#### Registro do Ciclo 12 — 11/11
1. **Desafio do ciclo (em 1 frase):** Refatorar o código do Anuncify e revisar a qualidade de um CRUD par para eliminar duplicações, melhorar nomes e legibilidade, reduzir funções extensas e tornar as validações mais resistentes a entradas inválidas.
2. **O que implementei (commits / arquivos / links):** Refatoração de trechos duplicados, padronização de nomes de variáveis e funções, limpeza de comentários redundantes e reforço das verificações de fluxo no repositório do Anuncify (docs(logbook): ciclo 12 e revisao 2 / ajustes no código do CRUD).
3. **Objeto(s) de conhecimento mobilizado(s):** Refatoração de código, modularização, legibilidade e nomenclatura, validação de entrada, estruturas condicionais (if/elif/else), laços de repetição, listas e dicionários.
4. **Desvio ou erro encontrado + causa técnica:** Havia trechos repetidos para exibir/validar anúncios, nomes genéricos ou pouco descritivos, comentários repetindo o óbvio e lógica de validação dispersa; a causa técnica foi o acréscimo incremental de funcionalidades nos ciclos anteriores sem consolidar padrões de entrada e exibição.
5. **Decisão de ajuste + fonte:** Extraí validações/exibições repetidas para pontos únicos, renomeei identificadores conforme o domínio do Anuncify, removi comentários desnecessários e simplifiquei condições aninhadas, apoiando-me nas aulas de Algoritmos e Programação (Prof. Rondineli Seba Salomão, 2026.2), em Pense em Python (Downey) e na documentação oficial do Python.
6. **Feedback recebido e o que mudei:** A partir da revisão crítica do próprio código e da revisão por pares, tornei as mensagens de erro mais objetivas, evitei duplicação de checagens de existência/limite e mantive o controle de fluxo previsível mesmo com entradas malformadas.
7. **Próximo passo:** Consolidar o fechamento do Grupo 3 no Logbook AFP (Campos 05, 06 e 07), garantindo coerência entre o Campo 01, a Defesa Técnica e o Campo 07.

### 🧩 CAMPO 05 — Registro de Revisão por Pares (revisão nº 2)

| | |
|---|---|
| **Autor do CRUD revisado** | Enzo figueiredo |
| **Repositório revisado** | _[link](https://github.com/enzofigueiredo09/Algoritmos-e-Programa-o/blob/main/1%C2%B0%20Prazo%20do%20CRUD%20(1511)_ |
| **Revisor** | Joás franco rodrigues |
| **Ciclo / data** | _Ciclo 12 · 26/11_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 1. Inspeção estática (duplicação, nomes, tamanho de funções e comentários) | Revisor | _26/11_ | ☑ Concluída ☐ Em andamento ☐ Com desvio | mudar_parque e cancelar_ingresso repetem a listagem formatada; funções curtas e legíveis, com comentários pontuais. |
| 2. Teste de casos mínimos, máximos e de borda | Revisor | _26/11_ | ☑ Concluída ☐ Em andamento ☐ Com desvio | Lista vazia (len == 0) e índices 1 e len(lista) tratados; ausência de checagem de string vazia ou espaços em nome/parque. |
| 3.Teste com entradas inválidas e lote de dados com defeito | Revisor | _26/11_ | ☑ Concluída ☐ Em andamento ☐ Com desvio | Entradas não numéricas em int(input(...)) geram ValueError; campos em branco ou variações de caixa (case) entram sem normalização. |
| 4. Consolidação dos achados e rastreabilidade técnica| Revisor | _26/11_ | ☑ Concluída ☐ Em andamento ☐ Com desvio | Falhas de qualidade e robustez vinculadas a objetos de conhecimento e referências. |
| 5. Devolução de feedback focado em qualidade | Revisor | _26/11_ | ☑ Concluída ☐ Em andamento ☐ Com desvio | Feedback objetivo entregue com cenários de falha, reprodução e refatorações recomendadas. |

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| Código-fonte do Crud (crud.py) | 1 | 1 | 0 | Revisado quanto a duplicação, clareza de nomes, modularidade e tratamento de erros. |
| Casos de teste (mínimos, máximos, inválidos e vazios) | 8 | 8 | 0 | Cobriram lista vazia, primeiro/último elemento, índice inválido, texto em int() e inputs em branco. |
| Lote de dados com defeito | 1 | 1 | 0 | Aplicado para verificar resistência a registros vazios, duplicidade de texto e tipos inesperados. |

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:** Resistência do CRUD a entradas inválidas/vazias e lote defeituoso, ausência de lógica duplicada crítica, clareza de nomes/funções e integridade de lista de dicionários e matriz.
- **A solução atende?** ☐ Sim ☑ Parcialmente ☐ Não

**5d. GESTÃO DE RISCOS:**
- **Risco:** Quebra por ValueError em entradas não numéricas, cadastro de campos vazios/espaços ou remoção acidental sem confirmação em lotes defeituosos.
- **Estratégia de mitigação:** Executar testes de estresse/defeito sem alterar o código original e propor validação de entrada (.strip(), checagem numérica ou try/except ValueError) e extração de helper para listagem.

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| _26/11/26_ | Rejeitar strings vazias ou só com espaços (.strip()) antes de criar ou alterar ingressos. | Revisor | Manipulação de strings e validação de entrada | Documentação oficial do Python — String Methods (str.strip()) |
| _26/11/26_ | Proteger conversões int(input(...)) contra ValueError antes de acessar índices da lista. | Revisor | Conversão de tipos, condicionais e tratamento de exceções | Documentação oficial do Python — Errors and Exceptions e Built-in Functions |
| _26/11/26_ | Extrair a exibição numerada de ingressos para reduzir duplicação entre mudar_parque e cancelar_ingresso. | Revisor | Modularização, funções e refatoração | Pense em Python (Downey) e aulas de Algoritmos e Programação (2026.2) |
| _26/11/26_ | Exigir confirmação antes de lista_ingressos.pop(numero - 1) em operações destrutivas. | Revisor | Estruturas condicionais (if/else) e mutação de listas | Aulas de Algoritmos e Programação (Prof. Rondineli Seba Salomão, 2026.2) |
| _26/11/26_ | Avaliar o CRUD frente a casos de borda e lote defeituoso como critério de qualidade do Ciclo 12. | Revisor | Testes de software, casos de borda e qualidade de código |Orientações do Logbook AFP 2026.2 — Ciclo 12 e Campo 05 |

### 🧩 CAMPO 07 — Evolução conceitual
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

*Evidência rastreável de aprendizagem entre o início e o encerramento do ciclo AFP.*

**7a. O que eu pensava no início do ciclo (com base no Campo 01 — registrar a hipótese inicial e os objetos de conhecimento que achava conhecer):**

> No início, eu imaginava resolver o CRUD de forma direta, apoiando-me na noção intuitiva de variáveis, condições e repetições que já conhecia por cima, sem antecipar com clareza os efeitos colaterais de tipos de dados (como o retorno em string de input()), limites de estrutura, mutação de coleções, escopo em funções e casos de borda. Achava que fazer "funcionar no cenário normal" já bastava para dar o problema por resolvido.

**7b. O que aprendi — conceitos, princípios ou relações técnicas que não dominava no início e que agora consigo explicar com precisão (mínimo 3 objetos de conhecimento):**

| OBJETO DE CONHECIMENTO | O QUE EU NÃO DOMINAVA | O QUE APRENDI E CONSIGO DEMONSTRAR | EVIDÊNCIA (campo do Logbook onde aparece) |
|---|---|---|---|
| Variáveis, tipos, conversão e validação de entrada | Achava que valores lidos e comparados se comportavam de modo óbvio, sem tratar strings vazias ou falhas em int(). | Sei validar entradas antes da conversão/uso, evitando erros de tipo e mantendo o fluxo estável em entradas inválidas. | Campo 01, Campo 03, Ciclos 09 e 12, Defesa Técnica |
| Estruturas condicionais, operadores lógicos e laços | Misturava condições sem cobrir bem casos de borda ou alterações de tamanho/estado durante iteração. | Sei estruturar if/elif/else, and/or/not e laços com condições de guarda e limites explícitos. | Ciclos 05, 09 e 11, Defesa Técnica |
| Listas, dicionários, modularização e refatoração | Não dominava a organização limpa em estruturas compostas e funções com escopo, parâmetros e retornos claros, nem a refatoração para eliminar duplicações. | Sei estruturar dados em coleções, dividir responsabilidades em funções e refatorar código mantendo clareza e rastreabilidade. | Ciclos 09, 10 e 12, Campo 05, Defesa Técnica |

**7c. Conceitos que precisei corrigir ao longo do ciclo — onde eu estava equivocado e o que o corrigiu (Fechamento Teórico, pesquisa, Peer Review, arguição):**

1. **Equívoco:** Achar que um fluxo CRUD básico funcionando no caminho feliz já cobre cenários de borda, entradas inválidas ou efeitos de alterar/remover registros. — **Correção:** Passar a validar pré-condições, limites e estados antes de alterar ou remover dados.
   **O que corrigiu:** Prática nos ciclos do CRUD, testes de casos inválidos, Peer Review (Campo 05) e orientações em aula/arguição.
2. **Equívoco:** Pensar que refatorar ou dividir em funções é apenas "enfeitar" ou mexer no código depois de pronto, sem vínculo com escopo, responsabilidade e qualidade. — **Correção:** Tratar modularização e refatoração como decisões técnicas guiadas por clareza, redução de duplicação, escopo/parâmetros e fontes verificáveis.
   **O que corrigiu:** Ciclos 10 e 12, pesquisa em Pense em Python / documentação oficial e revisão por pares.
**7d. Transferência — como este aprendizado se aplica a um contexto diferente do problema trabalhado (ao menos 1 exemplo concreto da área de formação):**

> Em Engenharia de Software, ao desenvolver um script de automação ou API/serviço de cadastro de chamados ou ativos de TI, os mesmos fundamentos se aplicam: validar e normalizar dados recebidos externamente antes de persistir, verificar existência e limites antes de atualizar/excluir, evitar mutar coleções enquanto se itera sobre elas e separar responsabilidades em funções pequenas e testáveis.

**7e. Avaliação honesta do próprio percurso — o que ainda não domino e preciso aprofundar após este ciclo:**

> Ainda não domino com profundidade o tratamento sistemático de exceções (try/except) em múltiplas camadas, a persistência durável de dados fora da memória (arquivos/bancos) e a escrita de suítes automatizadas de testes; pretendo aprofundar esses pontos na sequência do curso aplicando-os em projetos maiores e na evolução pós-defesa.

---

# 🏁 DEFESA TÉCNICA — quarta 18/11

<details>
<summary>📘 Orientações para a Defesa Técnica e preparação</summary>

**A Defesa é antes dos prazos dos Grupos 2 e 3.** Você será arguido sobre o que já estiver registrado e commitado. Priorize, até **terça 17/11**:
- [ ] **Grupo 1 entregue** (prazo 16/11): Identificação, Registros 01 a 04, Campos 01 e 02.
- [ ] **Campo 04 (IA)** e **Campo 03** ao menos em rascunho, para sustentar as perguntas sobre decisões (critérios 2 e 5).
- [ ] **Campo 06c** (pergunta da banca e resposta) e **rascunho de 7a e 7b**, para sustentar a evolução conceitual (critério 3).
- [ ] Registros dos Ciclos já feitos, mesmo que ainda não "entregues" no prazo do grupo.
- [ ] `README.md`, `docs/` e CRUD rodando.
- [ ] Você consegue explicar **cada linha** do seu código e **cada decisão** registrada.
- Os demais itens seguem com os prazos dos grupos (21/11 e 26/11). A banca pode consultar o histórico do Git.

**A Defesa Técnica é individual.** Você será arguido sobre o que registrou. Cada aluno recebe pelo menos **1 questão** nos níveis de **Avaliação** ou **Criação** (taxonomia de Bloom).

**Como a Rubrica se liga ao seu Logbook:**

| Critério da Rubrica | Onde você prepara a evidência |
|---|---|
| 1. Domínio dos objetos de conhecimento | Campos 01, 02 e 07b |
| 2. Aplicação do conteúdo à solução ⚠️ *inegociável* | Registros dos ciclos (itens 3 e 5), Campo 03c e Campo 05e |
| 3. Evolução conceitual ⚠️ *inegociável* | Campo 01 → Campo 07 (7a, 7b e 7c; leve o rascunho) |
| 4. Capacidade de transferência | Campo 07d |
| 5. Argumentação sob pressão | Campo 06c e Campo 04e |
| 6. Autonomia intelectual e coerência com o Logbook | Todo o Logbook (principalmente Campos 04 e 06a) |

**Treino:** peça a um colega que faça 3 perguntas "imprevistas" sobre o seu CRUD e responda **sem consultar** o Logbook. Se não conseguir, volte ao Campo 06b.
</details>

## 🧩 RUBRICA DE DEFESA TÉCNICA (revisada)
*Avaliação individual de cada membro na Semana 16. Cada membro recebe ao menos 1 questão nos níveis de Avaliação ou Criação da Taxonomia de Bloom. Critérios revisados para medir aprendizagem, aplicação, evolução e transferência do conteúdo.*

| | |
|---|---|
| **Nome** | _Joás franco rodrigues_ |
| **Curso / Time / Função** | _Engenharia de software_ |

<details>
<summary>🔒 Uso do professor — rubrica completa</summary>

| CRITÉRIO | EXCELENTE (4,0) | SATISFATÓRIO (3,0) | INSATISFATÓRIO (2,0) | AUSENTE (0) |
|---|---|---|---|---|
| **1. DOMÍNIO DOS OBJETOS DE CONHECIMENTO** — Responde com precisão técnica, sem apoio dos colegas, demonstrando aprendizagem do conteúdo. | Responde com precisão e profundidade, nomeando os objetos de conhecimento mobilizados sem hesitação. | Responde com precisão, com imprecisões pontuais que não comprometem o raciocínio. | Responde de forma vaga, com erros conceituais relevantes ou dependendo dos colegas. | Não responde ou demonstra desconhecimento total. |
| **2. APLICAÇÃO DO CONTEÚDO À SOLUÇÃO** — Demonstra como os objetos de conhecimento fundamentaram as decisões do processo. | Explicita com precisão qual objeto de conhecimento fundamentou cada decisão relevante do processo investigativo, citando referência e demonstrando por que aquele conhecimento era o mais adequado. | Estabelece a relação conteúdo-decisão na maioria das perguntas, com alguma imprecisão pontual. | Não consegue explicitar a relação entre o conteúdo e as decisões do processo investigativo com clareza. | Não demonstra nenhuma relação entre os objetos de conhecimento e as decisões tomadas. |
| **3. EVOLUÇÃO CONCEITUAL** — Demonstra aprendizagem em relação ao que sabia no início do ciclo. | Identifica com precisão o que aprendeu, o que corrigiu e como o conhecimento evoluiu ao longo do ciclo. | Demonstra evolução em parte dos conceitos trabalhados, com alguma dificuldade de articular a trajetória. | Dificuldade em identificar diferenças entre o que sabia no início e o que domina agora. | Não demonstra nenhuma percepção de evolução conceitual ao longo do ciclo. |
| **4. CAPACIDADE DE TRANSFERÊNCIA** — Aplica o conhecimento a um contexto diferente do problema trabalhado. | Consegue transferir o aprendizado para um contexto novo com fundamentação técnica precisa. | Realiza a transferência com imprecisões que não comprometem a lógica do raciocínio. | Demonstra dificuldade em aplicar o conhecimento a contextos diferentes do problema original. | Não consegue realizar nenhuma transferência do conhecimento para contexto diferente. |
| **5. ARGUMENTAÇÃO SOB PRESSÃO** — Mantém coerência técnica diante de questionamentos imprevistos. | Mantém raciocínio coerente, reconhece limites com honestidade e reformula com fundamentação. | Mantém coerência na maior parte, com hesitações pontuais sem perda do fio técnico. | Fragilidade técnica diante de questionamentos imprevistos. | Não sustenta argumentação técnica diante de nenhum questionamento. |
| **6. AUTONOMIA INTELECTUAL E COERÊNCIA COM O LOGBOOK** — Defende o que registrou com consciência e sem depender do grupo. | Defende com precisão as decisões do Logbook, demonstrando autoria plena e independência intelectual. | Defende a maioria das decisões com coerência, com alguma imprecisão ou apoio pontual. | Depende dos colegas ou demonstra desconhecimento de parte do que registrou no próprio Logbook. | Não reconhece o que registrou ou não demonstra autonomia intelectual durante a arguição. |

**PONTUAÇÃO:** _____ / 24,0 **CONCEITO:** _____________

**Conversão:** 20–24 = Excelente (4,0) | 14–19 = Satisfatório (3,0) | 8–13 = Insatisfatório (2,0) | < 8 = Ausente (0)

> ⚠️ **Critérios 2 (Aplicação) e 3 (Evolução Conceitual) são inegociáveis — AUSENTE em qualquer um deles implica nota máxima de 2,0 na Defesa, independentemente do desempenho nos demais.**

**OBSERVAÇÕES:** _…_

**Professor(a):** _________________  **Data:** ___________
</details>

### Registro do Encerramento — 18/11
1. **O que apresentei/defendi (em 1 frase):** Apresentei e defendi o CRUD do Anuncify em Python, explicando a declaração e o uso de variáveis para os atributos do anúncio, o controle de vagas e do ciclo de vida (criar, consultar, modificar e excluir) com recursos nativos da linguagem e as limitações da versão em memória.
2. **Objeto(s) de conhecimento que a banca mais explorou:** Variáveis, tipos de dados e atribuição, estruturas condicionais e de repetição, controle de fluxo em operações CRUD e evolução/limitações das estruturas de dados.
3. **Pergunta que mais me desafiou e como respondi:** A pergunta sobre como eu declarei e utilizei as variáveis no Anuncify (e as limitações dessa escolha) exigiu detalhar tanto a criação/reatribuição das variáveis em Python quanto a lógica de cada operação do CRUD sem depender de listas estruturadas ou bibliotecas externas. Respondi explicando que as variáveis são declaradas por atribuição na linguagem e usadas para armazenar os campos do anúncio e controlar o estado nas operações de criar (respeitando o limite de 3 vagas), consultar, modificar (validando existência antes de sobrescrever) e excluir (limpando as variáveis para liberar vaga), assumindo com clareza os limites de capacidade, ausência de listas estruturadas e armazenamento apenas em memória.
4. **O que levo deste semestre para o próximo módulo:** Levo o domínio das bases de lógica de programação, controle de fluxo e raciocínio estruturado para sustentar decisões técnicas, além do hábito de registrar hipóteses, erros, correções e transferências para problemas mais complexos.

---

# 🆘 Estou atrasado no Logbook. E agora?

1. **Não apague nem "retroescreva" o passado.** Preencha agora e **escreva a data real** do preenchimento (ex.: *"preenchido com atraso em 12/11"*).
2. **Campo 01 e Checkpoint (sem consulta):** se perdeu a janela, registre **o que sabe hoje, sem consultar nada**, marcando-o como *preenchimento tardio*. Combine o tratamento com o professor.
3. **Priorize a ordem dos grupos:** Grupo 1 (16/11) → Defesa (18/11) → Grupo 2 (21/11) → Grupo 3 (26/11). Dentro de cada grupo, os Campos vêm antes dos Registros.
4. **Use o histórico do Git** (`git log --oneline`) para reconstruir o que fez em cada ciclo — ele é uma evidência melhor que a memória.
5. **Fale com o professor** antes do prazo, não depois.
