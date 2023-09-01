import random

def jogar():
    print("************************************")
    print("* Bem vindo ao jogo de Adivinhação *")
    print("************************************")
    print("")

    num_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000
    #rodada = 1 # usando o loop for, não é necessário atribuir valor a essa variavel

    print("Escolha um nível de difuldade.")
    print("Digite (1) para Fácil - (2) para Médio - (3) para Dificil")
    print("")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    print("###### PENSE EM NÚMERO DE 1 A 100")

    print(num_secreto)

    #Substituindo while por for
    #while(rodada <= total_tentativas):
    for rodada in range(1,total_tentativas + 1):
        print("Rodada {} de {} : " .format(rodada, total_tentativas))
        print("")

        chute_str = input("Digite um palpite entre 1 e 100: ")
        chute = int(chute_str)

        if(chute < 1 or chute >100):
            print("Você digitou ", chute_str)
            print("")
            print("Numero incorreto, digite entre 1 e 100")
            print("")
            continue
        
        acertou = chute == num_secreto 
        maior = chute > num_secreto 
        menor = chute < num_secreto
    
        if(acertou):
            print("")
            print("Meus Parabéns!!")
            print("")
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("")
                print("Errou! Seu palpite foi maior do que num secreto")            
            elif (menor):
                print("")
                print("Errou! Seu palpite foi menor do que num secreto")            
            pontos_perdidos = abs(num_secreto - chute)
            pontos = pontos - pontos_perdidos
            print("")
            
        #rodada = rodada + 1 # não é necessário incrementar essa variável, pois esta usando o loop for.
    print("")

#if(rodada == total_tentativas):

    print("O número secreto era: {}. Você fez {} pontos".format(num_secreto,pontos))
print("Game Over!!!")

if(__name__ == "__main__"):
    jogar()