print("************************************")
print("* Bem vindo ao jogo de Adivinhação *")
print("************************************")

print("###### PENSE EM NÚMERO DE ZERO A 100")

num_secreto = 42
total_tentativas = 3
rodada = 1 

while(rodada <= total_tentativas):
    print("Rodada {} de {} : " .format(rodada, total_tentativas))
    chute_str = input("Digite o seu palpite: ")
    chute = int(chute_str)
    acertou = chute == num_secreto 
    maior = chute > num_secreto 
    menor = chute < num_secreto

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
    rodada = rodada + 1
print("Game Over!!!")