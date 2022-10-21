import forca
import adivinha

print("*********************************")
print("Menu de Jogos!")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Informe qual quer jogar: "))

if(jogo == 1):
    print("Abrindo jogo da Forca...")
elif(jogo == 2):
    print("Abrindo jogo de Adivinhação...")