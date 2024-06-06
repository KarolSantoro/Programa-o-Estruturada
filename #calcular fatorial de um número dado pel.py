#calcular fatorial de um número dado pelo usuario.
num  = int(input("digite um número:"))
resultado = 1
for n in range (1,num+1):
    resultado *= n 
print ("o fatorial é:", resultado)