while True:
    num1 = int(input("Digite o numero que deseja saber a tabuada: "))
    for i in range(1,11):
        resultado = num1 * i
        print(f"{num1} x {i} = {resultado}")