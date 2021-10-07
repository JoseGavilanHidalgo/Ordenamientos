##########  LIBRERIA TOOLSORT ########### 
listaprueba=[8,3,6,4,2,5,7,1]
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
        
        aux=aux+'\n'+'Compara : ' +str(lista[posicion-1]) + " con : " + str(valoractual) + " ------> " + str(lista)
        #ciclo que desplaza hacia la derecha los items que son mayores al valor actual 
        #  cuando se llega a un item menor o al final de la sublista se inserta el item actual
        while posicion > 0 and lista[posicion-1] > valoractual:
            lista[posicion]=lista[posicion-1]
            posicion=posicion-1

        lista[posicion]=valoractual
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

def ordenar_quicksort(lista, izq , der):
    aux=''
    
  
    if izq < der :
        
        (iparticion,aux1) = particion(lista, izq , der)
        aux=aux1
        ordenar_quicksort(lista,izq,iparticion)
        ordenar_quicksort(lista,iparticion+1,der)

     
  
    return aux
    
def particion(lista,izq,der):
    aux=''
    
    pivot=lista[izq]
    
    while True:
        
        aux = aux + "\nCompara : " + str(lista[der]) + " con el pivote : " + str(pivot) + " ------> " + str(lista)
        #Mientras cada elemento desde la izq este en orden(menor que el pivote) :
        while lista[izq] < pivot:
            aux = aux + "\nCompara : " + str(lista[izq]) + " con el pivote : " + str(pivot) + " ------> " + str(lista)
            izq +=1

        #Mientras cada elmento desde la der este en orden (mayor que el pivote) :
        while lista[der] > pivot:
            der -=1
            aux = aux + "\nCompara : " + str(lista[der]) + " con el pivote : " + str(pivot) + " ------> " + str(lista)
            # si la izquierda es mayor o igual que la derecha significa que no se necesita hacer intercambio, pues ya estan en orden.

        if izq >= der :

            # indicar " donde queda el piv " para poder divir el arreglo y ordenar los elementos restantes 
            # Si las variables quedaron "lejos" (es decir, la izquierda no superó ni
            # alcanzó a la derecha)
            # significa que se detuvieron porque encontraron un valor que no estaba
            # en orden, así que lo intercambiamos
            # print('kkkkkkkkkkkkkkkkkkkkk')
            # print(aux)
            # print(der)
            # print(lista[der])
            return (der,aux)

        else:

            lista[izq], lista[der] = lista[der] , lista[izq]    

            #Hasta este punto ya se intercambiaron , pero se siguen avanzando los indices

            izq += 1
            der -= 1

  


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

x=ordenar_quicksort(listaprueba,0,len(listaprueba)-1)
# mergesortaux= merge(listaprueba)
# x=ordenar_burbuja(listaprueba)
print(x)


##### HEAPSORT #####



########### FUNCIONES EXTRAS ###############



##### GENERADOR DE LISTAS #####



##### RANDOM #####



##### NORMAL #####

