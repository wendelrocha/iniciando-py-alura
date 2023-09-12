def jogar():
    print("************************************")
    print("*    Bem vindo ao jogo da Forca    *")
    print("************************************")
    print("")

    palavra_secreta = "banana"
    letras_acertadas = ["-","-","-","-","-","-"]
    
    enforcou = False
    acertou = False

    print(letras_acertadas)
    print ("")
    
    #enquanto não enforcou é verdadeiro e não acertoou verdadeiro
    while(not enforcou and not acertou):
        
        chute = input("Qual letra? ")
        chute = chute.strip()
        
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("")
                letras_acertadas[index] = letra
                #print ("Encontrei a letra {} na posição {}".format(letra,index))                
            index = index + 1
        print(letras_acertadas)
        
        print("")
        print("Continue jogando.. ")
        print("")
        
    print("Game Over!!!")

if(__name__ == "__main__"):
    jogar()