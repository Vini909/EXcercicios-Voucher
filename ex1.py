num=int(input("Digite um numero que farei a tabuada dele até o 10: "))
cont=1

print("tabuada de {}".format(num))

while(cont<=10):
    print(f"{num} X {cont} = {num*cont}")
    cont= cont +1