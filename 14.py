pagar = 0
while True:
    codigo = int(input('Digite o código do produto: '))
    preço = 0
    if codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print('Código inválido!')
    if preco != 0:
        quant = int(input('Quantidade: '))
        pagar = pagar + (preco * quant)
        print('Total a pagar R${:.2f}'.format(pagar))