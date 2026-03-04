medicoes = []

print("Digite 8 medições de corrente elétrica (em Amperes):")
for i in range(8):
    corrente = float(input(f"Digite a medição {i+1} de corrente (A): "))
    medicoes.append(corrente)


acima_15a = sum(1 for m in medicoes if m > 15)


sobrecarga = any(m > 20 for m in medicoes)


media_corrente = sum(medicoes) / len(medicoes)

alerta_200 = any(m > 200 for m in medicoes)


print(f"Medições acima de 15A: {acima_15a}")
print(f"Há sobrecarga (acima de 20A): {'SIM' if sobrecarga else 'NÃO'}")
print(f"Média da corrente: {media_corrente:.2f}A")

if alerta_200:
    print(" ALERTA: Uma ou mais medições ultrapassaram 200A!")
else:
    print("Todas as medições estão dentro dos limites de segurança.")
