print("* Bem vindo ao ambiente de testes *")
print("")

## ENCONTRAR ERROS E OPÇÕES PARA SUAS SOLUÇÕES NOS CÓDIGOS ABAIXO

# Comparando variáveis int 

"""minha_idade = 24
idade_namorado = 25

if(minha_idade == idade_namorado)
    print('temos idades iguais')
else:
    print('temos idades diferentes')"""

# Comparação de variáveis estranha

"""numero1 = 10
numero2 = 10
if(numero1 = numero2):
    print("São números iguais")"""

# Somar string com int
"""idade1 = 10
idade2 = "20"
print(idade1 + idade2)

idade1 = 10
idade2 = int("20")
print(idade1 + idade2)"""

# Concatenando strings

"""nome = "Nico"
sobrenome = "Steppat"
#print(nome,sobrenome)
print(nome,sobrenome, sep="_")
#print(nome + " " + sobrenome)"""

## Usando o elif c/ lógica errada

##idade_str = input("Digite sua idade: ")
##idade = int(idade_str)

##if (idade > 18):
##    print("Você é maior de idade.")
##else:
##    if (idade < 12):
##        print("Você é uma criança.")
##    elif (idade > 12):
##        print("Você é um adolescente.")"""

## Usando o elif corretamente c/ operadores de comparação

"""idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade >= 18):
    print("Você é maior de idade.")
else:
    if (idade <= 12):
        print("Você é uma criança.")
    elif (idade >= 13):
        print("Você é um adolescente.")"""

## Corrigir o código

##usuario = input("Informe o usuário do sistema!")

##if(usuario == "Flávio"):
##    print("Seja bem-vindo Flávio!")
##else(usuario == "Douglas"):
##    print("Seja bem-vindo Douglas!")
##else(usuario == "Nico"):
##    print("Seja bem-vindo Nico")
##else:
##    print("Usuário não identificado!")

## código correto

"""usuario = input("Informe o usuário do sistema: ")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif (usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")"""

## Testando formatações

"""Em 2017 o Carnaval acontece em fevereiro do dia 24 até o dia 28"

dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017

#print("Em" ano, "o carnaval acontece em", mes, "do dia", dia_ini, "até o dia", dia_fim)
print("Em {} o carnaval acontece em {} do dia {} até o dia {}.".format(ano,mes,dia_ini,dia_fim))"""

# Usando laços com for 

"""contador = 1 
for contador in range(1,11,3):
    print(contador)"""

# Trocando a posição de strings

print("Tentativa {1} de {0}".format("Cordeiro","Leonardo"))