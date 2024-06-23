import tkinter as tk
from tkinter import messagebox

# Crea una ventana de tkinter
ventana = tk.Tk()
ventana.withdraw()  # Oculta la ventana principal

# Muestra una ventana emergente con un mensaje
messagebox.showinfo("Falta algo", "¡Falta algún elemento!")