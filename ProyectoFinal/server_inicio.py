import subprocess
import threading
from tkinter import messagebox
import tkinter


def ejecutar_comando(comando):
    subprocess.run(comando)

def iniciar_servidor():
    comando = ["python", "servidor_principal.py"]
    hilo = threading.Thread(target=ejecutar_comando, args=(comando,))
    hilo.start()

    comando1 = ["python", "servidor_aux1.py"]
    hilo1 = threading.Thread(target=ejecutar_comando, args=(comando1,))
    hilo1.start()

    comando2 = ["python", "servidor_aux2.py"]
    hilo2 = threading.Thread(target=ejecutar_comando, args=(comando2,))
    hilo2.start()

    hilo.join()
    hilo1.join()
    hilo2.join()

if __name__ == '__main__':
    ventana = tkinter.Tk()
    ventana.withdraw()
    print("\nIniciciando servidor_principal.py")
    print("Iniciciando servidor_aux1.py")
    print("Iniciciando servidor_aux2.py")
    messagebox.showinfo("Iniciando...", "Servidores listos")
    iniciar_servidor()