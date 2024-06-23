import os
import subprocess
import time
from tkinter import messagebox
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter as tk
import socket
from screeninfo import get_monitors

#creacion de interfaz
class ClienteGUI2:
    def __init__(self, ventana, direccion_ip):
        self.ventana = ventana
        self.servidor = direccion_ip

        #interfaz
        self.ventana.title("Imagenes a Matrices Binarias")
        self.ventana.iconbitmap("menu.ico")
        #self.ventana.state('zoomed')
        monitor = get_monitors()[0]
        ancho = monitor.width
        altura = monitor.height
        self.ventana.geometry(f"{ancho}x{altura}")

        #variables
        self.datos=StringVar()
        self.tiempoS=StringVar()
        self.tiempoF=StringVar()
        self.tiempoE=StringVar()

        #frame de contencion
        self.miframe=tk.Frame(self.ventana)
        self.miframe.pack(fill="both", expand = "True")
        self.miframe.config(bg="gray")

        #label de cargar datos
        self.Label1=Label(self.miframe, text="agreg una imagen para continuar     ")
        self.Label1.config(bg="gray", fg="white", font=10)
        self.Label1.grid(row=0, column=1, pady=5, padx=15, sticky="e")

        #label de direccion de imagen
        self.Label2=Label(self.miframe, text="Direccion de la imagen: ")
        self.Label2.config(bg="gray", fg="white", font=10)
        self.Label2.grid(row=0, column=4, pady=5, sticky="e")
        
        #Entry de la direccio de imagen
        self.Label6=Entry(self.miframe, width=25, textvariable=self.datos)
        self.Label6.config(bg="black", fg="white", font=10)
        self.Label6.grid(row=0, column=5, pady=5)
        
        #label de donde esta el imagen a matriz binaria
        self.Label3=Label(self.miframe, text="Imagen en matriz binaria")
        self.Label3.config(bg="gray", fg="white", font=10)
        self.Label3.grid(row=1, column=4, pady=5)
        
        #Label limpial
        self.Label11=Label(self.miframe, text="Limpiar campo de matriz")
        self.Label11.config(bg="gray", fg="white", font=10)
        self.Label11.grid(row=1, column=5, pady=5)
        
        #Label imagen a convertir
        self.Label12=Label(self.miframe, text="Imagen a convertir")
        self.Label12.config(bg="gray", fg="white", font=10)
        self.Label12.grid(row=1, column=1, pady=5)
        
        #Text de imagen
        self.Area2=Text(self.miframe, width=50, height=18, wrap="none", state='disabled')
        self.Area2.config(bg="light gray", font=10)
        self.Area2.grid(row=2, column=1, padx=25, pady=10)
        
        #Label abrir matriz secuencial
        self.Label14=Label(self.miframe, text="Abrir matriz en txt de Secuencial: ")
        self.Label14.config(bg="gray", fg="white", font=10)
        self.Label14.grid(row=8, column=1, pady=5)
        
        self.Label17=Label(self.miframe)
        self.Label17.config(bg="gray", fg="white", font=10)
        self.Label17.grid(row=7, column=1, padx=5)
        
        #Label abrir matriz fork
        self.Label15=Label(self.miframe, text="Abrir matriz en txt de Fork: ")
        self.Label15.config(bg="gray", fg="white", font=10)
        self.Label15.grid(row=8, column=4, pady=5)
        
        self.Label18=Label(self.miframe)
        self.Label18.config(bg="gray", fg="white", font=10)
        self.Label18.grid(row=7, column=4, padx=5)

        #Label abrir matriz execute
        self.Label16=Label(self.miframe, text="Abrir matriz en txt de Execute: ")
        self.Label16.config(bg="gray", fg="white", font=10)
        self.Label16.grid(row=8, column=5, pady=5)
        
        self.Label19=Label(self.miframe)
        self.Label19.config(bg="gray", fg="white", font=10)
        self.Label19.grid(row=7, column=5, padx=5)

        #label de tiempo secuencial
        self.Label4=Label(self.miframe, text="Tiempo de ejecución Secuencial: ")
        self.Label4.config(bg="gray", fg="white", font=10)
        self.Label4.grid(row=4, column=1, padx=1, pady=5)
        
        self.Label8=Label(self.miframe, textvariable=self.tiempoS)
        self.Label8.config(bg="gray", fg="white", font=10)
        self.Label8.grid(row=5, column=1, padx=5)

        #label de tiempo Fork
        self.Label7=Label(self.miframe, text="Tiempo de ejecución ForkJoin: ")
        self.Label7.config(bg="gray", fg="white", font=10)
        self.Label7.grid(row=4, column=4, padx=5, pady=10)
        
        self.Label9=Label(self.miframe, textvariable=self.tiempoF)
        self.Label9.config(bg="gray", fg="white", font=10)
        self.Label9.grid(row=5, column=4, padx=5)

        #label de tiempo execute
        self.Label5=Label(self.miframe, text="Tiempo de ejecución Execute: ")
        self.Label5.config(bg="gray", fg="white", font=10)
        self.Label5.grid(row=4, column=5, padx=5, pady=10)
        
        self.Label10=Label(self.miframe, textvariable=self.tiempoE)
        self.Label10.config(bg="gray", fg="white",font=10)
        self.Label10.grid(row=5, column=5, padx=5)

        #boton agrgar
        self.bottonA=Button(self.miframe, text="Agregar", command=self.codigoagrgar)
        self.bottonA.grid(row=0, column=1, pady=5)

        #boton secuencial
        self.bottonS=Button(self.miframe, text="Secuencial", command=self.llamadaseria)
        self.bottonS.grid(row=6, column=1, pady=5)

        #boton fork
        self.bottonF=Button(self.miframe, text="ForkJoin", command=self.llamadafork)
        self.bottonF.grid(row=6, column=4, pady=5)

        #boton execute
        self.bottonE=Button(self.miframe, text="ExecuteService", command=self.llamadaexecute)
        self.bottonE.grid(row=6, column=5, pady=5)

        #boton limpiar
        self.bottonE=Button(self.miframe, text="Limpiar", command=self.codigolimpiar)
        self.bottonE.grid(row=2, column=5, pady=5)

        #boton abrir matriz secuencial
        self.bottonE=Button(self.miframe, text="txtSecuencial", command=self.abrir_archivoS)
        self.bottonE.grid(row=9, column=1, pady=5)

        #boton abrir matriz fork
        self.bottonE=Button(self.miframe, text="txtForkJoin", command=self.abrir_archivoF)
        self.bottonE.grid(row=9, column=4, pady=5)

        #boton abrir matriz execute
        self.bottonE=Button(self.miframe, text="txtExecuteS", command=self.abrir_archivoE)
        self.bottonE.grid(row=9, column=5, pady=5)

        #enviar imagen
        self.bottonEn=Button(self.miframe, text="Enviar", command=self.enviar_imagen)
        self.bottonEn.grid(row=0, column=2, pady=5)

        #recibir imagen
        self.bottonEn=Button(self.miframe, text="Recibir", command=self.save_imagen)
        self.bottonEn.grid(row=1, column=2, pady=5)

        #fusionar imagen
        self.bottonfu=Button(self.miframe, text="Fusionar", command=self.fusionar_imagen)
        self.bottonfu.grid(row=2, column=2, pady=5)

        #textarea
        self.Area1=Text(self.miframe, width=50, height=18, wrap="none")
        self.Area1.config(bg="light gray", font=10)
        self.Area1.grid(row=2, column=4, padx=5, pady=10)

        self.ver=Scrollbar(self.miframe, command=self.Area1.yview)
        self.ver.grid(row=2, column=3, sticky="nsew")

        self.hor=Scrollbar(self.miframe, orient="horizontal", command=self.Area1.xview)
        self.hor.grid(row=3, column=4, sticky="nsew")

        self.Area1.config(yscrollcommand=self.ver.set)
        self.Area1.config(xscrollcommand=self.hor.set)


#Codigo:
    #codigo de limpiar
    def codigolimpiar(self):
        self.Area1.delete(1.0, tk.END)
        messagebox.showinfo("info", "Campos limpiados")

    #codigo de agrgar
    def codigoagrgar(self):
        archivo = filedialog.askopenfilename(title="Seleccione una imagen", initialdir="./Imágenes", filetypes=(("Imagenes", "*.jpg;*.jpeg;*.png;*.gif;*.bmp"), ("Todos los archivos", "*.*")))
        if archivo:    
            self.datos.set(archivo)
            direccion=self.Label6.get()
            img = Image.open(direccion)
            newimg = img.resize((548,415))
            render = ImageTk.PhotoImage(newimg)
            Label13=Label(self.miframe, image = render, bg="light gray")
            Label13.image = render
            Label13.grid(row=2, column=1, pady=5)
        else:
            messagebox.showinfo("Falta imagen", "¡No se seleccionó ninguna imagen!")

    #codigo de enviar
    def enviar_imagen(self):
        direccion = self.datos.get()
        if direccion:
            cliente_valor = 2
            with open(direccion, 'rb') as file:
                image_data = file.read()

            data_to_send = bytes([cliente_valor]) + image_data

            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((self.servidor, 12345))
            client_socket.sendall(data_to_send)
            client_socket.close()
        else:
            messagebox.showinfo("Falta imagen", "¡No se seleccionó ninguna imagen!")

    
    def save_imagen(self):
        direccion = self.datos.get()
        if direccion:
            comando = ["python", "cliente_aux2.py"]
            subprocess.run(comando)
            messagebox.showinfo("Conexion...", "Imagen guardada")
        else:
            messagebox.showinfo("Falta imagen...", "¡No se seleccionó ninguna imagen!")

    def fusionar_imagen(self):
        respuesta = messagebox.askyesno("Continuar...", "¿Estás seguro de fusionar la imagen actual y la almacenada? Esto remplazara tu imagen actual por la imagen fusionada")        
        ruta = "C:/Users/Dark6/Documents/Python/ProyectoFinal/Recibida1.jpg" #cambiar siempre
        if respuesta:
            if os.path.exists(ruta):
                messagebox.showinfo("Fusionando...", "Imagen fusionada")
                # Abrir las imágenes
                direccion=self.Label6.get()
                imagen_1 = Image.open(direccion)
                imagen_2 = Image.open(ruta)

                # Obtener las dimensiones de las imágenes
                ancho1, alto1 = imagen_1.size
                ancho2, alto2 = imagen_2.size

                # Asegurarse de que ambas imágenes tengan el mismo ancho
                if ancho1 != ancho2:
                    imagen_2 = imagen_2.resize((ancho1, alto2), resample=Image.BILINEAR)

                # Crear una nueva imagen con el ancho de la imagen1 y la suma de las alturas de ambas imágenes
                fusionada = Image.new('RGB', (ancho1, alto1 + alto2))

                # Pegar las imágenes en la imagen fusionada
                fusionada.paste(imagen_1, (0, 0))
                fusionada.paste(imagen_2, (0, alto1))

                # Guardar la imagen fusionada
                fusionada.save('imagen_fusionada2.jpg')
                fusion = "C:/Users/Dark6/Documents/Python/ProyectoFinal/imagen_fusionada2.jpg" #cambiar siempre
                self.datos.set(fusion)
                direccion=self.Label6.get()
                img = Image.open(direccion)
                newimg = img.resize((548,415))
                render = ImageTk.PhotoImage(newimg)
                Label13=Label(self.miframe, image = render, bg="light gray")
                Label13.image = render
                Label13.grid(row=2, column=1, pady=5)
            else:
                messagebox.showinfo("Falta archivo...", "El archivo Recibida1.jpg no se encuentra en el dispositivos")
        else:
            messagebox.showinfo("Cancelando...", "Fusion denegada")

    #codigo de secuencial
    def llamadaseria(self):
        direccion=self.Label6.get()
        if direccion:
            start_time = time.time()
            self.codigoseria()
            end_time = time.time()
            elapsed_time = end_time - start_time
            elapsed_time_ms = elapsed_time * 1000
            self.tiempoS.set(" milisegundos" +"\n"+ str(elapsed_time_ms))
        else:
            messagebox.showinfo("Falta imagen...", "¡No se seleccionó ninguna imagen!")
    
    
    def codigoseria(self):
        direccion=self.Label6.get()
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
            self.Area1.insert(END, content)
    
    #codigo de Fork
    def llamadafork(self):
        direccion=self.Label6.get()
        if direccion:
            start_time = time.time()
            self.codigofork()
            end_time = time.time()
            elapsed_time = end_time - start_time
            elapsed_time_ms = elapsed_time * 1000
            self.tiempoF.set(" milisegundos" +"\n"+ str(elapsed_time_ms))
        else:
            messagebox.showinfo("Falta imagen...", "¡No se seleccionó ninguna imagen!")
     
        
    def codigofork(self):
        direccion=self.Label6.get()
        img = Image.open(direccion).convert("L")
        img_array = np.array(img)
        to_binary = np.vectorize(lambda x: 0 if x < 128 else 1)
        bin_matrix = to_binary(img_array)
        with open("Imagen_matriz_fork.txt", "w") as f:
            for row in bin_matrix:
                f.write(" ".join(str(x) for x in row) + "\n")
        with open("Imagen_matriz_fork.txt", "r") as f:
            content = f.read()
        self.Area1.insert(END, content)

    #codigo de Execute
    def llamadaexecute(self):
        direccion=self.Label6.get()
        if direccion:
            start_time = time.time()
            self.codigoexecute()
            end_time = time.time()
            elapsed_time = end_time - start_time
            elapsed_time_ms = elapsed_time * 1000
            self.tiempoE.set(" milisegundos" +"\n"+ str(elapsed_time_ms)) 
        else:
            messagebox.showinfo("Falta imagen...", "¡No se seleccionó ninguna imagen!")

    def codigoexecute(self):
        direccion=self.Label6.get()
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
            self.Area1.insert(END, "".join(str(x) for x in row) + "\n")

    #codigo de abrir txt
    def abrir_archivoS(self):
        respuesta = messagebox.askyesno("Continuar...", "Abrir el archivo de texto donde esta almacenada la matriz binaria")
        ruta = "C:/Users/Dark6/Documents/Python/ProyectoFinal/Imagen_matriz_secuencial.txt"
        if respuesta:
            if os.path.exists(ruta):
                os.startfile("Imagen_matriz_secuencial.txt")
            else:
                messagebox.showinfo("Falta archivo...", "El archivo Imagen_matriz_secuencial.txt no se encuentra en el dispositivos")
        else:
            messagebox.showinfo("Cancelando...", "Apertura de archivo denegada")

    def abrir_archivoF(self):
        respuesta = messagebox.askyesno("Continuar...", "Abrir el archivo de texto donde esta almacenada la matriz binaria")
        ruta = "C:/Users/Dark6/Documents/Python/ProyectoFinal/Imagen_matriz_fork.txt"
        if respuesta:
            if os.path.exists(ruta):
                os.startfile("Imagen_matriz_fork.txt")
            else:
                messagebox.showinfo("Falta archivo...", "El archivo Imagen_matriz_fork.txt no se encuentra en el dispositivos")
        else:
            messagebox.showinfo("Cancelando...", "Apertura de archivo denegada")

    def abrir_archivoE(self):
        respuesta = messagebox.askyesno("Continuar...", "Abrir el archivo de texto donde esta almacenada la matriz binaria")
        ruta = "C:/Users/Dark6/Documents/Python/ProyectoFinal/Imagen_matriz_execute.txt"
        if respuesta:
            if os.path.exists(ruta):
                os.startfile("Imagen_matriz_execute.txt")
            else:
                messagebox.showinfo("Falta archivo...", "El archivo Imagen_matriz_execute.txt no se encuentra en el dispositivos")
        else:
            messagebox.showinfo("Cancelando...", "Apertura de archivo denegada")