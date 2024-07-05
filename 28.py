num=float(input("Digite um numero: "))
num2=float(input("Digite outro numero: "))
print("1- Soma de 2 números.")
print("2- Diferença entre 2 números.")
print("3- Produto entre 2 números.")
print("4- Divisão entre 2 números (o denominador não pode ser zero).")
formula=str(input("Digite a formula 1,2,3 ou 4 :"))
if formula=='3':
    soma=num*num2
    print("Esse e o resultado da multiplicação: ",soma)
elif formula=='4':
    soma=num/num2
    print("Esse e o resultado da divisão: ",soma)
elif formula=='+':
    soma=num+num2
    print("Esse e o valor da soma: ",soma)
elif formula=='2':
    soma=num-num2
    print("Esse e o resultado da subtração: ",soma)
else:
    print("Equação invalida")