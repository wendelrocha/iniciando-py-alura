print("************************************")
print("* Bem vindo ao jogo de Adivinhação *")
print("************************************")

print("###### PENSE EM NÚMERO DE 1 A 100")

num_secreto = 42
total_tentativas = 3
rodada = 1 

#Substituindo while por for
#while(rodada <= total_tentativas):
for rodada in range(1,total_tentativas + 1):
    print("Rodada {} de {} : " .format(rodada, total_tentativas))

    chute_str = input("Digite o seu palpite entre 1 e 100: ")
    chute = int(chute_str)

    if(chute < 1 or chute >100):
        print("Você digitou ", chute_str)
        print("Numero incorreto")
        continue
    
    acertou = chute == num_secreto 
    maior = chute > num_secreto 
    menor = chute < num_secreto
 
    if(acertou):
        print("Você acertou")
        print("")
        print("Meus Parabéns!!")
        print("")
        break
    else:
        if (maior):
            print("Errou! Seu palpite foi mais alto do que num secreto")
        elif (menor):
            print("Errou! Seu palpite foi mais baixo do que num secreto")
        print("")
    rodada = rodada + 1
print("Game Over!!!")