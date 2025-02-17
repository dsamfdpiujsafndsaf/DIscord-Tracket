# -*- coding: utf-8 -*-
import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Toplevel
from tkinter import ttk  # Importar ttk para usar Progressbar
import threading
from PIL import Image, ImageTk
import os

def compile_to_exe():
    # Obtener el Bot Token y Server ID ingresados
    bot_token = entry_token.get()
    server_id = entry_server.get()

    if not bot_token or not server_id:
        messagebox.showerror("Error", "Por favor, ingrese ambos parámetros: Bot Token y Server ID.")
        return

    # Abrir el archivo Python existente para editarlo
    file_path = filedialog.askopenfilename(
        defaultextension=".py",
        filetypes=[("Python Files", "*.py")],
        title="Seleccionar archivo de bot"
    )

    if not file_path:
        return  # Si el usuario cancela, no hacer nada

    # Crear una ventana emergente para mostrar la barra de progreso y la imagen
    progress_window = Toplevel()
    progress_window.title("Compilando...")
    progress_window.geometry("500x150")
    progress_window.configure(bg="#2E2E2E")
    progress_window.resizable(False, False)

    # Agregar la imagen 
    try:
        # Obtiene la ruta absoluta desde el directorio donde se ejecuta el script
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Directorio del script
        image_path = os.path.join(script_dir, "logoCompiler/diablo_emote.png")  # Ruta absoluta a la imagen

        diablo_img = Image.open(image_path)  # Abrir la imagen usando la ruta
        diablo_img = diablo_img.resize((50, 50))  # Redimensionar la imagen
        diablo_photo = ImageTk.PhotoImage(diablo_img)
        
        # Crear y mostrar el label con la imagen
        label_diablo = tk.Label(progress_window, image=diablo_photo, bg="#2E2E2E")
        label_diablo.image = diablo_photo
        label_diablo.pack(pady=10)

    except FileNotFoundError:
        messagebox.showerror("Error", "No se pudo encontrar la imagen. Asegúrate de que la ruta sea correcta.")
        return
    
    # Crear la barra de progreso
    progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=400, mode="indeterminate")  # Usar ttk
    progress_bar.pack(pady=10)
    progress_bar.start()

    # Función para realizar la compilación
    def compile_process():
        try:
            # Leer el contenido del archivo seleccionado con codificación UTF-8
            with open(file_path, "r", encoding="utf-8") as file:
                file_content = file.read()

            # Reemplazar los valores de bot_token y server_id en el archivo
            file_content = file_content.replace('bot_token = "MTEyMjI1OTQ0NDEzMTE4MDYzNw.Gk0ITL.SHuAEZrZc0XlLyif4gpUrVj787ut8BaLLM00sU"', f'bot_token = "MTEyMjI1OTQ0NDEzMTE4MDYzNw.Gk0ITL.SHuAEZrZc0XlLyif4gpUrVj787ut8BaLLM00sU"')
            file_content = file_content.replace('server_id = "1252007684564189206"', f'server_id = "1252007684564189206"')

            # Guardar el archivo con las modificaciones usando UTF-8
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(file_content)

            # Permitir al usuario seleccionar una carpeta donde depositar el ejecutable
            output_directory = filedialog.askdirectory(title="Selecciona la carpeta de destino para el ejecutable")
            if not output_directory:
                raise ValueError("No se seleccionó ninguna carpeta de destino.")

            #################################################################
            #           IMPORTANTE!! RUTA ABSOLUTA DE PYINSTALLER           #
            #################################################################

            # Ruta abosulta de pyinstaller
            pyinstaller_path = "C:/Users/Alumno/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0/LocalCache/local-packages/Python312/Scripts/pyinstaller.exe"

            # Construir el comando completo como una sola cadena
            command = f'"{pyinstaller_path}" --onefile --noconsole --distpath "{output_directory}" "{file_path}"'

            # Ejecutar pyinstaller como una única cadena
            subprocess.run(command, shell=True, check=True)

            # Cerrar la ventana de progreso cuando termine
            progress_window.destroy()
            messagebox.showinfo("Éxito", f"El archivo .exe se generó correctamente en la carpeta: {output_directory}")

        except Exception as e:
            progress_window.destroy()
            messagebox.showerror("Error", f"Hubo un problema: {e}")

    # Ejecutar la compilación en un hilo para no bloquear la interfaz gráfica
    compile_thread = threading.Thread(target=compile_process)
    compile_thread.start()


# Crear la interfaz gráfica
root = tk.Tk()
root.title("Compilador de Bot")
root.geometry("500x400")
root.configure(bg="#2E2E2E")
root.resizable(False, False)

# Estilo moderno
style_font = ("Arial", 14)
style_fg = "#00FF00"
style_bg = "#2E2E2E"
button_fg = "#FFFFFF"
button_bg = "#4CAF50"
button_hover = "#45a049"

# Agregar un título
label_title = tk.Label(root, text="Compilador de Bot", font=("Arial", 20, "bold"), fg=style_fg, bg=style_bg)
label_title.pack(pady=20)

# Bot Token
label_token = tk.Label(root, text="Bot Token:", font=style_font, fg=style_fg, bg=style_bg)
label_token.pack(pady=10)

entry_token = tk.Entry(root, width=40, font=style_font, fg=style_fg, bg="#1C1C1C", insertbackground=style_fg, relief="flat", bd=0)
entry_token.pack(pady=10)

# Server ID
label_server = tk.Label(root, text="Server ID:", font=style_font, fg=style_fg, bg=style_bg)
label_server.pack(pady=10)

entry_server = tk.Entry(root, width=40, font=style_font, fg=style_fg, bg="#1C1C1C", insertbackground=style_fg, relief="flat", bd=0)
entry_server.pack(pady=10)

# Botón de compilar
def on_hover(event):
    compile_button.config(bg=button_hover)

def on_leave(event):
    compile_button.config(bg=button_bg)

compile_button = tk.Button(root, text="Compilar a .exe", font=("Arial", 16, "bold"), fg=button_fg, bg=button_bg, relief="flat", command=compile_to_exe)
compile_button.pack(pady=30)

# Hover effect
compile_button.bind("<Enter>", on_hover)
compile_button.bind("<Leave>", on_leave)

root.mainloop()
