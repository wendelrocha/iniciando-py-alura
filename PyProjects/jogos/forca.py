import random

def jogar():
    print("************************************")
    print("*    Bem vindo ao jogo da Forca    *")
    print("************************************")
    print("")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
   
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    print ("")
    
    # Enquanto não enforcou é verdadeiro (not enforcou) e não acertou (not acertoou) é verdadeiro faça
    while(not enforcou and not acertou):
        
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    print("")
                    letras_acertadas[index] = letra
                    print ("Encontrei a letra {} na posição {}".format(letra,index))
                index += 1
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        
        print("")
        print("Continue jogando.. ")
        print("")
    
    if(acertou):
        print("Você ganhou!!!")    
        print("")
    else:
        print("Você perdeu")
        print("")
        print("A palavra secreta é:",palavra_secreta)
    
    print("Game Over!!!")

if(__name__ == "__main__"):
    jogar()