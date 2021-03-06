##########  LIBRERIA TOOLSORT ########### 
listaprueba=[6,5,3,1,8,7,2,4,9]
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
        while posicion > 0 and lista[posicion-1] > valoractual:
            aux=aux+"\n"+str(valoractual)+ " cambia con : " + str(lista[posicion-1])
            aux=aux+"\nCompara y Desplaza hacia la derecha los mas grandes "
            lista[posicion]=lista[posicion-1]
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
    



##### MERGESORT #####

def ordenar_mergesort(lista):
  
    if len(lista) > 1: # se especifica que si el largo de al lista que se le entregue a la funcion, es mayor que 1, procedera con la funcion, ya que se necesita mas de 1 dato para realizar el ordenamiento
        mitad = len(lista) // 2 # se crea una variable para calcular la mitad de la lista con un resultado entero diviendo //
        primera = lista[:mitad] # obtenemos la primera mitad de la lista con [:mitad]
        segunda = lista[mitad:] # obtenemos la segunda mitad de la lista con [mitad:]

        ordenar_mergesort(primera) #llamamos la funcion y la aplicamos a ambas mitades
        ordenar_mergesort(segunda)
        aux1=0 #creamos variables auxiliares, utilizando aux1 para comparar su valor con el valor del largo de la primera mitad y aux2 para comparar su valor con el valor del largo de la sungda mitad
        aux2=0
        aux3=0

        while aux1 < len(primera) and aux2 < len(segunda):#aqui la condicion para entrar al ciclo while
            if primera[aux1] < segunda[aux2]: #comenzamos ordenando desde la primera mitad comparando desde la posicion aux1 con la posicion aux2 de la segunda mitad
                lista[aux3] = primera[aux1] #se reemplaza en la lista, en la posicion aux3, el valor que se encuentre en la posicion aux1 de la primera mitad
                aux1+=1
            else:
                lista[aux3] = segunda[aux2] #si el valor en la segunda mitad en la posicion aux2 es menor que el valor de la primera mitad en la posicion aux1, se reemplaza el valor de la posicion aux3 por el valor de la segunda mitad en la posicion aux2
                aux2+=1
  


            aux3+=1

        while aux1 < len(primera): #comparamos el valor de aux1 acumulado con el largo de la primera mitad para entrar al ciclo while siempre y cuando aux1 sea menor a len(primera)
            lista[aux3] = primera[aux1] #reemplazamos el valor de la posicion aux3 de la lista principal por el dato que se ecuentre en la primera mitad en la posicion aux1
            aux1+=1
            aux3+=1
        while aux2 < len(segunda): #se realiza la misma comparacion pero esta vez con el largo de la segunda mitad y con el valor acumulado del auxiliar 2, luego se entra al ciclo while
      
            lista[aux3] = segunda[aux2] #se reemplazan los valores
            aux2+=1
            aux3+=1    

        print('primera : ')
        print(primera)  
        print('segunda :')
        print(segunda)
  

print(listaprueba)
ordenar_mergesort(listaprueba)
print(listaprueba)

##### HEAPSORT #####

# para agrupar el subarbol en el indice i
# n es el tamano
def amontonar(lista, n, i):
	mlargo = i # raiz
	l = 2 * i + 1	 # izq = 2*i + 1
	r = 2 * i + 2	 # derecho = 2*i + 2

	# Si existe un hijo izquierdo en la raiz exists y es mayor que la raiz
	if l < n and lista[i] < lista[l]:
		mlargo = l

	# Si existe un hijo derecho en la raiz y es mayor que la raiz
	if r < n and lista[mlargo] < lista[r]:
		mlargo = r

	# Cambiamos raiz si es necesario
	if mlargo != i:
		lista[i],lista[mlargo] = lista[mlargo],lista[i] # Realiza el cambio
		# amontonar la raiz
		amontonar(lista, n, mlargo)

def ordenar_heapsort(lista):
	n = len(lista)
    
    #Construimos el MaxHeap
    # Dado que el ??ltimo padre estar?? en ((n // 2) -1) podemos comenzar en esa ubicaci??n.
	for i in range(n // 2 - 1, -1, -1):
		amontonar(lista, n, i)

	#Extrayemos 1 por 1
	for i in range(n-1, 0, -1):
		lista[i], lista[0] = lista[0], lista[i] # cambiamos
		amontonar(lista, i, 0)

# ordenar_heapsort(listaprueba)
# print(listaprueba)