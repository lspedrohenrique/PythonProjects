import random

def imprime_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra():
    arquivo = open("lista.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_em_letras_acertadas(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_vencedor():
    print("Parabéns, você ganhou!!")

def imprime_perdedor():
    print("Você perdeu!!")

def jogar():

    imprime_abertura()

    palavra_secreta = carrega_palavra()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    erros = 0

    while(True):

        chute = pede_chute() #A função pede_chute retorna a entrada(chute) do usuário.

        if(chute in palavra_secreta):
           marca_chute_em_letras_acertadas(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        if (erros == 6):
            break
        if ("_" not in letras_acertadas):
            break
        print(letras_acertadas)

    if("_" not in letras_acertadas):
        imprime_vencedor()
    else:
        imprime_perdedor()

if(__name__ == "__main__"):
    jogar()