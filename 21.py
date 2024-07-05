nota=float(input('Digite o valor da primeira prova: '))
nota2=float(input('Digite o valor da segunda prova: '))
nota3=float(input('Digite o valor da terceira prova: '))
media=((nota*2)+(nota2*3)+(nota3*5))/10
if media==0 or media<=2.9:
    print("Reprovado")
elif media>=3 and media<=5.9:
    print("Recuperação")
else:
    print("Aprovado")