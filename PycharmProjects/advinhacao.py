print("************************************")
print("* Bem vindo ao jogo de Adivinhação *")
print("************************************")

print("###### PENSE EM NÚMERO DE ZERO A 100")

num_secreto = 42
chute_str = input("Digite o seu palpite: ")
chute = int(chute_str)
acertou = chute == num_secreto 
maior = chute > num_secreto 
menor = chute < num_secreto
print("O tipo da variável -acertou- é : ", type(acertou))
type(acertou)

print("Você digitou ", chute_str)
print("")

if(acertou):
    print("Você acertou")
    print("")
    print("Meus Parabéns!!")
    print("")
else:
    if (maior):
        print("Errou! Seu palpite foi mais alto do que num secreto")
    elif (menor):
        print("Errou! Seu palpite foi mais baixo do que num secreto")
    print("")

print("Game Over!!!")