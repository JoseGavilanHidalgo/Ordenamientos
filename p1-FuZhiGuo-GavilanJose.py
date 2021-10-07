from _tkinter import *
import numpy as np 
import tkinter as tk
import pandas as pd
from pandas import *
from tkinter import *
from tkinter import font
from tkinter import messagebox
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import ttk
from matplotlib import pyplot as plt
from pandas.core import frame
import random
from ToolSortFuZhiGuoGavilanJose import *

#### Funciones ####
def IRSELECCIONASCENDENTE():  #Aqui, creamos la ventana para el tipo de ordenamiento SELECCION
   x=ordenar_seleccionAscendente(listaprincipal)
   messagebox.showinfo("LISTA ORDENADA POR SELECCION ASCENDENTE",x)

def IRSELECCIONDESCENDENTE():
    x=ordenar_seleccionDescendente(listaprincipal)
    messagebox.showinfo("LISTA ORDENADA POR SELECCION DESCENDENTE",x)

def IRINSERCION():  #Aqui, creamos la ventana para el tipo de ordenamiento INSERCION
    x=ordenar_insercion(listaprincipal)
    messagebox.showinfo("LISTA ORDENADA POR INSERCION",x)
  

def IRQUICKSORT():  #Aqui, creamos la ventana para el tipo de ordenamiento QUICKSORT
    x=ordenar_quicksort(listaprincipal,0,len(listaprincipal)-1)
    messagebox.showinfo("LISTA ORDENADA POR QUICKSORT",x)   

def IRBUBBLESORT():  #Aqui, creamos la ventana para el tipo de ordenamiento BUBBLESORT
    x=ordenar_burbuja(listaprincipal)
    messagebox.showinfo("LISTA ORDENADA POR BUBBLESORT",x)    

def IRHEAPSORT():  #Aqui, creamos la ventana para el tipo de ordenamiento HEAPSORT
    ventanaHEAPSORT = Toplevel() 
    ventanaHEAPSORT['bg'] = 'steel blue'  # color de fondo
    ventanaHEAPSORT.geometry("500x450+500+300") # tamaño de la ventana
    ventanaHEAPSORT.resizable(0,0) # no se puede ampliar la ventana
    ventanaHEAPSORT.title("ORDENAMIENTO HEAPSORT")   # titulo

    entryHEAPSORT = ttk.Entry(ventanaHEAPSORT,state="readonly",textvariable="") # se crea un entry en donde se mostrara la lista a ordenar en modo HEAPSORT
    entryHEAPSORT.place(x=10,y=10,width=480,height=420) # se edita el ancho y largo del entry anterior          

def IRMERGESORT(): #Aqui, creamos la ventana para el tipo de ordenamiento MERGESORT
    x=ordenar_mergesort(listaprincipal)
    messagebox.showinfo("LISTA ORDENADA POR MERGESORT",x)

def crearLista():
    listaprincipal.clear()
    def mostrar():
        messagebox.showinfo("LISTA",listaprincipal)
        ventanaAgregar.destroy()

    def agregarnumero():
        listaprincipal.append(num.get())
        messagebox.showinfo("Numero Agregado","Numero "+str(num.get())+ " agregado con exito ")
        num.set(0)
        print(listaprincipal)


    ventanaAgregar = Toplevel() 
    ventanaAgregar['bg'] = 'steel blue'  # color de fondo
    ventanaAgregar.geometry("500x450+500+300")
    ventanaAgregar.resizable(0,0)
    ventanaAgregar.title("CREAR LISTA")

    label1=Label(ventanaAgregar,font=fuente_0,bg= "steel blue",fg="white",text="Ingrese Numero : ").place (x=50 , y=50)
    num=IntVar()
    entry1=ttk.Entry(ventanaAgregar, textvariable= num).place(x=250 , y=55)

    button1 = ttk.Button(ventanaAgregar, text="Agregar", command=agregarnumero).place(x=275,y=80)
    button2 = ttk.Button(ventanaAgregar,text="Finalizar y Mostrar",command=mostrar).place(x=150,y=150)

def crearListaRandom():
    listaprincipal.clear()
    def generador():
        
        for i in range(num.get()):
            listaprincipal.append(random.randint(0,20))
        messagebox.showinfo("LISTA CREADA",listaprincipal)
        ventanaAgregarR.destroy()
        

    ventanaAgregarR = Toplevel() #crea nueva ventana al seleccionar practicante-> mostrar datos
    ventanaAgregarR['bg'] = 'steel blue'  # color de fondo
    ventanaAgregarR.geometry("500x450+500+300")
    ventanaAgregarR.resizable(0,0)
    ventanaAgregarR.title("CREAR LISTA")

    label1=Label(ventanaAgregarR,font=fuente_0,bg= "steel blue",fg="white",text="Ingrese cantidad de numeros que quiere en la lista : ").place (x=20 , y=50)
    num=IntVar()
    entry1=ttk.Entry(ventanaAgregarR, textvariable= num).place(x=170 , y=95)

    button1 = ttk.Button(ventanaAgregarR, text="Crear", command=generador).place(x=200,y=150)
    

def eliminarLista():
    listaprincipal.clear()
    messagebox.showinfo("LISTA ELIMINADA","Lista eliminada con exito")
    




#### VENTANA INICIAL ####

raiz=Tk()
raiz.title("Calculadora ordenamientos")
raiz.geometry('600x700') 
raiz.config(bg="steel blue")
raiz.resizable(0,0)
raiz.update()

#### FONTS ####

fuente_0 = font.Font(family="Arial", size=15, weight="normal")

#### LABELS ####

label1=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Bienvenido" ).place(x=245, y=0)
label2=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Ingrese una lista o genere una al azar" ).place(x=130, y=60)
label3=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Ahora, seleccione el tipo de ordenamiento" ).place(x=110, y=250)
label4=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Selección" ).place(x=130, y=300)
label5=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Inserción" ).place(x=360, y=300)
label6=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Bubblesort" ).place(x=355, y=400)
label7=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Quicksort" ).place(x=130, y=400)
label8=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Mergesort" ).place(x=355, y=500)
label9=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Heapsort" ).place(x=130, y=500)

#### BUTTONS ####

button1 = ttk.Button(raiz, text="Crear lista", command=crearLista ).place(x=160,y=120)

button2 = ttk.Button(raiz,text="Generar lista aleatoria", command=crearListaRandom ).place(x=320,y=120)

button3= ttk.Button(raiz,text="Eliminar lista",command=eliminarLista).place(x=255,y=190)

button3 = ttk.Button(raiz, text="ASCENDENTE", command=IRSELECCIONASCENDENTE ).place(x=87,y=340)
button4 = ttk.Button(raiz, text="DESCENDENTE", command=IRSELECCIONDESCENDENTE ).place(x=207,y=340)

button5 = ttk.Button(raiz, text="IR", command=IRINSERCION  ).place(x=367,y=340)

button6 = ttk.Button(raiz, text="IR", command=IRBUBBLESORT ).place(x=367,y=450)

button7 = ttk.Button(raiz, text="IR", command=IRQUICKSORT ).place(x=137,y=450)

button8 = ttk.Button(raiz, text="IR", command=IRMERGESORT ).place(x=367,y=560)

button9 = ttk.Button(raiz, text="IR", command=IRHEAPSORT ).place(x=137,y=560)

#### ENTRYS ####







#### VARIABLES ####

listaprincipal=[]
# x=ordenar_burbuja(listaprueba)
# print(x)

raiz.mainloop()
