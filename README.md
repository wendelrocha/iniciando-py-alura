Alura, Nico Steppat
Python: começando com a linguagem Python

## 01. Instalação do Python3

### Instalar python3

Existe para Windows, Mac e Linux
Pode usar sem instalar (testes básicos) na plataforma https://replit.com/languages/python3

### Funções e Variáveis

**Funções**

Uma função sempre terá um parenteses depois de seu nome
    
função print(paramentros)
função help(parametros)

Exemplos
    
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

Outro exemplo usando variáveis

    dia = 15
    mes = 10
    ano = 2015

    print(dia,mes,ano,sep="/")
    15/10/2015

-- Tipagem do Python

Uma variável só passa a existir quando atribuímos um valor.
Mesmo se declaramos o tipo e o nome da variável, sem ter atribuído o valor.
Em Python, a variável só passa a existir quando atribuímos um valor, como no exemplo abaixo:

    int idade;

Veja que foi declarado apenas o nome e a tipagem da variável

idade = 12

Após atribuir valor, a variável passa a existir

Exemplos:

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

-- Snake_Case

Padrão/convenção pra definição nomes de variáveis, usando o simbolo de underline (_) para separar as palavras

Exemplo

    idade_esposa = 20
    perfil_vip = 'Flávio Almeida'
    recibos_em_atraso = 30

Em outras linguagens usa-se o padrão CamelCase, que não é o padrão do Python, mas pode ser usado tbm no Python.
Neste caos, não se separam as palavras na variável. 

Exemplo:

    idadeEsposa = 20
    perfilVip = 'Flávio Almeida'
    recibosEmAtraso = 30

# Lidando com a entrada do usuário

Escolhendo a IDE (Integrated Development Environment) 

O PyCharm é uma IDE voltada exclusivamente para o Python. 
https://www.jetbrains.com/pycharm/ usar versão community

Outra opção bastante popular é o VS Code. 

Executar primeiro projeto: JOGO DA ADIVINHAÇÃO

-- Comparando variaveis 

Não se compara strings com inteiros. O sinal de igualdade é representado por ==
No Python não importa o número digitado, a comparação com == envolvendo tipos diferentes resultará em falso. Isso porque a função input sempre retorna um texto (string). 

-- Convertendo uma variável

Sendo assim, é necessário converter o valor retornado em inteiro, para que a comparação com outro inteiro, no caso o numero_secreto, seja possível. Realizamos essa conversão através da função int.

int(chute_str)

-- Estrutura do if e else

if(num_secreto == chute):
    print("Você acertou. ")
else:
    print("Você errou. ")

Também encontrado na forma sem parênteses, pois o Python aceita ambas as formas. 
Seguir a forma que usa parênteses, pois deixa mais claro qual é a condição, 
principalmente quando há várias condições a avaliar através das operações lógicas AND ou OR.

-- Somar string com int

idade1 = 10
idade2 = int("20")
print(idade1 + idade2)

-- Concatenando strings

nome = "Nico"
sobrenome = "Steppat"
print(nome,sobrenome)
print(nome,sobrenome, sep="_")
print(nome + " " + sobrenome)

-- Diferenças entre Python2 e Python3

** A função print

No Python 2, não precisamos colocar os parênteses na função print. Já no Python 3, os parênteses são obrigatórios. Ainda na função print, no Python 2 não há os parâmetros sep e end e quando há mais parâmetros a saída é diferente. 

** A função input

No Python 2, ela automaticamente converte o tipo da variável. Considerado má prática, porque se a intenção do desenvolvedor não for converter o tipo da variável. 
Por isso é bem comum encontrar a função raw_input sendo utilizada no Python 2: chute = raw_input("Digite o seu número: "); O retorno dessa função será sempre uma string, equivalente à função input do Python 3, mas ela não existe nessa versão.

Resumo

As funções input(...), print(...) e int(...) existem no Python 3.
A função raw_input(..) existe apenas no Python 2.

-- Diferenças entre JavaScript e Python

JavaScript, faz conversões de acordo com o que julga necessário 
num1 = 10
10
num2 = "20"
'20'
soma = num1 + num2
'1020'
multiplica = num1 * num2
200

Python, não faz as conversões, porém simplifica algo que seria trabalhoso, mas não muda a característica da linguagem. 
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

-- Diferenças entre Terminal do Python e Prompt de comando do Windows/Linux

Terminal do Python
O terminal interativo do Python é uma ferramenta que permite executar comandos Python diretamente no terminal. Quando você digita um comando nele e pressiona Enter, o Python executa o comando imediatamente e retorna o resultado. Isso é ótimo para testar rapidamente pequenos pedaços de código Python ou explorar as funcionalidades da linguagem. Mas, em contrapartida, o terminal interativo do Python não serve para executar arquivos.

Prompt de comando do Windows/Linux
Essa ferramenta é uma interface de linha de comando mais geral que permite executar comandos do sistema operacional e outras tarefas relacionadas ao sistema como carregar um arquivo, e para fazer isso você deve escrever “nome do diretório com o comando cd”, que é um atalho para mudar de diretório no cmd do windows e linux, localizar o arquivo que deseja e executá-lo.

-- Config. UTF-8 no VS Code

UTF-8 é um formato de codificação que permite que caracteres especiais e acentos sejam exibidos corretamente ao digitar no editor de códigos.

# Testando Valores

A condição elif

Em alguns casos casos, para forçar testar uma condução no senão (else), podemos fazer um else com uma condição de entrada, o elif. 
Vamos utilizá-lo para deixar o código mais semântico, já que na prática não há diferença:

if (numero_secreto == chute):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (chute < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")

-- Código + limpo (boas práticas)

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

-- Usando elif com operadores de comparação

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

-- Variável do tipo boleana 

A variável acertou é do tipo bool.
Uma variável do tipo bool pode ter apenas dois valores, True ou False, que podemos usar diretamente:

passou = True
errou = False

Exemplo prático: 
acertou = chute == num_secreto 
print("O tipo da variável -acertou- é : ", type(acertou))

## A sequência do jogo

-- Usando laços de repetição 

Quando queremos escrever o nosso código apenas uma vez, e repeti-lo, faremos um laço, ou um loop. 

Exemplo while 

total_de_tentativas = 3
rodada = 1

while (total_de_tentativas > 0):
    print("Tentativa", rodada, "de", total_de_tentativas)
    chute_str = input("Digite o seu número: ")

    --- restante do código comentado

Ambos, if e while, possuem uma condição de entrada. A diferença é que o if executa o bloco apenas uma vez, mas o while repete o bloco enquanto a condição for verdadeira.
O interessante é que o Python não possui um laço com uma condição de saída, que outras linguagens chamam de do-while.

-- Formatação de strings

