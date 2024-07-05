num=int(input("Digite quantas avalições você tem: "))
provas=[]
for nota in range(1,num+1):
    provas.append(float(input("Digite a nota: ")))

    media = sum(provas)/num
    print(media)