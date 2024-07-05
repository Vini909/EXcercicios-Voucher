num=float(input("Digite um numero: "))
num2=float(input("Digite outro numero: "))
formula=str(input("Digite a formuala +,-,/ ou X :"))
if formula=='x' or formula=='X':
    soma=num*num2
    print("Esse e o resultado da multiplicação: ",soma)
elif formula=='/':
    soma=num/num2
    print("Esse e o resultado da divisão: ",soma)
elif formula=='+':
    soma=num+num2
    print("Esse e o valor da soma: ",soma)
elif formula=='-':
    soma=num-num2
    print("Esse e o resultado da subtração: ",soma)