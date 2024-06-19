import tkinter as tk
from tkinter import Menu
from login import create_login_screen, check_credentials

# Función para salir de la aplicación
def salir():
    ventana.quit()

# Función para mostrar la pantalla de información de trabajadores
def mostrar_info_trabajadores():
    frame_login.pack_forget()  # Ocultar el frame de inicio de sesión
    frame_info_trabajadores.pack()  # Mostrar el frame de información de trabajadores

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Pantalla de Bienvenida")

# Crear el menú
barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

# Menú 'Archivo'
menu_archivo = Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Crear el formulario de inicio de sesión
frame_login = create_login_screen(ventana, salir, mostrar_info_trabajadores, check_credentials)

# Frame para la información de trabajadores (inicialmente oculto)
frame_info_trabajadores = tk.Frame(ventana, padx=20, pady=20)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
