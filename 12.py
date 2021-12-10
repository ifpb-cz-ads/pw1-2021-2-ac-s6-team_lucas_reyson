divida = float(input('Vlor inicial da dívida: '))
juros_mes = float(input('Juros mensal: '))
pag = float(input('Valor mensal pagamento: '))

mes = 1
total = divida
j_pago = 0

while total > pag:
    juros = total * juros_mes/100
    total = total + juros - pag
    j_pago = j_pago + juros_mes
    print("Saldo do mês {} é de R${:.2f}.".format(mes, total))
    mes = mes + 1 

print('A quantidade de meses restantes para que a divida seja paga é de: {}, e a quantidade de juros vai ser de: {}'.format(mes-1, j_pago))
print('O total pago é de: {:.2f}'.format(total))

