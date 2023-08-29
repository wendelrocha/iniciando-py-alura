print("************************************")
print("* Bem vindo ao jogo de Adivinhação *")
print("************************************")

num_secreto = 42
chute_str = input("Digite o seu palpite: ")
print("")

print("Você digitou ", chute_str)
print("")
chute = int(chute_str)

if(num_secreto == chute):
    print("Você acertou")
    print("")
    print("Meus Parabéns!!")
    print("")
else:
    print("Você errou.")
    print("")
print("Game Over!!!")