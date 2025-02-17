import os
import subprocess
import tkinter as tk
from tkinter import messagebox
import pyperclip
import re

# Función para ejecutar PyInstaller y obtener la ruta absoluta
def ejecutar_pyinstaller():
    try:
        # Obtener el directorio donde se está ejecutando el script Python
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Ejecutar pyinstaller en el mismo directorio donde está el script
        proceso = subprocess.Popen(
            ['pyinstaller', '--version'],  # Usamos '--version' para verificar si pyinstaller funciona correctamente
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=script_dir  # Establece el directorio de trabajo en el directorio del script
        )

        # Obtener la salida y los errores del comando
        stdout, stderr = proceso.communicate()

        # Verificar si hubo un error
        if proceso.returncode == 0:
            # Si no hay error, pyinstaller funciona correctamente
            ruta_absoluta = os.path.abspath(script_dir)  # Obtiene la ruta del directorio actual del script
            mostrar_ventana(f"PyInstaller está funcionando correctamente.\n\nPuedes usar pyinstaller desde este directorio:\n{ruta_absoluta}", ruta_absoluta)
        else:
            # Si hay un error, buscar la ruta del error
            error_message = stderr.decode("utf-8")
            # Usamos expresión regular para encontrar la ruta dentro del mensaje de error
            match = re.search(r"(C:\\[^\\]+\\Scripts\\pyinstaller\.py)", error_message)
            if match:
                # Extraemos la ruta del error
                ruta_error = match.group(1)
                mostrar_ventana(f"Hubo un error con PyInstaller. Puede que el archivo pyinstaller.py esté en esta ruta:\n{ruta_error}", ruta_error)
            else:
                # Si no encontramos la ruta, mostramos el error completo
                mostrar_ventana(f"Hubo un error con PyInstaller:\n{error_message}", None)

    except Exception as e:
        # Si ocurre un error general, mostrarlo
        messagebox.showerror("Error", f"Ocurrió un error al ejecutar PyInstaller:\n{str(e)}")

# Función para mostrar una ventana con la ruta y la opción de copiarla
def mostrar_ventana(mensaje, ruta):
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Resultado de PyInstaller")
    ventana.geometry("700x450")
    ventana.config(bg="#1a1a1a")  # Fondo oscuro, típico de estética hacker
    
    # Título en la parte superior
    label_titulo = tk.Label(
        ventana,
        text="PyInstaller Status",
        font=("Courier New", 18, "bold"),
        bg="#1a1a1a",
        fg="#33ff33",  # Verde brillante
        pady=10
    )
    label_titulo.pack(pady=10)
    
    # Etiqueta con el mensaje
    label_mensaje = tk.Label(
        ventana,
        text=mensaje,
        font=("Courier New", 12),
        bg="#1a1a1a",
        fg="#d1d1d1",  # Color gris claro para el texto
        justify="left",
        padx=20,
        pady=10
    )
    label_mensaje.pack(pady=10)
    
    # Si hay una ruta, agregar un botón para copiarla al portapapeles
    if ruta:
        def copiar_al_portapapeles():
            pyperclip.copy(ruta)
            messagebox.showinfo("Copiado", "La ruta ha sido copiada al portapapeles.")
        
        # Botón para copiar la ruta
        boton_copiar = tk.Button(
            ventana,
            text="Copiar al Portapapeles",
            font=("Courier New", 12),
            command=copiar_al_portapapeles,
            bg="#4CAF50",  # Verde hacker
            fg="white",
            relief="flat",
            padx=20,
            pady=10,
            bd=0,  # Sin borde
            activebackground="#388E3C",  # Color cuando el botón es presionado
            activeforeground="white"
        )
        boton_copiar.pack(pady=20)
    
    # Botón de salir
    boton_salir = tk.Button(
        ventana,
        text="Salir",
        font=("Courier New", 12),
        command=ventana.quit,
        bg="#ff3333",  # Rojo brillante
        fg="white",
        relief="flat",
        padx=20,
        pady=10,
        bd=0,  # Sin borde
        activebackground="#D32F2F",  # Color cuando el botón es presionado
        activeforeground="white"
    )
    boton_salir.pack(pady=10)
    
    # Fondo de consola con efecto de sombra para dar aspecto de terminal
    ventana.lift()
    ventana.attributes("-topmost", True)  # Mantener la ventana siempre encima
    ventana.after(100, lambda: ventana.attributes("-topmost", False))  # Hacerla no siempre encima después de unos segundos

    ventana.mainloop()

# Ejecutar el script
if __name__ == "__main__":
    ejecutar_pyinstaller()
