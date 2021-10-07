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

raiz=Tk()



raiz.title("Calculadora ordenamientos")
raiz.geometry('600x700') 
raiz.config(bg="steel blue")
raiz.resizable(0,0)
raiz.update()

fuente_0 = font.Font(family="Arial", size=15, weight="normal")

label1=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Bienvenido" ).place(x=245, y=0)
label2=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Ingrese una lista o genere una al azar" ).place(x=130, y=60)

button1 = ttk.Button(raiz, text="Crear lista", command="" ).place(x=160,y=150)
button2 = ttk.Button(raiz,text="Generar lista aleatoria", command="" ).place(x=320,y=150)


label3=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Ahora, seleccione el tipo de ordenamiento" ).place(x=110, y=220)


label4=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Selección" ).place(x=130, y=300)
button3 = ttk.Button(raiz, text="IR", command="" ).place(x=137,y=340)

label5=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Inserción" ).place(x=360, y=300)
button4 = ttk.Button(raiz, text="IR", command="" ).place(x=367,y=340)

label6=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Bubblesort" ).place(x=355, y=400)
button5 = ttk.Button(raiz, text="IR", command="" ).place(x=367,y=450)

label7=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Quicksort" ).place(x=130, y=400)
button6 = ttk.Button(raiz, text="IR", command="" ).place(x=137,y=450)

label8=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Mergesort" ).place(x=355, y=500)
button7 = ttk.Button(raiz, text="IR", command="" ).place(x=367,y=560)

label9=Label(raiz,font=fuente_0,bg="steel blue",fg="white", text="Heapsort" ).place(x=130, y=500)
button8 = ttk.Button(raiz, text="IR", command="" ).place(x=137,y=560)





raiz.mainloop()
