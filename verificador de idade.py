idade = int (input("Digite sua idade:"))
if idade <= 13:
    print ("Você é criança!")
elif idade > 13 and idade <= 17:
    print ("Você é adolescente!")
elif idade >= 18 and idade <= 59:
    print ("Você é adulto!")
else:
    print ("Você é idoso!")

