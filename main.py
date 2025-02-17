import os
import subprocess

def run_script_in_terminal():
    try:
        # Obtener la ruta absoluta del directorio donde está este script
        script_directory = os.path.dirname(os.path.abspath(__file__))
        script_to_run = os.path.join(script_directory, "CompilerPYtoEXE.py")

        # Cambiar el directorio actual al del script
        os.chdir(script_directory)

        # Comando para abrir una terminal y ejecutar el script
        if os.name == "nt":  # Para Windows
            # Usar powershell para ejecutar el script
            command = f'Powershell -NoExit -Command "python3 {script_to_run}"'
            subprocess.run(command, shell=True)
        elif os.name == "posix":  # Para Linux/Mac
            # Usar terminal predeterminada
            command = f'x-terminal-emulator -e "python3 {script_to_run}"'
            subprocess.run(command, shell=True)
        else:
            print("No se pudo determinar el sistema operativo.")

    except PermissionError as e:
        print(f"Error de permisos: {e}. Asegúrate de tener acceso al archivo o directorio.")
    except Exception as e:
        print(f"Hubo un problema: {e}")

if __name__ == "__main__":
    run_script_in_terminal()
