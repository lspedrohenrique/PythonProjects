print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute = int(input("Digite o seu número: "))

acertou = chute == numero_secreto #true or false

chute_alto = chute > numero_secreto #true or false

chute_baixo = chute < numero_secreto #true or false

print("Você digitou", chute)

if(acertou):
    print("Parabéns! Você acertou!")
else:
    if(chute_alto):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif(chute_baixo):
        print("Você errou! O seu chute foi menor do que o número secreto.")

print("Fim de Jogo.")
