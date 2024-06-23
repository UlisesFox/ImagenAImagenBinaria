import os
import time
import threading
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from multiprocessing import Process, Queue

#raiz de frame
raiz=Tk()
raiz.title("Imagenes a Matrices Binarias")
raiz.iconbitmap("menu.ico")
raiz.state('zoomed')


#variables
datos=StringVar()
tiempoS=StringVar()
tiempoF=StringVar()
tiempoE=StringVar()


#codigo de agrgar
def codigolimpiar():
    Area1.delete(1.0, END)


#codigo de agrgar
def codigoagrgar():
    archivo = filedialog.askopenfilename(title="Seleccione una imagen", initialdir="./Imágenes", filetypes=(("Imagenes jpg","*.jpg"),("Imagenes png","*.png")))
    datos.set(archivo)
    direccion=Label6.get()
    img = Image.open(direccion)
    newimg = img.resize((548,415))
    render = ImageTk.PhotoImage(newimg)
    Label13=Label(miframe, image = render, bg="light gray")
    Label13.image = render
    Label13.grid(row=2, column=1, pady=5)


#codigo de secuencial
def llamadaseria():
    start_time = time.time()
    codigoseria()
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_ms = elapsed_time * 1000
    tiempoS.set(" milisegundos" +"\n"+ str(elapsed_time_ms))
    
def codigoseria():
    direccion=Label6.get()
    image = Image.open(direccion)
    width, height = image.size
    binary_matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = image.getpixel((x, y))
            if sum(pixel) > 255:
                row.append(1)
            else:
                row.append(0)
        binary_matrix.append(row)
    with open("Imagen_matriz_secuencial.txt", 'w') as f:
        for row in binary_matrix:
            for pixel in row:
                f.write(str(pixel))
            f.write('\n')
    with open("Imagen_matriz_secuencial.txt", 'r') as f:
        content = f.read()
        Area1.insert(END, content)


#codigo de Fork
def llamadafork():
    start_time = time.time()
    codigofork()
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_ms = elapsed_time * 1000
    tiempoF.set(" milisegundos" +"\n"+ str(elapsed_time_ms))
        
def codigofork():
    direccion=Label6.get()
    img = Image.open(direccion).convert("L")
    img_array = np.array(img)
    to_binary = np.vectorize(lambda x: 0 if x < 128 else 1)
    bin_matrix = to_binary(img_array)
    with open("Imagen_matriz_fork.txt", "w") as f:
        for row in bin_matrix:
            f.write(" ".join(str(x) for x in row) + "\n")
    with open("Imagen_matriz_fork.txt", "r") as f:
        content = f.read()
    Area1.insert(END, content)


#codigo de Execute
def llamadaexecute():
    start_time = time.time()
    codigoexecute()
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_ms = elapsed_time * 1000
    tiempoE.set(" milisegundos" +"\n"+ str(elapsed_time_ms)) 

def codigoexecute():
    direccion=Label6.get()
    img = Image.open(direccion)
    img = img.convert("L")
    pixels = img.load()
    bin_matrix = []
    for i in range(img.size[0]):
        row = []
        for j in range(img.size[1]):
            gray_value = pixels[i, j]
            if gray_value < 128:
                row.append(0)
            else:
                row.append(1)
        bin_matrix.append(row)
    with open("Imagen_matriz_execute.txt", "w") as f:
        for row in bin_matrix:
            f.write(" ".join(str(x) for x in row) + "\n")
    for row in bin_matrix:
        Area1.insert(END, "".join(str(x) for x in row) + "\n")

    
#codigo de abrir txt
def abrir_archivoS():
    os.startfile("Imagen_matriz_secuencial.txt")

def abrir_archivoF():
    os.startfile("Imagen_matriz_fork.txt")

def abrir_archivoE():
    os.startfile("Imagen_matriz_execute.txt")


#frame de contencion
miframe=Frame()
miframe.pack(fill="both", expand = "True")
miframe.config(bg="gray")
miframe.pack


#label de cargar datos
Label1=Label(miframe, text="Agrege una imagen para continuar: ")
Label1.config(bg="gray", fg="white", font=10)
Label1.grid(row=0, column=1, pady=5, padx=15, sticky="e")


#label de direccion de imagen
Label2=Label(miframe, text="Direccion de la imagen: ")
Label2.config(bg="gray", fg="white", font=10)
Label2.grid(row=0, column=4, pady=5, sticky="e")


#Entry de la direccio de imagen
Label6=Entry(miframe, width=25, textvariable=datos)
Label6.config(bg="black", fg="white", font=10)
Label6.grid(row=0, column=5, pady=5)


#label de donde esta el imagen a matriz binaria
Label3=Label(miframe, text="Imagen en matriz binaria")
Label3.config(bg="gray", fg="white", font=10)
Label3.grid(row=1, column=4, pady=5)


#Label limpial
Label11=Label(miframe, text="Limpiar campo de matriz")
Label11.config(bg="gray", fg="white", font=10)
Label11.grid(row=1, column=5, pady=5)


#Label imagen a convertir
Label12=Label(miframe, text="Imagen a convertir")
Label12.config(bg="gray", fg="white", font=10)
Label12.grid(row=1, column=1, pady=5)


#Text de imagen
Area2=Text(miframe, width=50, height=18, wrap="none", state='disabled')
Area2.config(bg="light gray", font=10)
Area2.grid(row=2, column=1, padx=25, pady=10)


#Label abrir matriz secuencial
Label14=Label(miframe, text="Abrir matriz en txt de Secuencial: ")
Label14.config(bg="gray", fg="white", font=10)
Label14.grid(row=8, column=1, pady=5)

Label17=Label(miframe)
Label17.config(bg="gray", fg="white", font=10)
Label17.grid(row=7, column=1, padx=5)


#Label abrir matriz fork
Label15=Label(miframe, text="Abrir matriz en txt de Fork: ")
Label15.config(bg="gray", fg="white", font=10)
Label15.grid(row=8, column=4, pady=5)

Label18=Label(miframe)
Label18.config(bg="gray", fg="white", font=10)
Label18.grid(row=7, column=4, padx=5)


#Label abrir matriz execute
Label16=Label(miframe, text="Abrir matriz en txt de Execute: ")
Label16.config(bg="gray", fg="white", font=10)
Label16.grid(row=8, column=5, pady=5)

Label19=Label(miframe)
Label19.config(bg="gray", fg="white", font=10)
Label19.grid(row=7, column=5, padx=5)


#label de tiempo secuencial
Label4=Label(miframe, text="Tiempo de ejecución Secuencial: ")
Label4.config(bg="gray", fg="white", font=10)
Label4.grid(row=4, column=1, padx=1, pady=5)

Label8=Label(miframe, textvariable=tiempoS)
Label8.config(bg="gray", fg="white", font=10)
Label8.grid(row=5, column=1, padx=5)


#label de tiempo Fork
Label7=Label(miframe, text="Tiempo de ejecución ForkJoin: ")
Label7.config(bg="gray", fg="white", font=10)
Label7.grid(row=4, column=4, padx=5, pady=10)

Label9=Label(miframe, textvariable=tiempoF)
Label9.config(bg="gray", fg="white", font=10)
Label9.grid(row=5, column=4, padx=5)


#label de tiempo execute
Label5=Label(miframe, text="Tiempo de ejecución Execute: ")
Label5.config(bg="gray", fg="white", font=10)
Label5.grid(row=4, column=5, padx=5, pady=10)

Label10=Label(miframe, textvariable=tiempoE)
Label10.config(bg="gray", fg="white",font=10)
Label10.grid(row=5, column=5, padx=5)


#boton agrgar
bottonA=Button(miframe, text="Agregar", command=codigoagrgar)
bottonA.grid(row=0, column=2, pady=5)


#boton secuencial
bottonS=Button(miframe, text="Secuencial", command=llamadaseria)
bottonS.grid(row=6, column=1, pady=5)


#boton fork
bottonF=Button(miframe, text="ForkJoin", command=llamadafork)
bottonF.grid(row=6, column=4, pady=5)


#boton execute
bottonE=Button(miframe, text="ExecuteService", command=llamadaexecute)
bottonE.grid(row=6, column=5, pady=5)


#boton limpiar
bottonE=Button(miframe, text="Limpiar", command=codigolimpiar)
bottonE.grid(row=2, column=5, pady=5)


#boton abrir matriz secuencial
bottonE=Button(miframe, text="txtSecuencial", command=abrir_archivoS)
bottonE.grid(row=9, column=1, pady=5)


#boton abrir matriz fork
bottonE=Button(miframe, text="txtForkJoin", command=abrir_archivoF)
bottonE.grid(row=9, column=4, pady=5)


#boton abrir matriz execute
bottonE=Button(miframe, text="txtExecuteS", command=abrir_archivoE)
bottonE.grid(row=9, column=5, pady=5)


#textarea
Area1=Text(miframe, width=50, height=18, wrap="none")
Area1.config(bg="light gray", font=10)
Area1.grid(row=2, column=4, padx=5, pady=10)

ver=Scrollbar(miframe, command=Area1.yview)
ver.grid(row=2, column=3, sticky="nsew")

hor=Scrollbar(miframe, orient="horizontal", command=Area1.xview)
hor.grid(row=3, column=4, sticky="nsew")

Area1.config(yscrollcommand=ver.set)
Area1.config(xscrollcommand=hor.set)


#loop de ventana
raiz.mainloop()
