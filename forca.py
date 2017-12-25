import random

def jogar():

    print("**************************")
    print("Bem vindo ao jogo da forca")
    print("**************************")
    
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())
    
    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou        = False
    acertou         = False
    erros           = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Qual a letra?")
        chute = chute.strip().upper()
        print("jogando")

        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
            print(letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
    if(acertou):
        print("Parabéns, você ganhou")
    else:    
        print("Fim do jogo, você perdeu")

if(__name__ == "__main__"):
    jogar()