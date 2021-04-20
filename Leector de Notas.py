opcion = 1
while (str (opcion)!= 5):       
    n = int(input("Introduzca su calificacion "))
    if n > 100:
        print ("Datos erroneos, vuelva a intentarlo")
    elif n < 0:
        print ("Datos erroneos, vuelva a intentarlo")
    elif n >= 90:
        print ("A")
    elif n >= 85:
        print ("B+")
    elif n >= 80:
        print ("B")
    elif n >= 75:
        print ("C+")
    elif n >= 70:
        print ("C")
    elif n >= 60:
        print ("D")
    else:
        print ("F")
