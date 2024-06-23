import tkinter as tk
import cliente_gui2
import socket

def main():
    # Crear la ventana principal
    ventana = tk.Tk()

    # Crear una instancia de la GUI del cliente
    gui_cliente = cliente_gui2.ClienteGUI2(ventana, 'localhost')  
    #gui_cliente = cliente_gui2.ClienteGUI2(ventana, '192.168.137.221') # Reemplaza con la dirección IP del servidor
    #gui_cliente = cliente_gui2.ClienteGUI2(ventana, '192.168.100.122')

    # Iniciar el bucle de eventos de la interfaz gráfica
    ventana.mainloop()

if __name__ == '__main__':
    main()
