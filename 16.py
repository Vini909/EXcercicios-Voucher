horas=float(input("Informe as horas trabalhadas: "))
num=horas*40.5
if num>=2500:
    num2=num*11/100
    print("Esse e o valor do seu salario com imposto de 11%: ",num2)
else:
    print("Esse e o seu salario total sem imposto: ",num)