peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
IMC = peso/(altura * altura) 
print(" Resultado do seu IMC é:", IMC)
if IMC <18.5:
    print ("Baixo peso")
elif IMC >= 18.5 and IMC <= 24.9:
    print ("Peso normal")
elif IMC >= 25 and IMC <= 29.9:
    print ("Excesso de peso")
elif IMC >= 30 and IMC <= 34.9:
    print ("Obesidade Grau I")
elif IMC >=35 and IMC <= 39.9:
    print ("Obesidade Grau II")
elif IMC >= 40:
    print ("Obesidade Mórbida")
 




     
    






