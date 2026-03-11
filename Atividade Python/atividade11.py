# while continuar (continuar = True)
#if
#else
#elif
#for
continuar = True
while continuar:
    print("Digite um número: ")
    numero = int(input())
    if numero > 0:
        print("O número é positivo")
    elif numero < 0:
        print("O número é negativo")
    else:
        print("O número é zero")
    print("Deseja continuar? (s/n)")
    resposta = input()
    if resposta == "n":
        continuar = False
print("Programa encerrado")



