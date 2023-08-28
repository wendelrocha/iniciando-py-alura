Alura, Nico Steppat
Python: começando com a linguagem Python

01. Instalação do Python3

Instalar python3

Existe para Windows, Mac e Linux
Pode usar sem instalar (testes básicos) na plataforma https://replit.com/languages/python3

Funções e Variáveis 

Funções 

Uma função sempre terá um parenteses depois de seu nome
    
Exemplos

    função print(paramentros)
    função help(parametros)

>>>> help(print)

>>> print("Brasil ganhou 5 copas do mundo")  
Brasil ganhou 5 copas do mundo

>>> print("Brasil", "ganhou", 5, "copas do mundo", sep="-") 
Brasil-ganhou-5-copas do mundo

>>> print("Brasil", "ganhou", 5, "copas", "do", "mundo", sep="-") 
Brasil-ganhou-5-copas-do-mundo

>> pais="italia"
>>> ntitulos=4

>>> type(pais)
<class 'str'>

>>> type(ntitulos)
<class 'int'>

Lembrando que o \n é um caractere especial, que faz com que o novo prompt comece em uma nova linha.

>>> print(pais, "ganhou", ntitulos, "copas", "do", "mundo",sep=" ",end="!\n") 
italia ganhou 4 copas do mundo!

Outro exemplo usando variáveis

>>> dia = 15
>>> mes = 10
>>> ano = 2015

>>> print(dia,mes,ano,sep="/")
15/10/2015

Tipagem do Python

Uma variável só passa a existir quando atribuímos um valor.
Mesmo se declaramos o tipo e o nome da variável, sem ter atribuído o valor.
Em Python, a variável só passa a existir quando atribuímos um valor, como no exemplo abaixo:

int idade;

    declarou apenas o nome e a tipagem da variável

idade = 12

    Após atribuir valor, a variável passa a existir

Exemplos: 

>>> mes="ago"

>>> type(mes)
<class 'str'>

>>> mes=8

>>> type(mes)
<class 'int'>

>>> mes=8.9

>>> type(mes)
<class 'float'>

Snake_Case

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

02. Lidando com a entrada do usuário