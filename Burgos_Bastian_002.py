import csv 
lista=[]
diccionario={}

def mayor ():
    mayor=0
    for x in lista:
        if int(x["puntos"])>int(mayor):
            mayor=x["puntos"]
        else :
            mayor=mayor
    print ("El mayor es : ",mayor)

def promedio ():
    acum=0
    cant=len(lista)
    if cant>0 :
        for x in lista:
            acum=acum+int(x["puntos"])
        prom=acum/cant
        print ("Promedio : ",prom)
        
def confirmar ():
    reps=input("Seguro que decea modificar el nombre (si/no) : ")
    if reps==("si")
        return True
    else :
        return False 

"""def actualizar(buscar,listita) :
    for x listita :
        if buscar==int(x["id"])
        print("Datos del Equipo : ")
        print (x)
        print ("")
        r=confirmar()
        if r :
            borrar=x["nombre"]
            nombre_a=input("Ingrese el nombre que desee")
            lista.remove(borrar)
            
            
        else:
            print ("Actualizacion cancelada")
            """"
        
def validacion_puntos (puntitos):
    if puntitos > 0 and puntitos <= 150 :
        return True 
    else :
        return False
def categoriap(validos,puntitos):
    if validos :
        if puntos>=0 and puntos<=40 :
            categorias="amateur"
        elif puntos>=41 and puntos<=80 :
            categorias="principiante"
        elif puntos>=81 and puntos<=120 :
            categorias="avanzado"
        elif puntos >120 :
            categorias="idolo"
        return (categorias)


while (True) :
    print ("""
-----------M E N U-----------------

1.- Agregar equipo
2.- Listar equipo
3.- Actualizar nombre de equipo por id
4.- Generar BBDD
5.- Cargar BBDD
6.- Estadísticas
0.- Salir

""")
    op=int(input("Ingrese opcion : "))
    if op==1 :
        print ("")
        print ("---------- Agregando equipo --------------    ")
        print ("")
        id=int(input("ingrese id del equipo : "))
        nombre=input("Ingrese nombre del equipo : ")
        puntos=int(input("Ingrese puntos del equipo : "))
        validacion_puntos(puntos)
        valido=validacion_puntos(puntos)
        categoriap(valido,puntos)
        categoria=categoriap(valido,puntos)
        diccionario={"id":id,"nombre":nombre,"puntos":puntos,"categoria":categoria}
        lista.append(diccionario)
        print ("")
        print ("se agrego correctamente")
    elif op==2 :
        print ("")
        print ("------------ Listar equipos ----------")
        print ("")
        for x in lista :
            print ("id : ",x["id"]," Nombre : ",x["nombre"]," Puntos : ",x["puntos"]," Categoria : ",x["categoria"] )
    elif op==3 :
        #falta
        print ("")
        print ("-------- Actualizar Nombre --------")
        print ("")
        actualizar_e=int(input("Ingrese id del equipo : "))
        
    elif op==4 :
        print ("")
        print ("------ GENERANDO ARCHIVO BBDD -------")
        print ("")
        with open ("bbdd.csv","w",newline="") as bbdd:
            campo=["id","nombre","puntos","categoria"]
            escritor=csv.DictWriter(bbdd,fieldnames=campo)
            escritor.writeheader()
            escritor.writerows(lista)
            print ("Se agrego correctamente"
    elif op==5 :
        print ("")
        print ("------- CARGANDO BBDD ------")
        print ("")
        with open ("bbdd.csv","r",newline="") as bbdd:
            lector=csv.DictReader(bbdd)
            for fila in lector :
                lista.append(fila)
                print ("se cargo la bbdd" )
    elif op==6 :
        print ("")
        print ("-------- ESTADISTICAS --------")
        print ("")
        promedio()
        mayor ()
    elif op==0 :
        print ("")
        print ("ADIOS....")
    else :
        print ("")
        print ("Ingrese opcion valida!!")
        
