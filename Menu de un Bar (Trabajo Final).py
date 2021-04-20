kk = input ('Bienvenido al Adames Bar, porfavor introduzca su nombre: ')
z = 0
while (str (z) < '2' ):
    print ('')
    print ('Bienvenido/a '+ (kk) +' al Adames Bar\n')
    print ('Menu\n')
    print ('Agua')
    print ('Jugo')
    print ('Refresco')
    print ('Bebida Energetica')
    print ('Bebida Alcoholica\n')
    opcion = input ("Que desea ordenar? ")
    def eyklk ():
        global z
        if z == 1:
            global n2
            global hoho
            print ('')
            print ('      Su orden')
            print ('')
            print (hoho + '  ' + str(n2) + ' pesos')
            print (ohno + '  '+ str(n1) + ' pesos')
            print ('')
            print ('Por un total de ' + str(n1 + n2) + ' pesos')
            print ('Gracias espero que vuelvas al Adames Bar!')
            z = z + 1
        elif z == 0:    
            print ('Desea algo mas?')
            lol = input ('')
            if lol == 'no' or lol == 'No' or lol == 'NO':
                z = z + 2
                if 'n2' in globals():
                    print ('Gracias espero que vuelvas al Adames Bar!')                
                else:
                    print ('')
                    print ('        Su orden')
                    print ('')
                    print (ohno + '  ' + str(n1))
                    print ('')
                    print ('Por un total de ' + str(n1) + ' dolares')
                    print ('Gracias espero que vuelvas al Adames Bar!')
            if lol == 'si' or lol == 'Si' or lol == 'SI':
                        print ('')
                        z = z + 1
                        n2 = n1
                        hoho = ohno
    if (opcion) == 'agua' or  (opcion) == 'Agua' or (opcion) == 'AGUA':
        print ('Con gas   30 pesos')
        print ('Sin gas   20 pesos\n')
        i = input ('Que tipo de agua desea? ')
        if i == 'con gas' or i == 'con' or i == 'Con gas' or i == 'Con' or i == 'gas' or i == 'Gas' or i == 'GAS' or i == 'CON GAS' or i == 'CON':
            print ('Esa agua le costara 30 pesos')
            n1 = 30
            ohno = 'Agua con gas'
            eyklk()
        elif i == 'sin gas' or i == 'sin' or i == 'Sin gas' or i == 'Sin' or i == 'SIN' or i == 'SIN GAS' :
            n1 = 20
            ohno = 'Agua sin gas'
            print ('Esa agua le costara 20 pesos')
            eyklk()
        else:
            print ('Opcion no en el menu')
    elif (opcion) == 'jugo' or (opcion) == 'Jugo' or (opcion) == 'JUGO':
            print ('')
            print ('Nuestra seleccion de jugos:')
            print ('')
            print ('Jugo de Naranja  50 pesos')
            print ('Jugo de Manzana  50 pesos')
            print ('Jugo de Limon    50 pesos')
            print ('Jugo de Fresa    55 pesos')
            print ('Jugo de Uva      55 pesos')
            print ('Jugo de Chinola  55 pesos\n')
            x = input ("Que jugo desea? ")
            if x == 'de naranja' or x == 'jugo de naranja' or x == 'naranja' or x == 'NARANJA' or x == 'DE NARANJA' or x == 'JUGO DE NARANJA':
                n1 = 50
                ohno = 'Jugo de Naranja'
                print ('Ese jugo le costara 50 pesos')
                eyklk()
            elif x == 'de manzana' or x == 'jugo de manzana' or x == 'manzana' or x == 'MANZANA' or x == 'JUGO DE MANZANA' or x == 'DE MANZANA' :
                n1 = 50
                ohno = 'Jugo de Manzana'
                print ('Ese jugo le costara 50 pesos')
                eyklk()
            elif x == 'de limon' or x == 'jugo de limon' or x == 'limon' or x == 'JUGO DE LIMON' or x == 'LIMON' or x == 'DE LIMON' :
                n1 = 50
                ohno = 'Jugo de Limon'
                print ('Ese jugo le costara 50 pesos')
                eyklk()
            elif x == 'de fresa' or x == 'jugo de fresa' or x == 'fresa' or x == 'FRESA' or x == 'JUGO DE FRESA' or x == 'DE FRESA':
                n1 = 55
                ohno = 'Jugo de Fresa'
                print ('Ese jugo le costara 55 pesos')
                eyklk()        
            elif x == 'de uva' or x == 'jugo de uva' or x == 'uva' or x == 'UVA' or x == 'DE UVA' or x == 'JUGO DE UVA':
                n1 = 55
                ohno = 'Jugo de Uva'
                print ('Ese jugo le costara 55 pesos')
                eyklk()
            elif x == 'de chinola' or x == 'jugo de chinola' or x == 'chinola' or x == 'CHINOLA' or x == 'JUGO DE CHINOLA' or x == 'DE CHINOLA':
                n1 = 55
                ohno = 'Jugo de Chinola'
                print ('Ese jugo le costara 55 pesos')
                eyklk()
            else:
                print ('')
                print ('Opcion no en el menu')
    elif (opcion) == 'refresco' or (opcion) == 'Refresco' or (opcion) == 'REFRESCO':
            print ('')
            print ('Nuestra seleccion de refrescos:')
            print ('')
            print ('Coca-Cola  45 pesos')
            print ('7up        40 pesos\n')
            o = input ("Que refresco desea? ")
            if o == 'Cocacola' or o == 'COCACOLA' or o == 'COCA-COLA' or o == 'COCA COLA' or o == 'cocacola' or o == 'refresco cocacola' or o == 'Refresco cocacola' or o == 'Coca-cola' or o == 'Coca-Cola' or o == 'coca cola' or o == 'Coca Cola' or o == 'Coca cola':   
                n1 = 45
                ohno = 'Coca-Cola'
                print ('Ese refresco le costara 45 pesos')
                eyklk()
            elif o == '7up' or o == 'Refresco de 7up' or o == 'refresco de 7up' or o == 'refresco 7up' or o == 'Refresco 7up' or o == '7 up' or o == '7UP':
                n1 = 40
                ohno = '7up'
                print ('Ese refresco le costara 40 pesos')
                eyklk()
            else:
                print ('')
                print ('Opcion no en el menu')
    elif (opcion) == 'Bebida Energetica' or (opcion) == 'Bebida energetica' or (opcion) == 'energetica' or (opcion) == 'bebida energetica' or (opcion) == 'Energetica' or (opcion) == 'ENERGETICA' or (opcion) == 'BEBEIDA ENERGETICA':
            print ('')
            print ('Nuestra seleccion de bebidas energeticas:')
            print ('')
            print ('Ciclon    100 pesos')
            print ('Red Bull  120 pesos')
            print ('Monster   120 pesos\n')
            p = input ("Que bebida energetica desea? ")
            if p == 'ciclon' or p == 'Ciclon' or p == 'CICLON':
                n1 = 100
                ohno = 'Ciclon'
                print ('Esta bebida le costara 100 pesos')
                eyklk()
            elif p == 'red bull' or p == 'Red bull' or p == 'Redbull' or p == 'redbull' or p == 'red-bull' or p == 'Red-bull' or p == 'REDBULL' or p == 'RED-BULL':
                n1 = 120
                ohno = 'Red Bull'
                print ('Ese bebida le costara 120 pesos')
                eyklk()
            elif p == 'monster' or p == 'Monster':
                n1 = 120
                ohno = 'Monster'
                print ('Esa bebida le costara 120 pesos')
                eyklk()
                 
            else:
                print ('Opcion no en el menu')
    elif (opcion) == 'alcohol' or (opcion) == 'Alcohol' or (opcion) == 'ALCOHOL' or (opcion) == 'BEBIDA ALCOHOLICA'or(opcion) == 'Bebida Alcoholica' or (opcion) == 'bebida alcoholica' or opcion == 'Bebida alcoholica' or opcion == 'alcoholica' or  opcion == 'Alcoholica':
            print ('')
            print ('Nuestra seleccion de bebidas alcoholicas:')
            print ('')
            print ('Whisky')
            print ('Vodka')
            print ('Ron')
            print ('Cerveza')
            print ('Cocteles\n')
            v = input ("Que bebida alcoholica desea? ")
            if v == 'whisky' or v == 'Whisky' or v == 'WHISKY':
                gp = input ("Desea acompañante? ")
                if gp == 'Solo' or gp == 'solo' or gp == 'SOLO' or gp == 'NO' or gp == 'No' or gp == 'no' :
                    po = input ("Desea Hielo? ")
                    if po == 'no' or po == 'No' or po == 'NO':
                        n1 = 400
                        ohno = 'Whisky solo'
                        print ('Esa bebida le costara 400 pesos')
                        eyklk()
                    elif po == 'si' or po == 'Si' or po == 'SI' : 
                            n1 =430
                            ohno = 'Whisky con hielo'
                            print ('Esta bebida le costara 430 pesos')
                            eyklk()
                                   
                elif gp == 'SI' or gp == 'Si' or gp == 'si' or gp == 'acompañante' or gp == 'Acompañante' or gp == 'acompanante' or gp == 'Acompanante' or gp == 'con acompañante' or gp == 'Con acompañante' or gp == 'con' or gp == 'Con':
                        print ('Nuestra seleccion de acompañantes:')
                        print ('')
                        print ('Soda') 
                        print ('Agua tonica')
                        print ('7up')                
                        print ('Coca-Cola\n')
                        se= input ("Que acompañante desea?: ")
                        if se == 'soda' or se == 'Soda' or se == 'SODA':
                            n1 = 500
                            ohno = 'Whisky con soda'
                            print ('Esta bebida le costara 500 pesos')
                            eyklk()
                        elif se == 'agua tonica' or se == 'Agua tonica' or se == 'Agua Tonica' or se == 'aguatonica' or se == 'AGUA TONICA' or se == 'AGUATONICA':
                            n1 = 500
                            ohno = 'Whisky con Agua Tonica'
                            print ('Esta bebida le costara 500 pesos')
                            eyklk()    
                        elif se == '7up' or se == '7 up' or se == '7UP':
                            n1 = 520
                            ohno = 'Whisky con 7up'
                            print ('Esta bebida le costara 520 pesos')
                            eyklk()
                        elif se == 'COCACOLA' or se == 'COCA COLA' or se == 'COCA-COLA' or se == 'Cocacola' or se == 'cocacola' or se == 'refresco cocacola' or se == 'Refresco cocacola' or se == 'Coca-cola' or se == 'Coca-Cola' or se == 'coca cola' or se == 'Coca Cola' or se == 'Coca cola':
                            n1 = 520
                            ohno = 'Whisky con Coca-Cola'
                            print ('Esta bebida le costara 520 pesos')
                            eyklk()
                        else:
                            print ('Opcion no en el menu')
            elif v == 'vodka' or v == 'Vodka' or v == 'VODKA':
                gp = input ("Desea acompañante?")
                if gp == 'Solo' or gp == 'solo' or gp == 'SOLO' or gp == 'NO' or gp == 'no' or gp == 'No' :
                    po = input ("Desea Hielo? ")
                    if po == 'no' or po == 'No' or po == 'NO':
                        n1 = 350
                        ohno = 'Vodka solo'
                        print ('Esa bebida le costara 350 pesos')
                        eyklk()
                    elif po == 'si' or po == 'Si' or po == 'SI':
                            n1 = 370
                            ohno = 'Vodka con Hielo'
                            print ('Esta bebida le costara 370 pesos')
                            eyklk()
                                   
                elif gp == 'SI' or gp == 'Si' or gp == 'si' or gp == 'acompañante' or gp == 'Acompañante' or gp == 'acompanante' or gp == 'Acompanante' or gp == 'con acompañante' or gp == 'Con acompañante' or gp == 'con' or gp == 'Con':
                        print ('Nuestra seleccion de acompañantes:')
                        print ('')
                        print ('Soda')
                        print ('Agua tonica')
                        print ('7up')                
                        print ('Coca-Cola\n')
                        se= input ("Que acompañante desea?: ")
                        if se == 'soda' or se == 'Soda' or se == 'SODA':
                            n1 = 400
                            ohno = 'Vodka con Soda'
                            print ('Esta bebida le costara 400 pesos')
                            eyklk()
                        elif se == 'agua tonica' or se == 'Agua tonica' or se == 'Agua Tonica' or se == 'aguatonica' or se == 'AGUA TONICA' or se == 'AGUATONICA':
                            n1 = 400
                            ohno = 'Vodka con Agua Tonica'
                            print ('Esta bebida le costara 400 pesos')
                            eyklk()  
                        elif se == '7up' or se == '7 up' or se == '7UP' :
                            n1 = 450
                            ohno = 'Vodka con 7up'
                            print ('Esta bebida le costara 450 pesos')
                            eyklk()
                        elif se == 'COCACOLA' or se == 'COCA COLA' or se == 'COCA-COLA' or se == 'Cocacola' or se == 'cocacola' or se == 'refresco cocacola' or se == 'Refresco cocacola' or se == 'Coca-cola' or se == 'Coca-Cola' or se == 'coca cola' or se == 'Coca Cola' or se == 'Coca cola':
                            n1 = 450
                            ohno = 'Vodka con Coca-Cola'
                            print ('Esta bebida le costara 450 pesos')
                            eyklk()
                        else:
                            print ('')
                            print ('Opcion no en el menu')
            elif v == 'ron' or v == 'ron' or v == 'RON':
                gp = input ("Desea acompañante? ")
                if gp == 'Solo' or gp == 'solo' or gp == 'SOLO' or gp == 'NO' or gp == 'no' or gp == 'No':
                    po = input ("Desea Hielo? ")
                    if po == 'no' or po == 'No' or po == 'NO':
                        n1 = 300
                        ohno = 'Ron Solo'
                        print ('Esa bebida le costara 300 pesos')
                        eyklk()
                    elif po == 'si' or po == 'Si' or po =='SI': 
                        n1 = 320
                        ohno = 'Ron con Hielo'
                        print ('Esta bebida le costara 320 pesos')
                        eyklk()
                                   
                elif gp == 'SI' or gp == 'Si' or gp == 'si' or gp == 'acompañante' or gp == 'Acompañante' or gp == 'acompanante' or gp == 'Acompanante' or gp == 'con acompañante' or gp == 'Con acompañante' or gp == 'con' or gp == 'Con':
                        print ('Nuestra seleccion de acompañantes:')
                        print ('')
                        print ('Soda')
                        print ('Agua tonica')
                        print ('7up')                
                        print ('Coca-Cola\n')
                        se= input ("Que acompañante desea?: ")
                        if se == 'soda' or se == 'Soda' or se == 'SODA':
                            n1 = 350
                            ohno = 'Ron con Soda'
                            print ('Esta bebida le costara 350 pesos')
                            eyklk()
                        elif se == 'agua tonica' or se == 'Agua tonica' or se == 'Agua Tonica' or se == 'aguatonica' or se == 'AGUA TONICA' or se == 'AGUATONICA':
                            n1 = 350
                            ohno = 'Ron con Agua Tonica'
                            print ('Esta bebida le costara 350 pesos')
                            eyklk()    
                        elif se == '7up' or se == '7 up' or se == '7UP':
                            n1 = 400
                            ohno = 'Ron con 7up'
                            print ('Esta bebida le costara 400 pesos')
                            eyklk()
                        elif se == 'COCACOLA' or se == 'COCA COLA' or se == 'COCA-COLA' or se == 'Cocacola' or se == 'cocacola' or se == 'refresco cocacola' or se == 'Refresco cocacola' or se == 'Coca-cola' or se == 'Coca-Cola' or se == 'coca cola' or se == 'Coca Cola' or se == 'Coca cola':
                            n1 = 400
                            ohno = 'Ron con Coca-Cola'
                            print ('Esta bebida le costara 400 pesos')
                            eyklk()
                        else:
                            print ('Opcion no en el menu')            
            elif v == 'cerveza' or v == 'Cerveza' or v == 'CERVEZA':
                print ('')
                print ('Nuestra seleccion de cervezas')
                print ('')
                print ('Presidente     90/100 pesos')
                print ('Corona         80     pesos')
                print ('Heineken       80    pesos')
                print ('Blue Moon      120     pesos\n')
                i = input ("Que cerveza desea?: ")
                if i == 'presidente' or i == 'Presidente' or i == 'PRESIDENTE':
                    print ('')
                    print ('Normal  90  pesos')
                    print ('Light   90  pesos')
                    print ('Black   100 pesos')
                    kl = input('Como la prefiere?: ')
                    if kl == 'normal' or kl == 'Normal' or kl == 'NOMRMAL':
                        print ('Esta cerveza le costara 90 pesos')
                        n1 = 90
                        ohno = 'Presidente Normal'
                        eyklk()
                    elif kl == 'light' or kl == 'Light' or kl == 'LIGHT':
                        print ('Esta cerveza le costara 90 pesos')
                        n1 = 90
                        ohno = 'Presidente Light'
                        eyklk()
                    elif kl == 'black' or kl == 'BLACK' or kl == 'Black':
                        print ('Esta cerveza le costara 100 pesos')
                        n1 = 100
                        ohno = 'Presidente Black'
                        eyklk()
                    else:
                        print ('Opcion no en el menu')
                elif i == 'corona' or i == 'Corona' or i == 'CORONA':
                    print ('Esta cerveza le costara 80 pesos')
                    n1 = 80
                    ohno = 'Corona'
                    eyklk()
                elif i == 'Heineken' or i == 'heineken' or i == 'HEINEKEN':
                    print ('Esta cerveza le costara 80 pesos')
                    n1 = 80
                    ohno = 'Heineken'
                    eyklk()
                elif i== 'blue moon' or i == 'Blue moon' or i == 'BLUE MOON' or i == 'Blue Moon' or i == 'bluemoon' or i == 'BLUEMOON' or i == 'Bluemoon':
                    print ('Esta cervesza le costara 120 pesos')
                    n1 = 120
                    ohno = 'Blue Moon'
                    eyklk()
                else:
                    print ('Opcion no en el menu')
            elif v == 'Cocktail' or v == 'cocktail' or v == 'Cocteles' or v == 'cocteles' or v == 'Coctel' or v == 'coctel' or v == 'COCTELES' or v == 'COCTEL' or v == 'COCKTAIL':
                print ('')
                print ('Nuestra seleccion de cocteles')
                print ('')
                print ('Nombre        Precio                 Ingredientes')
                print ('')
                print ('Bloody Mary    400       Vodka, Jugo de Tomate, y Especies')
                print ('Cosmopolitan   350       Vodka, Triple Seco , Jugo de Arándanos y Zumo de Lima')
                print ('Daiquiri       300       Ron blanco y Jugo de Limón Criollo o Lima')
                print ('Gin Tonic      400       Ginebra y Agua Tónica,')
                print ('Margarita      350       Tequila, Triple Seco, y Jugo de Lima o Limón')
                print ('Manhattan      300       Whisky, y Vermut Rojo')
                print ('Martini        350       Ginebra con un chorro de Vermú')
                print ('Mojito         400       Ron, Azúcar, Limón, Hierbabuena y Agua Mineralizada')
                print ('')
                to = input ('Que desea ordenar? ')
                if to == 'bloody mary' or to == 'Bloody Mary' or to == 'BLOODYMARY' or to == 'bloodymary' or to == 'BLOODY MARY' or to == 'Bloody mary':
                    print ('Esta bebida le costara 400 pesos')
                    n1 = 400
                    ohno = 'Bloody Mary'
                    eyklk()
                elif to == 'Cosmopolitan' or to == 'cosmopolitan' or to == 'COSMOPOLITAN':
                    print ('Esta bebida le costara 350 pesos')
                    n1 = 350
                    ohno = 'Cosmopolitan'
                    eyklk()
                elif to == 'daiquiri' or to == 'DAIQUIRI' or to == 'Daiquiri':
                    print ('Esta bebida le costara 300 pesos')
                    n1 = 300
                    ohno = 'Daiquiri'
                    eyklk()
                elif to == 'gin tonic' or to == 'Gin Tonic' or to == 'GIN TONIC' or to == 'gintonic' or to == 'Gintonic' or to == 'GINTONIC':
                    print ('Esta bebida le costara 400 pesos')
                    n1 = 400
                    ohno = 'Gin Tonic'
                    eyklk()
                elif to == 'margarita' or to == 'MARGARITA' or to == 'Margarita':
                    print ('Esta bebida le costara 350 pesos')
                    n1 = 350
                    ohno = 'Margarita'
                    eyklk()
                elif to == 'manhattan' or to == 'MANHATTAN' or to == 'Manhattan':   
                    print ('Esta bebida le costara 300 pesos')
                    n1 = 300
                    ohno = 'Manhattan'
                    eyklk()
                elif to == 'Martini' or to == 'martini' or to == 'MARTINI':
                    print ('Esta bebida le costara 350 pesos')
                    n1 = 350
                    ohno = 'Martini'
                    eyklk()
                elif to == 'mojito' or to == 'MOJITO' or to == 'Mojito':
                    print ('Esta bebida le costara 400 pesos')
                    n1 = 400
                    ohno = 'Mojito'
                    eyklk()
                else:
                    print ('')
                    print ('Opcion no en el menu')
                    
            else:
                print ('')
                print ('Opcion no en el menu')

    else:
        print ('')
        print ('Opcion no en el menu')
                    
                        
                        
                               
                               
                
                    



                    
           

