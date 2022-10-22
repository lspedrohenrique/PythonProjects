import random #importar biblioteca com funções de números aleatórios

def adivinha():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101) #Primeiro randow para importar a biblioteca e depois o nome da função que está nessa biblioteca.

    total_de_tentativas = 0

    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 10

    elif(nivel == 2):
        total_de_tentativas = 6

    else:
        total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1) : #Para rodada de 1 ate total de tentativas + 1 faça

        print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #String interpolation

        chute = int(input("Digite o seu chute de 1 a 100: "))

        if(chute < 0 or chute > 100):
            print("Número fora da margem, digite um número entre 1 a 100")
            continue

        acertou = chute == numero_secreto #true or false

        chute_alto = chute > numero_secreto #true or false

        chute_baixo = chute < numero_secreto #true or false

        if(acertou):
            print("Parabéns! Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(chute_alto):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}, você fez {} pontos".format(numero_secreto, pontos))

            elif(chute_baixo):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))

            pontos_perdidos = abs(numero_secreto - chute) #Valor absoluto, sem sinal.
            pontos = pontos - pontos_perdidos

    print("****")
    print("Fim!")
    print("****")

if(__name__ == "__main__"):
    adivinha()