x = 1
cont = 0
soma = 0
media = 0

while x != 0:
    x = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + x

media = soma/(cont - 1)

print('Foram {} números digitados' .format(cont - 1))
print('A soma dos números foi: {}' .format(soma))
print('A média dos nuḿeros é: {}' .format(media))