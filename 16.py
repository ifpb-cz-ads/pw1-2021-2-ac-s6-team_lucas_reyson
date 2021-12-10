numero = int(input("Informe um número: "))

if numero == 0 or numero == 1:
    print("{} não se enquadra em primos e não primos.".format(numero))
else:
    if numero == 2:
        print("2 é primo")
    elif numero % 2 == 0:
        print("{} não é primo, 2 é o único número par primo.".format(numero))
    else:
        x = 3
        while(x < numero):
            if numero % x == 0:
                break
            x = x + 2
        if x == numero:
            print("{} é primo".format(numero))
        else:
            print("{} não é primo, pois é divisível por {}".format(numero, x))