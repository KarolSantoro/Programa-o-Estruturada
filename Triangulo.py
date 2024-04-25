area = float(input("Digite a área do triângulo:"))
base = float(input("Digite a base do triângulo:"))
altura = float(input("Digite a altura do triângulo:"))
if (area < base + altura) and (base < area + altura) and (altura < area + base):
    print ("Sim é possível formar um triângulo!")
    if (area == base) and (altura == area):
        print ("Seu triângulo é um EQUILATERO!")
    elif area != base != altura != area:
        print ("Seu triângulo é um ESCALENO!")
    else:
       print("Seu triângulo é um IÓSCELES!" )
else:
    print ("Infelimente não é possível formar um triângulo com os dados informados!")