import forca
import adivinhacao

print("************************************")
print("*        Escolha seu jogo          *")
print("************************************")
print("")

print("Aperte (1) para jogar Forca")
print("Aperte (2) para jogar Adivinhação")

jogo = int(input("Qual jogo? "))

if(jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando Adivinhação")
    adivinhacao.jogar()
elif(jogo != 1 or jogo != 2):
    print("Jogo inválido")
    print("Comece de novo")




