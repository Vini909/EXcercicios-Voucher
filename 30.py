num=float(input("Digite o valor do produto: "))
estado=str(input("Digite o estado MG,SP,RJ ou MS :"))
if estado=='mg' or estado=='MG':
    soma=(num*7)/100
    soma2=num+soma
    print("Esse e o valor com imposto: ",soma2)
elif estado=='SP' or estado=='sp' :
    soma=(num*12)/100
    soma2=num+soma
    print("Esse e o valor com imposto: ",soma2)
elif estado=='RJ' or estado=='rj':
    soma=(num*15)/100
    soma2=num+soma
    print("Esse e o valor com imposto: ",soma2)
elif estado=='MS' or estado== 'ms':
     soma=(num*8)/100
     soma2=num+soma
     print("Esse e o valor com imposto: ",soma2)