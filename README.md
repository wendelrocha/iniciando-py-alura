Alura, Nico Steppat
Python: começando com a linguagem Python: começando com a linguagem

Instalar python3

    Existe para Windows, Mac e Linux
    Pode usar sem na plataforma https://replit.com/languages/python3

Funções e Variáveis 

    Uma função sempre terá um parenteses depois de seu nome
    
    Exemplos

    função print(paramentros)
    função help(parametros)

>>> help(print)

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