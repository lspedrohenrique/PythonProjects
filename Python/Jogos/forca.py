
def forca():

    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False #Enforcou? Não

    acertou = False #Acertou? Não

    while(not enforcou and not acertou): #While só executa o bloco caso seja verdadeiro, sendo falso o python pula para o próximo comando

        chute = input("Qual letra?: ")
        chute = chute.strip() #A função .strip corrige qualquer entrada errada com espaços a mais

        posicao = 1

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): #A Função .upper() transforma toda a string aplicada em caracteres maiúsculos 
                print("Encontrei a letra {} na posição {}".format(chute, posicao))
            posicao = posicao + 1

        print("Jogando...")

    print("****")
    print("Fim!")
    print("****")

if(__name__ == "__main__"):
    forca()