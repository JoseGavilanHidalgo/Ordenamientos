##########  LIBRERIA TOOLSORT ########### 
listaprueba=[5,3,4,1,2]
##### SELECCION #####

### ASCENDENTE ###

def ordenar_seleccionAscendente(lista):
    
    # n = longitud lista
    n = len(lista)

    # ciclo que recorre desde la posicion 0 hasta la n-1
    for i in range(n-1):
        # ciclo que recorre desde i+1 hasta la longitud de la lista
        for j in range(i+1,n):
            #se guarda cada paso del ciclo en la variable i y j
            #compara el valor de la lista en la posicion i con el de la posicion j
            if lista[i] > lista[j]:
                #hace el cambio que esta en i por el que esta en la ultima posicion 
                lista[i], lista[j] = lista[j] , lista[i]
                print(lista[i],lista[j],lista)

### DESCENDENTE ###

def ordenar_seleccionDescendente(lista):
    
    # n = longitud lista
    n = len(lista)

    # ciclo que recorre desde la posicion 0 hasta la n-1
    for i in range(n-1):
        # ciclo que recorre desde i+1 hasta la longitud de la lista
        for j in range(i+1,n):
            #se guarda cada paso del ciclo en la variable i y j
            #compara el valor de la lista en la posicion i con el de la posicion j
            if lista[i] < lista[j]:
                #hace el cambio que esta en i por el que esta en la ultima posicion 
                lista[i], lista[j] = lista[j] , lista[i]
                print(lista[i],lista[j],lista)


##### INSERCION #####

def ordenar_insercion(lista):

    # n = longitud lista
    n=len(lista)
    print("La lista es : ", lista)

    #ciclo que recorre desde la posicion 0 y en cada pasada para cada item desde 1 hasta n-1
    for i in range(1,n):
        #Se guarda el valor de la posicion i de la lista en valor actual y en posicion el valor de la i
        valoractual=lista[i]
        posicion=i
        print(lista)
        #ciclo que desplaza hacia la derecha los items que son mayores al valor actual 
        #  cuando se llega a un item menor o al final de la sublista se inserta el item actual
        while posicion > 0 and lista[posicion-1] > valoractual:
            lista[posicion]=lista[posicion-1]
            posicion=posicion-1

        lista[posicion]=valoractual
    print(lista)
# ordenar_seleccionDescendente(listaprueba)
ordenar_insercion(listaprueba)


##### BURBUJA #####



##### QUICKSORT #####



##### MERGESORT #####



##### HEAPSORT #####



########### FUNCIONES EXTRAS ###############

##### GENERADOR DE LISTAS #####



##### RANDOM #####



##### NORMAL #####

