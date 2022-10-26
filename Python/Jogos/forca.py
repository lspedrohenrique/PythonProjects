
def forca():

    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    letras_secretas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False #Enforcou? Não

    acertou = False #Acertou? Não

    print(letras_secretas)

    while(not enforcou and not acertou): #While só executa o bloco caso seja verdadeiro, sendo falso o python pula para o próximo comando

        chute = input("Qual letra?: ")
        chute = chute.strip() #A função .strip() corrige qualquer entrada errada com espaços a mais

        indice = 0

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): #A Função .upper() transforma toda a string aplicada em caracteres maiúsculos 
                letras_secretas[indice] = letra.upper() #Atribuindo a letra na posição do índice 
            indice = indice + 1

        print(letras_secretas)

    print("****")
    print("Fim!")
    print("****")

if(__name__ == "__main__"):
    forca()