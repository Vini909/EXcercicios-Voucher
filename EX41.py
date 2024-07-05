valor=float(input("Digite o valor da venda: "))

porc= valor*10/100
pagvista= valor-porc
parcela= valor/3
avista=pagvista*0.05
prazo= valor*0.05

print(f"Compra com desconto {pagvista}")
print(f"parcelas: {parcela:.2f}")
print(f"\n comissaa vista: {avista}")
print(f"comissao a prazo: {prazo}")