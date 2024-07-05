lado1=int(input("Digite um valor: "))
lado2=int(input("Digite outro valor: "))
lado3=int(input("Digite outro valor: "))
soma=lado1+lado2
if soma>lado3:
    print("É um triangulo")
    if lado1==lado2==lado3:
        print("É um triangulo equilatero")
    elif lado1==lado2!=lado3:
        print("É um triangulo isoceles")
    elif lado1!=lado2!=lado3:
        print("É um trinagulo escaleno")
if soma<=lado3:
    print("Não é um triangulo")