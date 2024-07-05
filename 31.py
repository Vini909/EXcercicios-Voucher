num=float(input("Digite quantos Km seu carro faz a cada litro: "))
if num<=8:
    print("venda o carro!")
elif num>=8 and num<14:
    print("Econômico!")
elif num>14:
    print("Super econômico!")
