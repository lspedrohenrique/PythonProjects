from datetime_exemplo import date

data_atual = date.today()
print(data_atual)

data_em_texto = data_atual.strftime("%d/%m/%y")
print(data_em_texto)

