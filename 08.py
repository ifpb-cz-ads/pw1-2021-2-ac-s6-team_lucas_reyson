dividendo = int(input('Dividendo: '))
divisor = int(input('Divisor: '))

y = 0
resto = 0
x = dividendo

while x >= divisor:
    x = x - divisor 
    y = y + 1

resto = x

print('{}/{} = {} rest0 {}'.format(dividendo, divisor, y, resto))