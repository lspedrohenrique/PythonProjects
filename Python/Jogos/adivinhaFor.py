print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1) :

    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #String interpolation

    chute = int(input("Digite o seu chute: "))

    acertou = chute == numero_secreto #true or false

    chute_alto = chute > numero_secreto #true or false

    chute_baixo = chute < numero_secreto #true or false

    if(acertou):
        print("Parabéns! Você acertou!")
    else:
        if(chute_alto):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(chute_baixo):
            print("Você errou! O seu chute foi menor do que o número secreto.")

print("****")
print("Fim!")
print("****")