letra=str(input("Digite seu sexo M para masculino F para feminino: "))
nota2=float(input("Digite sua altura: "))
if letra=='M' or letra=='m':
    peso=(72.5*nota2)-58
    print("Esse é seu peso ideal: ",peso)
elif letra=='F' or letra=='f':  
    peso2=(62.1*nota2)-47.7
    print("Esse é seu peso ideal: ",peso2)
else:
    print("Sexo invalido")