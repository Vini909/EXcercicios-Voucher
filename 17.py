num=int(input("Digite o seu salario: "))
num2=int(input("Digite o valor da prestação: "))
num3=(num*20)/100
if num2>num3:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")