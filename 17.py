numero = int(input('Informe um número: '))

if numero >= 1:
        print('2')
        x = 1
        y = 3
        while x < numero:
            z = 3
            while(z < y):
                if y % z == 0:
                    break
                z = z + 2
            if z == y:
                print(z)
                x = x + 1
            y = y + 2