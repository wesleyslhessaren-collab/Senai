maior = float()
menor = float()
soma = 0
acima_100 = 0
for  cont in range(10):
    temperatura = float(input(f"Digite a {cont + 1} temperatura:"))
    soma += temperatura
    if cont == 0:
        maior = temperatura
        menor = temperatura 

    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura
    if temperatura > 100:
        acima_100 += 1
media = soma/10

print(f"A maior temperatura foi {maior} ")    
print(f"A  menor temperatura foi {menor} ")    
print(f"A média das temperaturas foi {media} ")
print(f"A temperatura ultrapassou 100°C {acima_100} vezes")    



    
