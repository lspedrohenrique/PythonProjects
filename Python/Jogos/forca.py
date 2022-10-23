
def forca():

    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False #Enforcou? Não

    acertou = False #Acertou? Não

    while(not enforcou and not acertou): #While só executa o bloco caso seja verdadeiro, sendo falso o python pula para o próximo comando

        chute = input("Qual letra?: ")

        posicao = 1
        
        for letra in palavra_secreta:
            if (chute == letra):
                print("Encontrei a letra {} na posição {}".format(chute, posicao))
            posicao = posicao + 1

        print("Jogando...")

    print("****")
    print("Fim!")
    print("****")

if(__name__ == "__main__"):
    forca()