import tkinter as tk
from tkinter import messagebox

def check_credentials(usuario, contrasena):
    # Aquí puedes implementar la lógica de validación de credenciales
    if usuario == "admin" and contrasena == "admin123":
        return True
    else:
        return False

def create_login_screen(ventana, salir_callback, mostrar_info_callback, login_callback):
    # Frame para el contenido principal
    frame_principal = tk.Frame(ventana, padx=20, pady=20)
    frame_principal.pack()

    # Etiqueta de bienvenida
    etiqueta_bienvenida = tk.Label(frame_principal, text="Bienvenido a la aplicación", font=("Arial", 18))
    etiqueta_bienvenida.grid(row=0, column=0, columnspan=2, pady=10)

    # Etiqueta y entrada para nombre de usuario
    etiqueta_usuario = tk.Label(frame_principal, text="Usuario:")
    etiqueta_usuario.grid(row=1, column=0, padx=10, pady=5, sticky="e")

    entrada_usuario = tk.Entry(frame_principal, width=30)
    entrada_usuario.grid(row=1, column=1, padx=10, pady=5)

    # Etiqueta y entrada para contraseña
    etiqueta_contrasena = tk.Label(frame_principal, text="Contraseña:")
    etiqueta_contrasena.grid(row=2, column=0, padx=10, pady=5, sticky="e")

    entrada_contrasena = tk.Entry(frame_principal, show="*", width=30)
    entrada_contrasena.grid(row=2, column=1, padx=10, pady=5)

    # Función para iniciar sesión
    def iniciar_sesion():
        usuario = entrada_usuario.get()
        contrasena = entrada_contrasena.get()

        if login_callback(usuario, contrasena):
            messagebox.showinfo("Login", "¡Inicio de sesión exitoso!")
            mostrar_info_callback()  # Llamar a la función para mostrar la pantalla de información de trabajadores
        else:
            messagebox.showerror("Login", "Usuario o contraseña incorrectos")

    # Botón de inicio de sesión
    boton_login = tk.Button(frame_principal, text="Iniciar Sesión", command=iniciar_sesion)
    boton_login.grid(row=3, column=0, columnspan=2, pady=10)

    # Devolver el frame principal para poder manejarlo desde el archivo main.py
    return frame_principal
