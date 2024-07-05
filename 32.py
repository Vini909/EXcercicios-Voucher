num=float(input("Digite sua idade: "))
if num>=5 and num<=11:
    print("Infantil")
elif num==12:
    print("Infantil ou juvenil")
elif num>=13 and num<=17:
    print("Juvenil")
elif num>=18:
    print("Senior")
else:
    print("Não pode participar")