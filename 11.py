deposito = float(input('Depósito de inicio: '))
juros = float(input('Taxa de juros: '))
por_mes = float(input('Valor do depósito mensal: ')) 

mes = 1 
total = deposito
deposito_mes = 0

while mes <= 12:
    total = total + (total * (juros / 100)) + por_mes + deposito_mes
    print("Saldo do mês {} é de R${:.2f}".format(mes, total))
    deposito_mes = float(input('Novo mês, deseja depósitar algum valor? Se sim, quanto? '))

    mes = mes + 1

print('O ganho obtido com os juros foi de R${:.2f}.'.format(total))