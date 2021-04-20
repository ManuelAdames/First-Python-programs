x = 1
ID = []
autor = []
nombre = []
edicion = []
isbm = []
fecha = []
ciudad = []
wow = 1000
y = 0
def libro ():
    print ('\n')
    print ('Nombre: ' + nombre[dud])
    print ('Autor: ' + autor[dud])
    print ('Edicion: '  + edicion[dud])
    print ('ISBM: ' + isbm[dud])
    print ('Ciudad: ' + ciudad[dud])
    print ('Fecha: ' + fecha[dud])
     
    
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
    
    if xd == '1':
        o = input ('Digite el nombre del libro: ')
        nombre.append(o)
        ko = input ('Digite el autor del libro: ')
        autor.append(ko)
        bo = input ('Digite la edicion del libro: ')
        edicion.append(bo)
        do = input ('Digite el ISBM del libro: ')
        isbm.append(do)
        so = input ('Digite la fecha de creacion del libro: ')
        fecha.append(so)
        to = input ('Digite la ciudad donde se publico libro: ')
        ciudad.append(to)
        ID.append(wow)
        print ('El ID de su libro es',wow)
        wow = wow + 1
        y = y + 1
        
    elif xd == '2':        
        t = 0
        for i in nombre:
            
            print ('\n',t,')',nombre[t],'\n')
            t = t + 1
        dud = int(input('Que libro desea editar? '))
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
            
    elif xd == '3':
        t = 0
        for i in nombre:
            print (t,')',nombre[t],'\n')
            t = t + 1
        LUL = int(input('Que libro desea eliminar? '))
        del nombre[LUL]
        del autor[LUL]
        del isbm[LUL]
        del ciudad[LUL]
        del edicion[LUL]
        del fecha[LUL]

    elif xd == '4':
        print ('Lista de libros')
        dud = 0
        for i in nombre:
            libro ()
            dud = dud + 1

            
    elif xd == '5':
        ki = int(input('Digite el ID: '))
        try:
            dud = ID.index(ki)
            libro ()
        except:
            print('Libro asociado ID digitado no existe')
            

        
    elif xd == '6':
        ki = input('Digite el nombre: ')
        try:
            dud = nombre.index(ki)
            libro ()
        except:
            print('Libro asociado a nombre digitado no existe')

        
    elif xd == '7':
        ki = input('Digite el ISBM: ')
        try:
            dud = isbm.index(ki)
            libro ()
        except:
            print('Libro asociado a ISBM digitado no existe')

        
    elif xd == '8':
        print ('Saliendo....')
        x = x + 1
            
        
        
        

            


 
            


