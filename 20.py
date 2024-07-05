nota=float(input('Digite o valor da primeira prova: '))
nota2=float(input('Digite o valor da segunda prova: '))
nota3=float(input('Digite o valor da terceira prova: '))
media=(nota*1+nota2*1+nota3*2)/4
if media>=60:
    print("Aprovado")
else:
    print("Reprovado")