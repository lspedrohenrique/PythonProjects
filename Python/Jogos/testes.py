print("Bem vindo ao nosso sistema!!")

anos = int(input("Informe sua idade: "))

meses = int(input("Informe quantos meses passou do seu aniversário: "))

anos_not = anos < 0 or anos > 100

meses_not = meses < 0 or meses > 11

while(anos_not or meses_not):
    print("Idade ou mês invalido, por favor informe valores validos para prosseguir")

    anos = int(input("Informe sua idade: "))

    meses = int(input("Informe quantos meses passou do seu aniversário: "))

    anos_not = anos < 0 or anos > 100

    meses_not = meses < 0 or meses > 11
    
print("Você tem {:02d} anos e {:02d} meses.".format(anos,meses))

if(anos < 18):
    print("Você é menor de idade!")
else:
    print("você é maior de idade!")