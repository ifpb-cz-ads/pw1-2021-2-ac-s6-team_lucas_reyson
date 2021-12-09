deposito = float(input('Depósito de inicio: '))
juros = float(input('Taxa de juros: '))
por_mes = float(input('Valor do depósito mensal: ')) 

mes = 1 
total = deposito

while mes <= 12:
    total = total + (total * (juros / 100)) + por_mes
    print("Saldo do mês {} é de R${:.2f}".format(mes, total))
    mes = mes + 1

print('O ganho obtido com os juros foi de R${:.2f}.'.format(total))