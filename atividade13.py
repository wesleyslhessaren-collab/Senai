# cria a variavel nome 
nome = input("Digite seu nome: ")
#menu basico

print(f"Bem Vindo, {nome}")
#usado para verificar o tipo de usuário e o tempo de login para visitantes

while True:#cria um laço de repetição para o menu


    user = float(input("Qual tipo de usuário você é?\n1- Membro\n2- VIsitantes\n3- Saír\n\nQual opção você deseja?: "))
    #escolha do tipo de usuário

    if user == 2:
        time = float(input("Digite a quantidade de horas que você deseja ficar logado(a) (maximo 4): "))
        print()
        if time <= 4:
            print(f"Olá, {nome}, seu login foi feito com sucesso!")
            break
#Caso a hora for maior que 4 o sistema irá negar o acesso
        if time > 4:
            print("Acesso negado! Quantidade de horas inválida.\n")
            tentativa = input("Tentar novamente?\n1- Sim\n2- Não\n\nEscolha: ")
            if tentativa == 1:
                continue
            elif tentativa == 2:
                print("Saíndo...")
                break


#Caso o usuário seja um membro ele terá acesso ao sistema sem restrições de tempo
    if user == 1:
        print("Bem Vindo!, tempo de login: 9h da manha, até as 18h da tarde")
        break

#Caso o usuário escolha a opção de sair o sistema irá encerrar a execução
    if user == 3:
        print("Até a proxima!")
        break
