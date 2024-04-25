num1 = int(input("Digite um número inteiro:"))
res = (num1)
if num1 > 0 and num1 % 2 ==0:
    print("O número digitado é POSITIVO e PAR!")
elif num1 > 0 and num1 % 3 ==0:
    print("O número digitado é POSITIVO e MÚLTIPLO DE 3!")
elif num1 < 0 and num1 % 2 ==0:
    print("O número digitado é NEGATIVO e ÍMPAR!")
elif num1 ==0:
    print("O número digitado é ZERO!")
else:
    print("O número digitado não é positivo,par,múltiplo de 3,negativo,ímpar ou zero!")