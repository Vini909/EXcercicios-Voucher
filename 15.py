nota=float(input("Primeira nota: "))
nota2=float(input("Segunda nota: "))
media=(nota+nota2)/2
if media>=0 or media<=10:   
    print("media: ",media)
else:   
    print("valor invalido")