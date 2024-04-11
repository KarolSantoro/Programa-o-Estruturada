preco = float(input("Digite o preço:"))
desconto = float(input("Digite o quantidade de desconto:"))
total = preco - (preco * desconto / 100)
print ("O valor é de R$" , format (total))