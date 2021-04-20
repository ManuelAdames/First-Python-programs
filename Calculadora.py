z = 1
while (str (z) != 'x' ):
    print ('Menu\n')
    print ('Opciones')
    print ('1. Suma')
    print ('2. Resta')
    print ('3. Multiplicacion')
    print ('4. Division')
    print ('x. Salir')
    opcion = input ("Elija una opcion: ")
    if (str (opcion) == '1'):
        n1 = input ('Introduzca un valor: ')
        n2 = input ('Introduzca otro valor: ')
        print ('Resultado: ' + str(int(n1) + int(n2))) 
    elif (str (opcion) == '2'):
         n1 = input ('Introduzca un valor: ')
         n2 = input ('Introduzca otro valor: ')
         print ('Resultado: ' + str(int(n1) - int(n2)))
    elif (str (opcion) == '3'):
         n1 = input ('Introduzca un valor: ')
         n2 = input ('Introduzca otro valor: ')
         print ('Resultado: ' + str(int(n1) * int(n2)))
    elif (str (opcion) == '4'):
         n1 = input ('Introduzca un valor: ')
         n2 = input ('Introduzca otro valor: ')
         print ('Resultado: ' + str(int(n1) / int(n2)))
    elif (str(opcion) == 'x'):
        print ('saliendo...')
    else:
        print('Opcion Invalida')
        


        
       
            
