import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk


class GuiaCompresionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guía para Crear un Archivo Autoextraíble con WinRAR")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")  # Fondo oscuro (estilo hacker)

        # Variables para manejar el paso actual y las imágenes
        self.paso_actual = 1
        ##self.imagenes = [
        ##    "C:\\Users\\TST\\Documents\\safe\\Discord-RAT-Shell\\buildEXE\\images\\paso1.png",  # Imagen paso 1 (Añadir archivo y crear autoextraíble)
        ##    "C:\\Users\\TST\\Documents\\safe\\Discord-RAT-Shell\\buildEXE\\images\\paso2.png",  # Imagen paso 2 (Configuración avanzada)
        ##    "C:\\Users\\TST\\Documents\\safe\\Discord-RAT-Shell\\buildEXE\\images\\paso3.png",  # Imagen paso 3 (Añadir icono)
        ##    "C:\\Users\\TST\\Documents\\safe\\Discord-RAT-Shell\\buildEXE\\images\\paso4.png",  # Imagen paso 4 (Configuración de actualizaciones)
        ##   "C:\\Users\\TST\\Documents\\safe\\Discord-RAT-Shell\\buildEXE\\images\\paso5.png",  # Imagen paso 5 (Acceso como administrador)
        ##    "C:\\Users\\TST\\Documents\\safe\\Discord-RAT-Shell\\buildEXE\\images\\paso6.png",  # Imagen paso 6 (Descomprimir en carpeta temporal)
        ##    "C:\\Users\\TST\\Documents\\safe\\Discord-RAT-Shell\\buildEXE\\images\\paso7.png"   # Imagen paso 7 (Ocultar todo)
        ##--]

        self.instrucciones = [
            "Paso 1: Añadir al archivo... y seleccionar 'Crear un archivo autoextraíble'.",
            "Paso 2: Luego ve a la pestaña Avanzado y marca la opción autoextraíble.",
            "Paso 3: En la pestaña Instalación, en el campo 'Ejecutar tras la extracción'.\n"
            "Añadir los nombres de los 2 archivos seleccionados 'file1.vbs' y 'file2.exe'",
            "Paso 4: En la pestaña Modos, selecciona 'Descomprimir en una carpeta temporal'\n"
            "Y selecionar la opción 'Ocultar el diálogo de inicio'",
            "Paso 5: En la pestaña 'Texto e icono', selecciona 'Cargar icono desde fichero'.\n"
            "Selecciona el icono que quieres para tu archivo autoextraíble.",
            "Paso 6: En la sección Actualizar, marca 'Extraer y actualizar ficheros'.\n"
            "Luego selecciona 'Sobreescribir todos los ficheros'.",
            "Paso 7: Regresa a la pestaña Avanzado y selecciona\n"
            "'Solicitar acceso como administrador'."
        ]

        # Crear los widgets de la interfaz
        self.crear_widgets()

    def crear_widgets(self):
        # Crear los widgets para la ventana #
        # Etiqueta para mostrar la instrucción del paso actual
        self.label_instruccion = tk.Label(self.root, text=self.instrucciones[self.paso_actual - 1],
                                          font=("Consolas", 14), fg="#00FF00", bg="#1e1e1e", justify=tk.LEFT)
        self.label_instruccion.pack(pady=20, padx=20)

        # Imagen para mostrar el paso visualmente
        self.imagen_paso = self.cargar_imagen(self.imagenes[self.paso_actual - 1])
        self.label_imagen = tk.Label(self.root, image=self.imagen_paso, bd=0, relief="flat")
        self.label_imagen.pack(pady=20)

        # Botones para avanzar o retroceder
        self.boton_atras = tk.Button(self.root, text="<< Atras", command=self.atras, state=tk.DISABLED,
                                     font=("Arial", 12), fg="#FFFFFF", bg="#333333", relief="flat", width=10)
        self.boton_atras.pack(side=tk.LEFT, padx=40)

        self.boton_siguiente = tk.Button(self.root, text="Siguiente >>", command=self.siguiente,
                                         font=("Arial", 12), fg="#FFFFFF", bg="#00FF00", relief="flat", width=12)
        self.boton_siguiente.pack(side=tk.RIGHT, padx=40)

        # Efecto hover para los botones
        self.boton_atras.bind("<Enter>", self.on_hover_atras)
        self.boton_atras.bind("<Leave>", self.on_leave_atras)
        self.boton_siguiente.bind("<Enter>", self.on_hover_siguiente)
        self.boton_siguiente.bind("<Leave>", self.on_leave_siguiente)

    def cargar_imagen(self, path):
        #Cargar y redimensionar la imagen
        try:
            imagen = Image.open(path)
            imagen = imagen.resize((400, 450), Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(imagen)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen {path}: {e}")
            return None

    def siguiente(self):
        #Función para avanzar al siguiente paso
        if self.paso_actual < len(self.instrucciones):
            self.paso_actual += 1
            self.actualizar_paso()

    def atras(self):
        # Función para retroceder al paso anterior #
        if self.paso_actual > 1:
            self.paso_actual -= 1
            self.actualizar_paso()

    def actualizar_paso(self):
        # Actualizar la instrucción y la imagen según el paso actual #
        # Actualizar instrucciones
        self.label_instruccion.config(text=self.instrucciones[self.paso_actual - 1])

        # Actualizar la imagen
        self.imagen_paso = self.cargar_imagen(self.imagenes[self.paso_actual - 1])
        self.label_imagen.config(image=self.imagen_paso)

        # Habilitar o deshabilitar botones
        if self.paso_actual == 1:
            self.boton_atras.config(state=tk.DISABLED)
        else:
            self.boton_atras.config(state=tk.NORMAL)

        if self.paso_actual == len(self.instrucciones):
            self.boton_siguiente.config(state=tk.DISABLED)
        else:
            self.boton_siguiente.config(state=tk.NORMAL)

    def on_hover_atras(self, event):
        # Efecto hover para el botón Atras #
        self.boton_atras.config(bg="#444444")

    def on_leave_atras(self, event):
        # Restaurar color de fondo al quitar el mouse del botón Atras #
        self.boton_atras.config(bg="#333333")

    def on_hover_siguiente(self, event):
        # Efecto hover para el botón Siguiente #
        self.boton_siguiente.config(bg="#00CC00")

    def on_leave_siguiente(self, event):
        # Restaurar color de fondo al quitar el mouse del botón Siguiente #
        self.boton_siguiente.config(bg="#00FF00")


# Crear la ventana principal
root = tk.Tk()

# Crear la aplicación
app = GuiaCompresionApp(root)

# Ejecutar la aplicación
root.mainloop()
