num = 1

print ('1. Adicao')
print ('2. Subtracao')
print ('3. Divisao')
print ('4. Multiplicacao')
print ('5. Sair')
opcao = input('Opcao: ')

while opcao != '5' :
    tabuada = int( input ('Numero: '))
    
    while num <= 10 :
        if opcao == '1' :
           result = tabuada + num
           print ('{0:2d} + {1:2d} = {2:2d}'.format(tabuada, num, result))
        elif opcao == '2':
           result = tabuada - num
           print ('{0:2d} - {1:2d} = {2:92}'.format(tabuada, num ,result))
        elif opcao == '3':
           result = tabuada * num
           print ('{0:2d} * {1:2d} = {2:2d}'.format(tabuada, num, result))
        elif opcao == '4':
           result = tabuada / num
           print ('{0:2d} / {1:2d} = {2:.2f}'.format(tabuada, num, result))
        num = num + 1

    print ('1. Adicao')
    print ('2. Subtracao')
    print ('3. Multiplicacao')
    print ('4. Divisao')
    print ('5. Sair')
    opcao = input('Opcao: ')