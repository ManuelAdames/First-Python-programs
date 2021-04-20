salir = 0
x = 0
i = 1
#LAS 2 VARIABLES SIGUIENTES SON DEL #4 n_libros = NUMERO DE LIBROS nom_libros = NOMBRE DEL LIBRO" t = TITULO
n_libros = 0
nom_libros = 0
t = 1



while salir == 0:
    print ("\nBienvenido/a a la libreria\n")
    print ("1) Agregar Libro") ###
    print ("2) Editar Libro")
    print ("3) Borrar Libro")  ###
    print ("4) Lista de todos los libros") ##
    print ("5) Buscar por ID") ###
    print ("6) Buscar por Nombre") ##
    print ("7) Buscar por ISBM") ###
    print ("8) Salir\n")

    global opcion
    opcion = input("Introduzca el número de su elección: ")
    



#AGREGAR LIBRO_____________________________________________________________________________________________________________________  
    if opcion == "1":    
        ID = str(input ("\n\nID del libro: "))
        autor = str(input("Nombre del autor: "))
        nombre = str(input("Título del libro: "))
        edicion = str(input("Edición del libro: "))
        isbm = str(input("Codigo ISMB: "))
        fecha = str(input("Fecha de publicación: "))
        ciudad = str(input("Nombre de la ciudad del libro: "))

        lista = [ID, autor, nombre, edicion, isbm, fecha, ciudad]

        if x == 0:
            biblioteca = [lista]
            x += 1

        elif x >= 1:
            biblioteca.insert(i, lista)
            i += 1

#EDITAR LIBRO_____________________________________________________________________________________________________________________ 
    elif opcion == "2":
        print ("WASAKAKA")

#BORRAR LIBRO_____________________________________________________________________________________________________________________ 
    elif opcion == "3":
        n_libros = 0
        print ("Que libro desea borrar?")

        for libro in (biblioteca):
            for caracter in biblioteca[n_libros]:
        
                if nom_libros == 2:
                    print ("\t" + str(t) + ") " + caracter)
                    nom_libros = 0
                    t += 1
                    break
        
                else:
                    nom_libros += 1
                    continue
        
            n_libros +=1
            
        titulo = int(input ("Introduzca el numero correspondiente al libro que desea eliminar: "))

        if titulo <= len(biblioteca):
            biblioteca.pop(titulo - 1)
            print ("El libro fue eliminado exitosamente")
            n_libros = 0
            t = 1
           
            
        else:
            print ("Favor de colocar el numero correspondiente al libro que desea eliminar")
            
        
        


#LISTA DE TODOS LOS LIBROS________________________________________________________________________________________________________ 
    if opcion == "4":
        try:
            for libro in biblioteca:
                print (libro)
        except:
            print ("Aun no hay libros existentes")
        
#BUSCAR POR ID ___________________________________________________________________________________________________________________

    if opcion == "5":
        n_libros = 0
        n_id = input ("\nIntroduce el ID del libro: ")
            
        for libro in biblioteca:
            for caracter in libro:
                if n_id == caracter:
                    i = biblioteca.index(libro)
                    print ("\nResultado de la busqueda: ")
                    print (biblioteca[i])
                    break
                break
                
                if n_id != caracter:
                    print ("El ID introducido no coincide con los libros disponibles, intente de nuevo")
                    break


#BUSCAR POR NOMBRE ________________________________________________________________________________________________________________            
        
    if opcion == "6":
        i = 0
        n_libros = 0
        n_nombre = input ("\nIntroduce el nombre del libro: ")


        for libro in biblioteca:
            for caracter in libro:
                if n_nombre == caracter:
                    if i == 2:
                        i = biblioteca.index(libro)
                        print ("\nResultado de la busqueda: ")
                        print (biblioteca[i])
                        break
                    break
                
                if n_nombre != caracter:
                    i += 1

#BUSCAR POR ISBM _________________________________________________________________________________________________________________
                    
       
    if opcion == "7":
        i = 0
        n_libros = 0
        n_nombre = input ("\nIntroduce el ISBM del libro: ")


        for libro in biblioteca:
            for caracter in libro:
                if n_nombre == caracter:
                    if i == 4:
                        i = biblioteca.index(libro)
                        print ("\nResultado de la busqueda: ")
                        print (biblioteca[i])
                        break
                    break
                
                if n_nombre != caracter:
                    i += 1


#SALIR ___________________________________________________________________________________________________________________________


    if opcion == "8":
        break
