##########  LIBRERIA TOOLSORT ########### 
listaprueba=[5,3,4,1,2]
##### SELECCION #####

### ASCENDENTE ###

def ordenar_seleccionAscendente(lista):
    aux = "La lista a ordenar es la siguiente : " + str(lista)
    # n = longitud lista
    n = len(lista)

    # ciclo que recorre desde la posicion 0 hasta la n-1
    for i in range(n-1):
        # ciclo que recorre desde i+1 hasta la longitud de la lista
        for j in range(i+1,n):
            #se guarda cada paso del ciclo en la variable i y j
            #compara el valor de la lista en la posicion i con el de la posicion j
            aux=aux+"\n"+"Compara : " +str(lista[i])+" con : "+str(lista[j])+" ----> "+str(lista)
            if lista[i] > lista[j]:
                #hace el cambio que esta en i por el que esta en la ultima posicion 
                lista[i], lista[j] = lista[j] , lista[i]
                # print(lista[i],lista[j],lista)
    aux=aux+"\nLa lista ordenada queda asi : "+str(lista)  
    return aux
                

### DESCENDENTE ###

def ordenar_seleccionDescendente(lista):
    aux = "La lista a ordenar es la siguiente : " + str(lista)
    # n = longitud lista
    n = len(lista)

    # ciclo que recorre desde la posicion 0 hasta la n-1
    for i in range(n-1):
        # ciclo que recorre desde i+1 hasta la longitud de la lista
        for j in range(i+1,n):
            #se guarda cada paso del ciclo en la variable i y j
            #compara el valor de la lista en la posicion i con el de la posicion j
            aux=aux+"\n"+"Compara : " +str(lista[i])+" con : "+str(lista[j])+" ----> "+str(lista)
            if lista[i] < lista[j]:
                #hace el cambio que esta en i por el que esta en la ultima posicion 
                lista[i], lista[j] = lista[j] , lista[i]
                # print(lista[i],lista[j],lista)
    aux=aux+"\nLa lista ordenada queda asi : "+str(lista)  
    return aux
                



##### INSERCION #####

def ordenar_insercion(lista):

    aux = "La lista a ordenar es la siguiente : " + str(lista)
    # n = longitud lista
    n=len(lista)
    
    #ciclo que recorre desde la posicion 0 y en cada pasada para cada item desde 1 hasta n-1
    for i in range(1,n):
        #Se guarda el valor de la posicion i de la lista en valor actual y en posicion el valor de la i
        valoractual=lista[i]
        posicion=i
        #ciclo que desplaza hacia la derecha los items que son mayores al valor actual 
        #  cuando se llega a un item menor o al final de la sublista se inserta el item actual
        # aux=aux+'\n'+'Compara : ' +str(lista[posicion-1]) + " con : " + str(valoractual) + " ------> " + str(lista)
        while posicion > 0 and lista[posicion-1] > valoractual:
            # aux=aux+"\n"+str(lista[posicion])+ " cambia con : " + str(lista[posicion-1])
            lista[posicion]=lista[posicion-1]
            aux=aux+"\nCompara y Desplaza hacia la derecha los mas grandes ----> " + str(lista)
            posicion=posicion-1

        aux=aux+"\n"+str(lista[posicion])+ " compara con : " + str(valoractual) 
        lista[posicion]=valoractual
        aux=aux+" ----> " + str(lista)

    aux=aux+"\nLa lista ordenada queda asi : "+str(lista)  
    return aux


##### BURBUJA #####

def ordenar_burbuja(lista):
    
    aux1 = "La lista a ordenar es la siguiente : " + str(lista)
    # n = longitud lista
    n = len(lista)
    for i in range(1,n):
        for j in range(0,n-i):
            aux1=aux1+'\n'+'Compara : ' +str(lista[j]) + " con : " + str(lista[j+1]) + " ------> " + str(lista)
            #Si el elemento es menor al primero entonces se intercambian , en caso contrario ,
            #  evalua el segundo con el siguiente elemento adyacente a su izquierda 
            # el algoritmo terminara una vez que las iteraciones sea igual al numero de elmentos que contenga el vector de numeros
            if (lista[j+1]<lista[j]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
    aux1=aux1+"\nLa lista ordenada queda asi : "+str(lista) 
    return aux1
                

##### QUICKSORT #####


# def ordenar_quicksort(lista, izq, der):
    
#     #se elige un elemento de la lista a ordenar , el cual es llamada pivote.
#     #se situan los demas elementos de la lista a la izq y derecha del pivote.
#     #de manera que a unlado queden los menores que el y al otro los mayores.
#     #es decir , la lista queda separada por 2 sublistas , una por la izquierda y otra por la derecha
#     #se repiten esto hasta que todos los elementos queden ordenados
#     aux1 = "La lista a ordenar es la siguiente : " + str(lista)
#     pivote = lista[izq]
#     i = izq
#     j = der
#     aux = 0

#     while i < j:
#         while lista[i] <= pivote and i < j:
#             i += 1

#         while lista[j] > pivote:
#             j -= 1

#         if i < j:
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux
            
            
#     lista[izq] = lista[j]
#     lista[j] = pivote

#     if izq < j-1:
#         ordenar_quicksort(lista,izq,j-1)
        
#     if j+1 < der:
#         ordenar_quicksort(lista,j+1,der)
#     aux1=aux1+"\nLa lista ordenada queda de la siguiente manera : " + str(lista)
#     return aux1

# x=ordenar_quicksort(listaprueba,0,len(listaprueba) - 1)
# print(x)
def ordenar_quicksort(lista):
    izquierda = []
    centro = []
    derecha = []
    aux=''
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)

        aux=aux+str(izquierda)+str(["izquierda"])+str(centro)+str(["derecha"])+str(derecha) 
        print(aux)
        # print(izquierda+["-"]+centro+["-"]+derecha)
        
        return ordenar_quicksort(izquierda)+centro+ordenar_quicksort(derecha)
    else:

        return lista
    

# print(listaprueba)
# print(ordenar_quicksort(listaprueba))

##### MERGESORT #####

#p = primer elemento
#r = ultimo elemento
# [p,q] son secuencia

def merge(lista):

    #n=largo de la lista
    n=len(lista)

    #Parte con un if que comprueba la longitud de la lista . Si es menor que 2 , se devuelve la lista porque ya esta ordenada

    if n<2:
        return lista
    
    #De lo contrario , se divide en 2.

    else:
        medio=n//2
        der=merge(lista[:medio])
        izq=merge(lista[:medio])
        
        return ordenar_mergesort(der,izq)

def ordenar_mergesort(lista1,lista2):

    #Intercala los elementos de las divisiones.
    
    i,j = 0, 0 
    resultado=[] #lista final

    #Intercala ordenadamente
    while(i < len(lista1) and j < len(lista2)):
        if(lista1[i] < lista2[j]): 
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    #Se agregan los resultados a la lista final

    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado

# x=ordenar_quicksort(listaprueba,0,len(listaprueba)-1)
# mergesortaux= merge(listaprueba)
# x=ordenar_burbuja(listaprueba)
# x=ordenar_insercion(listaprueba)
x=ordenar_seleccionAscendente(listaprueba)
print(x)


##### HEAPSORT #####



########### FUNCIONES EXTRAS ###############



##### GENERADOR DE LISTAS #####



##### RANDOM #####



##### NORMAL #####
