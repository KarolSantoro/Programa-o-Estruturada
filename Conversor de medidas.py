valor = float(input("Digite o valor que deseja converter:"))
mil = print("1. Milhas")
pol = print("2. Polegadas")
pes = print("3. Pés")
cm = print("4. Centímetros")
m = print("5. Metros")
km = print("6. Quilômetros")
conversor = input("Digite o tipo de conversor que deseja:")
if conversor == "1":
    print("O valor convertido em milhas é de:" , (valor)) 
    print("Em polegadas é de:" , (valor * 63360))
    print("Em pés é de:" , (valor * 5280))
    print("Em centímetros é de:" , (valor * 160900))
    print("Em metros é de:" , (valor * 1609))
    print("Em quilômetros é de:" , (valor * 1.609))
elif conversor == "2":
    print("O valor convertido em polegadas é de:" , (valor))
    print("Em milhas é de:" , (valor / 63360))
    print("Em pés é de:" , (valor / 12))
    print("Em centímetros é de:" , (valor * 2.54))
    print("Em metros é de:" , (valor / 39.37))
    print("Em quilômetros é de:" , (valor / 39370))
elif conversor == "3":
    print("O valor convertido em pés é de:" , (valor))
    print("Em milhas é de:" , (valor / 5280))
    print("Em polegadas é de:" , (valor * 12))
    print("Em centímetros é de:" , (valor * 30.48))
    print("Em metros é de:" , (valor / 3.281))
    print("Em quilômetros é de:" , (valor / 3281))
elif conversor == "4":
    print("O valor convertido em centímetros é de:" , (valor))
    print("Em milhas é de:" , (valor / 160900))
    print("Em polegadas é de:" , (valor / 2.54))
    print("Em pés é de:" , (valor / 30.48))
    print("Em metros é de:" , (valor / 100))
    print("Em quilômetros é de:" , (valor / 1000))
elif conversor == "5":
    print("O valor convertido em metros é de:" , (valor))
    print("Em milhas é de:" , (valor / 1609))
    print("Em polegadas é de:" , (valor * 39.37))
    print("Em pés é de:" , (valor * 3.281))
    print("Em centímetros é de:" , (valor * 100))
    print("Em quilômetros é de:" , (valor / 1000))
elif conversor == "6":
    print("O valor convertido em quilômetros é de:" , (valor))  
    print("Em milhas é de:" , valor / 1.609)
    print("Em polegadas é de:" , (valor * 39370))
    print("Em pés é de:" , (valor * 3281))
    print("Em centímetros é de:" , (valor * 10000))
    print("Em metros é de:" , (valor * 100))
else:
    print("ERRO! POR FAVOR DIGITE UMA UNIDADE DE ORIGEM VÁLIDA!")