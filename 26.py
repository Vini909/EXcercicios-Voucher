ano=int(input("Digite um ano que direi se ele e bisexto: "))
if (ano%4)==0 :
    print("É um ano bisexto")
elif (ano%400)==0 :
 print("É um ano bisexto")
elif (ano%100)==0 :
    print("É um ano bisexto")
else:
    print("Não é um ano bisexto")