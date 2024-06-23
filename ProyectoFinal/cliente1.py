import tkinter as tk
import cliente_gui1

def main():
    # Crear la ventana principal
    ventana = tk.Tk()

    # Crear una instancia de la GUI del cliente
    #cliente_gui1.ClienteGUI1(ventana, 'localhost')
    #cliente_gui1.ClienteGUI1(ventana, '192.168.137.221')  # Reemplaza con la dirección IP del servidor
    cliente_gui1.ClienteGUI1(ventana, '192.168.100.66')

    # Iniciar el bucle de eventos de la interfaz gráfica
    ventana.mainloop()

if __name__ == '__main__':
    main()
