import re

cep = "86181-230"

string = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
match = string.match(cep)

if match:
    print("Deu match paeee")
else:
    print("Deu ruim")