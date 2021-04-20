wow = 1000     #es lo que usamos para asignar el ID de los libros
j = 100               #es lo que usamos para asignar el ID de los catalogos
jo = 0                 #numero  de catalogos en el programa
pis = 0               #numero de libros en el programa
def libros ():
    H = open('libros.txt','a+')
    H.write(input(""))
#MENU DE CATALOGOS_____________________________________________________________________________________________________________________
h = 0
while (h < 1):
    print('      -Menu-        \n')
    print('1) Agregar catalogo')
    print('2) Editar catalogo')
    print('3) Administrar catalogos')
    print('4) Borrar catalogos')
    print('5) Ver catalogos')
    print('6) Salir\n')
    v = input('Que desea hacer?  ')
#AGREGAR CATALOGO_____________________________________________________________________________________________________________________
    if v == '1':
        f = open('catalogos.txt', 'a+')
        f.write(input("\nDigitite el nombre de su catalogo: "))
        f = open('catalogos.txt', 'a+')
        f.write(str(j))
        print ('El ID de este catalogo es',j,'\n')
        j = j + 1
        jo = jo + 1
#EDITAR CATALOGO_____________________________________________________________________________________________________________________
    if v == '2':
        if not catalogo:
            print ('\nNo existen catalogos registrados\n')
        else:
            t = 0
            for i in  catalogo:
                print ('\n',t,')',catalogo[t],'\n')
                t = t + 1
            opo = int(input('Que catalogo desea editar? '))
            catalogo[opo] = input('Digite el nuevo nombre: ')
#ADMINISTRAR CATALOGO_____________________________________________________________________________________________________________________
    if v == '3':
        if not catalogo: 
            print("\nNo existen catalogos registrados\n")
        else:
            t = 0
            for i in  catalogo:
                print ('\n',t,') ',catalogo[t])
                t = t + 1
            ji = 0
            jue = int(input('\nQue catalogo desea administrar: '))
            while (ji < 1):
                x = 1
#FUNCION PARA IMPRIMIR LIBRO_____________________________________________________________________________________________________________________
                def libro ():
                    print ('\n')
                    print ('Nombre: ' + nombre[dud])
                    print ('Autor: ' + autor[dud])
                    print ('Edicion: '  + edicion[dud])
                    print ('ISBM: ' + isbm[dud])
                    print ('Ciudad: ' + ciudad[dud])
                    print ('Fecha: ' + fecha[dud])
                    print ('ID: ',ID[dud])
#MENU DE BIBLIOTECA_____________________________________________________________________________________________________________________                    
                while (x < 2):
                    print ('')
                    print ('Bienvenido a la biblioteca')
                    print ("1) Agregar Libro")
                    print ("2) Editar Libro")
                    print ("3) Borrar Libro") 
                    print ("4) Lista de todos los libros")
                    print ("5) Buscar por ID") 
                    print ("6) Buscar por Nombre") 
                    print ("7) Buscar por ISBM") 
                    print ("8) Salir\n")
                    xd = input ('Que desea hacer: ')
#AGREGAR LIBRO_____________________________________________________________________________________________________________________                    
                    if xd == '1':
                        print ('Digite el nombre del libro: ')
                        libros ()
                        print ('Digite el autor del libro: ')
                        libros ()
                        print ('Digite la edicion del libro: ')
                        libros ()
                        print ('Digite el ISBM del libro: ')
                        libros ()
                        print ('Digite la fecha de creacion del libro: ')
                        libros ()
                        print ('Digite la ciudad donde se publico libro: ')
                        libros ()
                        ID.append(wow)
                        print ('El ID de su libro es',wow)
                        H = open('libros.txt','a+')
                        H.write(wow)
                        wow = wow + 1
                        book.append(nombre[pis])
                        book.append(autor[pis])
                        book.append(edicion[pis])
                        book.append(isbm[pis]) 
                        book.append(fecha[pis])
                        book.append(ciudad[pis])
                        book.append (ID[pis])
                        holo = 0
                        books.append((book[0] , book[1] , book [2] , book [3] , book[4] , book[5] , book[6]))
                        del book [:]
                        pis = pis +1
#EDITAR LIBROS_____________________________________________________________________________________________________________________
                    elif xd == '2':        
                        if not nombre: 
                            print ("\nNo existen libros registrados")
                        else:
                            t = 0
                            for i in nombre:                     
                                print ('\n',t,')',nombre[t])
                                t = t + 1
                            dud = int(input('\nQue libro desea editar? '))
                            libro()
                            wat = input ('Que desea editar de este libro? ')
                            if wat == 'nombre':
                                nombre[dud] = input('Digite el nuevo nombre: ')
                            if wat == 'autor':
                                autor[dud] = input('Digite el nuevo autor: ')
                            if wat == 'edicion':
                                edicion[dud] = input('Digite la nueva edicion: ')
                            if wat == 'ISBM':
                                isbm[dud] = input('Digite el nuevo ISBM: ')
                            if wat == 'fecha':
                                fecha[dud] = input('Digite la nueva fecha: ')
                            if wat == 'ciudad':
                                ciudad[dud] = input('Digite la nueva ciudad: ')
#BORRAR LIBRO_____________________________________________________________________________________________________________________                            
                    elif xd == '3':
                        if not nombre:
                            print ('\nNo existen libros registrados')
                        else:
                            t = 0
                            for i in nombre:
                                print ('',t,')',nombre[t],'\n')
                                t = t + 1
                            LUL = int(input('\nQue libro desea eliminar? '))
                            del nombre[LUL]
                            del autor[LUL]
                            del isbm[LUL]
                            del ciudad[LUL]
                            del edicion[LUL]
                            del fecha[LUL]
                            del ID[LUL]
                            print ('Libro eliminado')
#LISTAR LIBROS_____________________________________________________________________________________________________________________
                    elif xd == '4':
                        if not nombre: 
                            print("\nNo existen libros registrados")
                        else:
                            print ('Lista de libros')
                            dud = 0
                            for i in nombre:
                                libro ()
                                dud = dud + 1

#BUSCAR LIBRO POR ID_____________________________________________________________________________________________________________________
                    elif xd == '5':
                        ki = int(input('Digite el ID: '))
                        try:
                            dud = ID.index(ki)
                            libro ()
                        except:
                            print('Libro asociado ID digitado no existe')
#BUSCAR LIBRO POR NOMBRE_____________________________________________________________________________________________________________________                        
                    elif xd == '6':
                        ki = input('Digite el nombre: ')
                        try:
                            dud = nombre.index(ki)
                            libro ()
                        except:
                            print('Libro asociado a nombre digitado no existe')
#BUSCAR LIBRO POR ISBM_____________________________________________________________________________________________________________________
                    elif xd == '7':
                        ki = input('Digite el ISBM: ')
                        try:
                            dud = isbm.index(ki)
                            libro ()
                        except:
                            print('Libro asociado a ISBM digitado no existe')
#SALIR DE MENU DE LIBRO_____________________________________________________________________________________________________________________                    
                    elif xd == '8':
                        print ('Volviendo al menu de catalogos....')
                        x = x + 1
                        ji = ji + 1
#BORRAR CATALOGOS_____________________________________________________________________________________________________________________
    if v == '4':
                        if not catalogo:
                            print ('\nNo existen catalogos registrados\n')
                        else:
                            t = 0
                            for i in catalogo:
                                print ('\n',t,')',catalogo[t],'\n')
                                t = t + 1
                            LUL = int(input('Que catalogo desea eliminar? '))
                            #try a ve si el catalogo tiene libro
                            print ('Que quiere hacer con los libros de este catalogo?')
                            print ('1) Trasladarlos a otro catalogo')
                            print ('2) Borrarlos\n')
                            LoL =input('')
                            del catalogo[LUL]
                            del aidi[LUL]
                            print ('Catalogo eliminado')

              
#LISTAR CATALOGOS_____________________________________________________________________________________________________________________
    if v == '5':
            print ('Lista de catalogos\n')
            f = open('catalogos.txt', 'r')
            contenido =  f.read()
            print (contenido)
#SALIR DE MENU DE CATALOGOS(SALIR DE PROGRAMA)_____________________________________________________________________________________________________________________
    if v == '6':
        print ('Saliendo....')
        h = h +1
        
        
       
        
    
    
