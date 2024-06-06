#pedir nº inprimir até o usuario digitar 0, depois somar todos.
soma = 0
while True:
    num  = int(input("digite um número:"))
    if num ==0:
        break
    soma = soma + num
print("total é" , soma)
