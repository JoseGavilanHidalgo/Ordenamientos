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

#### Funciones ####

def crearLista():

    lista=[]
    ventanaAgregar = Toplevel() 
    ventanaAgregar['bg'] = 'steel blue'  # color de fondo
    ventanaAgregar.geometry("500x450+500+300")
    ventanaAgregar.resizable(0,0)
    ventanaAgregar.title("CREAR LISTA")

    label1=Label(ventanaAgregar,font=fuente_0,bg= "steel blue",fg="white",text="Ingrese Numero : ").place (x=50 , y=50)
    num=IntVar()
    entry1=ttk.Entry(ventanaAgregar, textvariable= num).place(x=250 , y=55)

    button1 = ttk.Button(ventanaAgregar, text="Agregar", command=lista.append(num.get())).place(x=275,y=80)
    button2 = ttk.Button(ventanaAgregar,text="Finalizar y Mostrar",command="").place(x=150,y=150)

def crearListaRandom(n):

    ventanaAgregarR = Toplevel() #crea nueva ventana al seleccionar practicante-> mostrar datos
    ventanaAgregarR['bg'] = 'steel blue'  # color de fondo
    ventanaAgregarR.geometry("500x450+500+300")
    ventanaAgregarR.resizable(0,0)
    ventanaAgregarR.title("CREAR LISTA")

    label1=Label(ventanaAgregarR,font=fuente_0,bg= "steel blue",fg="white",text="Ingrese Numero : ").place (x=50 , y=50)
    num=IntVar()
    entry1=ttk.Entry(ventanaAgregarR, textvariable= num).place(x=250 , y=55)

    button1 = ttk.Button(ventanaAgregarR, text="Agregar", command="").place(x=275,y=80)
    button2 = ttk.Button(ventanaAgregarR,text="Finalizar y Mostrar",command="").place(x=150,y=150)
        
    lista=[0]*n
    for i in range(n):
        lista[i]= random.randint(0,1000)
    return lista





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

button2 = ttk.Button(raiz,text="Generar lista aleatoria", command="" ).place(x=320,y=120)

button3 = ttk.Button(raiz, text="IR", command="" ).place(x=137,y=340)

button4 = ttk.Button(raiz, text="IR", command="" ).place(x=367,y=340)

button5 = ttk.Button(raiz, text="IR", command="" ).place(x=367,y=450)

button6 = ttk.Button(raiz, text="IR", command="" ).place(x=137,y=450)

button7 = ttk.Button(raiz, text="IR", command="" ).place(x=367,y=560)

button8 = ttk.Button(raiz, text="IR", command="" ).place(x=137,y=560)

#### ENTRYS ####

lista=StringVar()

entry1 = ttk.Entry(raiz, state="readonly" , textvariable=lista)

#### VARIABLES ####

listaprincipal=[]


raiz.mainloop()
