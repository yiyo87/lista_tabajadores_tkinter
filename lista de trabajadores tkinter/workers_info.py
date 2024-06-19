import tkinter as tk

def create_workers_info_screen():
    # Frame para la información de trabajadores
    frame_informacion = tk.Frame()
    frame_informacion.pack()

    # Contenido de la información de trabajadores (ejemplo)
    etiqueta_info_trabajadores = tk.Label(frame_informacion, text="Información de Trabajadores")
    etiqueta_info_trabajadores.pack(pady=10)

    # Aquí puedes agregar más widgets y funcionalidades según sea necesario

    # Devolver el frame de información de trabajadores para poder manejarlo desde el archivo main.py
    return frame_informacion
