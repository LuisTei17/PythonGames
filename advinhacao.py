import random
def jogar():

    print("********************************")
    print("BEM VINDO AO JOGO DA ADIVINHAÇÃO")
    print("********************************")

    numero_secreto = round(random.randrange(1,101))
    print(numero_secreto)
    total_de_tentativas = 0
    rodada              = 1

    nivel_str = input("Escolha o nível (1) Fácil, (2) Médio, (3) Difícil")
    nivel = int(nivel_str)

    if(nivel == 3):
        total_de_tentativas = 5
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 20

    pontos = 1000

    for rodada in range(1, total_de_tentativas+1):
        chute_str = input("Digite um número maior que 1 e menor que 100\n")

        chute = int(chute_str)
        
        if(chute > 100 | chute < 1 ):
            print("Você digitou um número menor que 1 ou maior que 100")
            continue

        igual = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        if(igual):
            print("Parabéns, você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Awn, você chutou muito alto")
            elif(menor):
                print("Awn, você chutou muito baixo")
            pontos_perdidos = abs(chute - numero_secreto)
            pontos = pontos - pontos_perdidos

if(__name__ == "__main__"):
    jogar()