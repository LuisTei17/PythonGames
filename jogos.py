import forca
import advinhacao

print("*************************")
print("****Escolha seu jogo*****")
print("*************************")

print("(1) Forca (2) Advinhação")
jogo = int(input("Qual jogo?"))

if(jogo == 1):
    forca.jogar()
if(jogo == 2):
    advinhacao.jogar()