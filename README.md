# Curso: Python começando com a linguagem
# Alura, Nico Steppat

Este repositório contém minhas anotações pessoais durante a jornada do curso. 
Referência oficial: https://docs.python.org/

## 01. Instalação do Python3

### Instalar python3

Existe para Windows, Mac e Linux
Pode usar sem instalar (testes básicos) na plataforma https://replit.com/languages/python3

### Funções e Variáveis

*Funções*

Uma função sempre terá um parenteses depois de seu nome
    
função print(paramentros)
função help(parametros)

*Exemplos*
    
    help(print)

    print("Brasil ganhou 5 copas do mundo")  
    Brasil ganhou 5 copas do mundo

    print("Brasil", "ganhou", 5, "copas do mundo", sep="-") 
    Brasil-ganhou-5-copas do mundo

    print("Brasil", "ganhou", 5, "copas", "do", "mundo", sep="-") 
    Brasil-ganhou-5-copas-do-mundo

    pais="italia"
    ntitulos=4

    type(pais)
    <class 'str'>

    type(ntitulos)
    <class 'int'>

Lembrando que o \n é um caractere especial, que faz com que o novo prompt (cursor) comece em uma nova linha.

    print(pais, "ganhou", ntitulos, "copas", "do", "mundo",sep=" ",end="!\n") 
    italia ganhou 4 copas do mundo!

*Outros exemplos usando variáveis:*

    dia = 15
    mes = 10
    ano = 2015

    print(dia,mes,ano,sep="/")
    15/10/2015

### Tipagem do Python

Uma variável só passa a existir quando atribuímos um valor.
Mesmo se declaramos o tipo e o nome da variável, sem ter atribuído o valor.
Em Python, a variável só passa a existir quando atribuímos um valor, como no exemplo abaixo:

*Exemplos*
    
    int idade

Veja que foi declarado apenas o nome e a tipagem da variável

    idade = 12

Após atribuir valor, a variável passa a existir

*Exemplos:*

    mes="ago"

    type(mes)
    <class 'str'>

    mes=8

    type(mes)
    <class 'int'>

    mes=8.9

    type(mes)
    <class 'float'>

Também existe o tipo bool (true or false)

*Snake_Case*

Padrão/convenção pra definição nomes de variáveis, usando o simbolo de underline (_) para separar as palavras

*Exemplo*

    idade_esposa = 20
    perfil_vip = 'Flávio Almeida'
    recibos_em_atraso = 30

*CamelCase*

Em outras linguagens usa-se o padrão CamelCase, que não é o padrão do Python, mas pode ser usado tbm no Python.
Neste caos, não se separam as palavras na variável. 

*Exemplo:*

    idadeEsposa = 20
    perfilVip = 'Flávio Almeida'
    recibosEmAtraso = 30

## 02. Lidando com a entrada do usuário

### Escolhendo a IDE (Integrated Development Environment)

O PyCharm é uma IDE voltada exclusivamente para o Python. 
https://www.jetbrains.com/pycharm/ usar versão community

Outra opção bastante popular é o VS Code. 

Executar primeiro projeto: JOGO DA ADIVINHAÇÃO

### Comparando variaveis

*Comparando uma variável*

Não se compara strings com inteiros. O sinal de igualdade é representado por ==
No Python não importa o número digitado, a comparação com == envolvendo tipos diferentes resultará em falso. Isso porque a função input sempre retorna um texto (string). 

    chute == num_secreto

*Convertendo uma variável*

Sendo assim, é necessário converter o valor retornado em inteiro, para que a comparação com outro inteiro, no caso o numero_secreto, seja possível. Realizamos essa conversão através da função int.

    int(chute_str)

### Testes lógicos

*Estrutura do if e else*

    if(num_secreto == chute):
        print("Você acertou. ")
    else:
        print("Você errou. ")

Também encontrado na forma sem parênteses, pois o Python aceita ambas as formas. 
Seguir a forma que usa parênteses, pois deixa mais claro qual é a condição, 
principalmente quando há várias condições a avaliar através das operações lógicas AND ou OR.

### Manipulando strings

*Somar string com int*

    idade1 = 10
    idade2 = int("20")
    print(idade1 + idade2)

*Concatenando strings*

    nome = "Nico"
    sobrenome = "Steppat"
    print(nome,sobrenome)
    print(nome,sobrenome, sep="_")
    print(nome + " " + sobrenome)

### Diferenças entre Python2 e Python3

*A função print*

No Python 2, não precisamos colocar os parênteses na função print. Já no Python 3, os parênteses são obrigatórios. Ainda na função print, no Python 2 não há os parâmetros sep e end e quando há mais parâmetros a saída é diferente. 

*A função input*

No Python 2, ela automaticamente converte o tipo da variável. Considerado má prática, porque se a intenção do desenvolvedor não for converter o tipo da variável. 
Por isso é bem comum encontrar a função raw_input sendo utilizada no Python 2: chute = raw_input("Digite o seu número: "); O retorno dessa função será sempre uma string, equivalente à função input do Python 3, mas ela não existe nessa versão.

*Resumo*

As funções input(...), print(...) e int(...) existem no Python 3.
A função raw_input(..) existe apenas no Python 2.

### Diferenças entre JavaScript e Python

*JavaScript* 

Faz conversões de acordo com o que julga necessário 

    num1 = 10
    10
    num2 = "20"
    '20'
    soma = num1 + num2
    '1020'
    multiplica = num1 * num2
    200

*Python* 

Não faz as conversões, porém simplifica algo que seria trabalhoso, mas não muda a característica da linguagem. 

    num1 = 10
    num2 = "20"
    soma = num1 + num2
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str

Então, ao invés de escrever dez vezes o número 20, podemos simplificar e escrever 10 * "20"

    num1 = 10
    num2 = "20"
    produto = num1 * num2
    print(produto)
    20202020202020202020

### Diferenças entre Terminal do Python e Prompt de comando do Windows/Linux

*Terminal do Python*

O terminal interativo do Python é uma ferramenta que permite executar comandos Python diretamente no terminal. Quando você digita um comando nele e pressiona Enter, o Python executa o comando imediatamente e retorna o resultado. Isso é ótimo para testar rapidamente pequenos pedaços de código Python ou explorar as funcionalidades da linguagem. Mas, em contrapartida, o terminal interativo do Python não serve para executar arquivos.

*Prompt de comando do Windows/Linux*

Essa ferramenta é uma interface de linha de comando mais geral que permite executar comandos do sistema operacional e outras tarefas relacionadas ao sistema como carregar um arquivo, e para fazer isso você deve escrever “nome do diretório com o comando cd”, que é um atalho para mudar de diretório no cmd do windows e linux, localizar o arquivo que deseja e executá-lo.

### Config. UTF-8 no VS Code

UTF-8 é um formato de codificação que permite que caracteres especiais e acentos sejam exibidos corretamente ao digitar no editor de códigos.
Procurar settings para mudar o formato. 

## 03. Testando Valores

### A condição elif

Em alguns casos casos, para forçar testar uma condução no senão (else), podemos fazer um else com uma condição de entrada, o elif. 
Vamos utilizá-lo para deixar o código mais semântico, já que na prática não há diferença:

    if (numero_secreto == chute):
        print("Você acertou!")
    else:
        if (chute > numero_secreto):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (chute < numero_secreto):
            print("Você errou! O seu chute foi menor que o número secreto.")

### Código + limpo (boas práticas)

Usando variáveis (valores testados) ao invés de usar nas variáveis.

    acertou = chute == num_secreto 
    maior = chute > num_secreto 
    menor = chute < num_secreto

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

### Usando elif com operadores de comparação

*Operadores*

Saiba, que além do == (igualdade), > (maior) e < (menor), 
também temos >= (maior ou igual), <= (menor ou igual) e != (diferente)

    idade_str = input("Digite sua idade: ")
    idade = int(idade_str)

    if (idade >= 18):
        print("Você é maior de idade.")
    else:
        if (idade <= 12):
            print("Você é uma criança.")
        elif (idade >= 13):
            print("Você é um adolescente.")

### Variável do tipo boleana 

A variável acertou é do tipo bool.
Uma variável do tipo bool pode ter apenas dois valores, True ou False, que podemos usar diretamente:

    passou = True
    errou = False

*Exemplo prático:*

    acertou = chute == num_secreto 
    print("O tipo da variável -acertou- é : ", type(acertou))

## 04. A sequência do jogo

### Usando laços de repetição 

Quando queremos escrever o nosso código apenas uma vez, e repeti-lo, faremos um laço, ou um loop. 

*Exemplo while*

    total_de_tentativas = 3
    rodada = 1

    while (total_de_tentativas > 0):
        print("Tentativa", rodada, "de", total_de_tentativas)
        chute_str = input("Digite o seu número: ")

    --- restante do código comentado

Ambos, if e while, possuem uma condição de entrada. A diferença é que o if executa o bloco apenas uma vez, mas o while repete o bloco enquanto a condição for verdadeira.
O interessante é que o Python não possui um laço com uma condição de saída, que outras linguagens chamam de do-while.

### Formatação de strings

Usamos {} para substituir por variáveis. 

*Exemplo:*

    print("Rodada {} de {} : " .format(rodada, total_tentativas))

## 05. Iterando de maneira diferente

### O laço com FOR (outro tipo de loop)

Executa as ações até que uma condição dentro de um escopo definido pela função range() seja atingida

A função range possui os seguintes parâmetros:
range(start, stop, step)

*Exemplos:*

    for rodada in range(1,10):
        print(rodada)

No exemplo, acima o escopo (range) é 1 até 10, sendo que o último número não conta, então ele imprime a variável rodada de 1 até 9. 

    for rodada in range(1,100,10):

No exemplo, acima o escopo (range) é 1 até 100, variando de 10 em 10, então ele imprime a variável rodada de 1 até 91, fazendo incrementos de 10 em 10. 

### Encerrando a iteração e o loop

Para realizar o controle de fluxo (control flow), usamos algumas palavras-chave. 

A palavra-chave break, faz com que saiamos do laço. 

    if (acertou):
        print("Você acertou!")
        break

Quando há uma condição que é atendida mas não queremos sair do laço, usamos outra palavra-chave: continue

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

### Mais sobre formatação de strings

https://docs.python.org/3/library/string.html#formatexamples

*Formatando strings*

    print("Tentativa {} de {}".format(3,10))
Tentativa 3 de 10
    print("Tentativa {1} de {0}".format(3,10))
Tentativa 10 de 3 (neste caso ele inverte os valores a serem substituídos, colocando a posição zero no segundo parâmetro e a posição um no primeiro parâmetro)

*Interpolando números floats*

    print("R$ {:f}".format(1.59))
    R$ 1.590000
    print("R$ {:7.2f}".format(1.59)) # remove os zeros (considerando 7 caracteres) e apresenta apenas duas casas decimais depis do ponto
    R$    1.59
    print("R$ {:07.2f}".format(1.59)) # inlui os zeros nos espaços vazios (considerando 7 caracteres) e apresenta apenas duas casas decimais depis do ponto
    R$ 0001.59
    print("R$ {:07.2f}".format(1548.59))
    R$ 1548.59
    
*Formatando números inteiros*

    print("Data {:02d}/{:02d}".format(5,9))
    Data 05/09

### Interpolação - Python 2 vs Python 3

Python 3 

    "{} {}".format(1, 2)

Python 2

    "%d %d" % (1, 2)

Mais exemplos comparando o Python 2 com Python 3: https://pyformat.info/

No Python 3.6+, existe um novo recurso para realizar a interpolação de strings. 
Esse recurso é chamado de f-strings ou formatted string literals.

    nome = 'Matheus'
    print(f'Meu nome é {nome}')
    Meu nome é Matheus

Com a letra f antes das aspas, é uma f-string. 
Em tempo de execução, captar a expressão que está entre chaves ({ }) e avaliá-la.
Além de variáveis, podemos passar também de funções e métodos:

    nome = 'Matheus'
    print(f'Meu nome é {nome.lower()}')
    Meu nome é matheus

## 06. Gerando números aleatórios

*Funções built-in* - https://docs.python.org/3.10/library/functions.html

    print(), input(), help(), range(), format(),round() etc. 

*Módulos (bibliotecas) Python para funções*

***Módulo random*** - https://docs.python.org/3/library/random.html#module-random

As funções que não são built-in no Python, devem ser carregadas para funcionar através de módulos.
O módulo random traz várias funções para a finalidade de gerar números aleatórios. 

    import random

    aleatorio = random.random() # cria um número (float) aleatório entre 0 e 1
    aleatorio = round(random.random() * 100) # cria um número (float) aleatório entre zero e cem, depois arredonda.
    aleatorio = random.randrange(1, 101) # cria um numero aleatorio entre 1 e 100, sem necessidade de arredondar ou remover decimais. 
    aleatorio=random.randrange(10) # cria um número aleatorio entre 0 e 9.

Os aleatórios gerados são na verdade  Pseudo-Random!
Por padrão o Python usa a hora (os milissegundos) como semente (seed), 
mas nada nos impede de definir o mesmo seed antecipadamente. Para isso, existe a função seed!

    aleatorio=random.seed(100)
    aleatorio=random.randrange(1,101)
    print(aleatorio)
    19  # usando seed 100 o resultado sempre sera 19.

## 07. Nível e Pontuação

### Atribuindo valores dinâmicos a variáveis

    import random

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # resto do código comentado

### Usando mais um função built-in

*Função abs*

    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos

*Função round*

O Python 3 usa Banker's rounding. Nessa forma, os valores são arredondados para o número que for mais próximo, por exemplo: 2.4 seria arredondado para 2, todavia 2.6 já seria arredondado para 3. Quando um valor é igualmente próximo de dois números, por exemplo 2.5, que possui 0.5 de diferença tanto para o número 2 quanto para o número 3, esse é arredondado para o valor par mais próximo, que, nesse caso, seria o número 2. 
Vale lembrar que somente os números x.5 recebem o tratamento "especial" do arredondamento para o valor par mais próximo, nos demais, o arredondamento ocorre conforme esperado.

Mais informações se encontram na documentação do Python 3: https://docs.python.org/3.5/library/functions.html#round

### Divisão de float e interger

O operador / sempre traz um float, mesmo se não for necessário, por isso ele também é chamado de float division:

    divisao = 3 / 2
    print(divisao)
    1.5
    type(divisao)
    <class 'float'>

O operador // também é chamado integer division e sempre devolve o valor inteiro (sem arredondar).

    divisao = 3 // 2
    print(divisao)
    1
    type(divisao)
    <class 'int'>

### Melhorando a organização do código

## Importando arquivos dentro de outros



