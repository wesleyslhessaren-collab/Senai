estoque = {}
print ("bem vindo ao sistema de gestão de estoque desenvolvido por wesley cavali slhessarenko")
while True:
    operacao = input ("deseja registrar a entrada e saída de produtos? (digite 'entrada' ou 'saída') ou 'sair'").lower() 

    
    if operacao not in ['entrada', 'saída', 'sair']:
        print("operação inválida.")
        continue

    if operacao == 'sair':
        break # quebra a ação de repetição
    produto = input("Digite o nome do produto: ").strip() # tem a função de limpar o bloco de código ()
    qtd = int(input("Digite a quantidade: "))

    if operacao == 'entrada':
        estoque[produto] = estoque.get(produto, 0) + qtd
    elif operacao == 'saída':
        if estoque.get(produto, 0) >= qtd:
            estoque[produto] -= qtd
        else:
            print("Erro:produto inexistente ou estoque insuficiente.")


print("\n ---Estoque Final ---")
for p, q in estoque.items():
    print(f"{p}: {q} unidades") 