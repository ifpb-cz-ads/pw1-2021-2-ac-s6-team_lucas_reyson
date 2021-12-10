n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

cont = 1
result = 0
while cont <= n2:
    result = result + n1
    cont = cont + 1

print(result)