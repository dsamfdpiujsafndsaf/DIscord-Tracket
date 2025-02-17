# **Discord RAT Windows - botConnect**

Este proyecto es una **Herramienta de administración remota (RAT)** basada en **Discord**, que permite ejecutar comandos de forma remota en una máquina víctima a través de un bot de Discord. El bot se conecta a un servidor Discord especificado por el usuario y los comandos se ejecutan a través de un canal de texto dentro del servidor Discord, lo que facilita la administración remota en un entorno controlado..

El bot es capaz de ejecutar comandos personalizados con el prefijo `!`, proporcionando acceso completo a la máquina víctima y facilitando la interacción en tiempo real. El proyecto incluye varias herramientas para automatizar la creación y compilación de un **archivo ejecutable (EXE)** que se puede ejecutar en la máquina víctima sin levantar sospechas..

---

## **Project Characteristics**

El proyecto incluye los siguientes scripts y funcionalidades.:

### 1. **botConnect.py**

- **Main Function**: Este script genera la conexión del bot de Discord que se conecta a un servidor específico.
- **Commands**:
    - `!myhelp`: Muestra una lista de comandos disponibles..
    - `!geolocate`: Muestra la dirección IP pública de la máquina víctima, además de otra información sobre la ubicación de dicha IP.
    - **Additional commands**: Comandos personalizados que puede definir para interactuar con la máquina víctima.

## !myhelp (List)

### 📜 Comandos Disponibles

### Comandos Generales:

- `!message` = Mostrar un cuadro de mensaje con tu texto  
  Sintaxis: `!message ejemplo`

- `!shell` = Ejecutar un comando de shell  
  Sintaxis: `!shell whoami`

- `!voice` = Hacer que una voz diga en voz alta una frase personalizada  
  Sintaxis: `!voice prueba`

- `!admincheck` = Comprobar si el programa tiene privilegios de administrador

- `!cd` = Cambiar de directorio

- `!dir` = Mostrar todos los elementos en el directorio actual

- `!download` = Descargar un archivo desde el ordenador infectado

- `!upload` = Subir un archivo al ordenador infectado  
  Sintaxis: `!upload archivo.png` (con archivo adjunto)

- `!delete` = Eliminar un archivo  
  Sintaxis: `!delete /ruta/del/archivo.txt`

- `!write` = Escribir tu frase deseada en el ordenador

- `!clipboard` = Recuperar el contenido del portapapeles del ordenador infectado

- `!idletime` = Obtener el tiempo de inactividad de los usuarios en el ordenador objetivo

- `!datetime` = Mostrar fecha y hora actuales

- `!currentdir` = Mostrar el directorio actual

---

### Escalado de Privilegios y Control del Sistema:

- `!getadmin` = Solicitar privilegios de administrador a través del aviso UAC

- `!block` = Bloquear el teclado y el ratón del usuario (Se requieren privilegios de administrador)

- `!unblock` = Desbloquear el teclado y el ratón del usuario (Se requieren privilegios de administrador)

- `!screenshot` = Tomar una captura de pantalla de la pantalla actual del usuario

- `!exit` = Salir del programa

- `!kill` = Matar una sesión o proceso  
  Sintaxis: `!kill session-3` o `!kill all`

- `!uacbypass` = Intentar eludir UAC para obtener privilegios de administrador

- `!shutdown` = Apagar el ordenador

- `!restart` = Reiniciar el ordenador

- `!logoff` = Cerrar sesión del usuario actual

- `!bluescreen` = Provocar una pantalla azul (Se requieren privilegios de administrador)

- `!migrateprocess <process_name>` = Migrar un proceso en ejecución a una nueva instancia.  
  Sintaxis: `!migrateprocess ejemplo.exe`

---

### Seguridad y Modificaciones del Sistema:

- `!prockill` = Matar un proceso por nombre  
  Sintaxis: `!prockill proceso`

- `!disabledefender` = Deshabilitar Windows Defender (Se requieren privilegios de administrador)

- `!disablefirewall` = Deshabilitar el Firewall de Windows (Se requieren privilegios de administrador)

- `!critproc` = Convertir el programa en un proceso crítico (Se requieren privilegios de administrador)

- `!uncritproc` = Eliminar el estado de proceso crítico (Se requieren privilegios de administrador)

- `!website` = Abrir un sitio web en el ordenador infectado  
  Sintaxis: `!website www.google.com`

- `!disabletaskmgr` = Deshabilitar el Administrador de Tareas (Se requieren privilegios de administrador)

- `!enabletaskmgr` = Habilitar el Administrador de Tareas (Se requieren privilegios de administrador)

- `!startup` = Agregar el programa al inicio

---

### Geolocalización y Comandos Varios:

- `!geolocate` = Geolocalizar el ordenador usando la latitud y longitud de la IP

- `!listprocess` = Listar todos los procesos

- `!infocounts` = Obtener información de las cuentas del sistema

- `!rootkit` = Lanzar un rootkit (Se requieren privilegios de administrador) 

- `!unrootkit` = Eliminar el rootkit (Se requieren privilegios de administrador) 

- `!getcams` = Listar los nombres de las cámaras

- `!selectcam` = Seleccionar una cámara para tomar una foto  
  Sintaxis: `!selectcam 1`

- `!webcampic` = Tomar una foto con la cámara web seleccionada

- `!myhelp` = Este menú de ayuda

### 2. **CompilerPYtoEXE.py**

- **Main Function**: Automatiza el proceso de configuración y compilación del bot en un archivo ejecutable **.exe**.
- **Process**:
    - Solicita al usuario el **Bot Token** y el **Server ID** (el ID del servidor de Discord).
    - Compila el archivo Python (`botConnect.py`) en un archivo EXE que se puede ejecutar en la máquina víctima.

### 3. **guiaAutoextraibleEXE.py**

- **Main Function**: Instrucciones detalladas sobre cómo empaquetar el archivo `.exe` con un archivo `fake_error.vbs` (que simula un error de Windows), la guía está en el script llamado `guiaAutoextraibleEXE.py`.
- **Goal**: Haga que el archivo `.exe` pase desapercibido empaquetándolo en un archivo **autoextraíble** que simula un error de Windows.

### 4. **ScriptSmartScreen**

- **Main Function**: Scripts que le permiten desactivar **SmartScreen** de Windows para evitar que el archivo ejecutable se bloquee.
- Includes:
    - **DuckyScript**: Para desactivar SmartScreen.
    - **PowerShell script**: Para desactivar SmartScreen automáticamente en la máquina víctima.

> NOTE:

For these 2 previous scripts ``social engineering`` sería necesario para que de alguna manera el usuario víctima ejecute al menos el script ``.ps1`` y así desactive el ``SmartScreen``.
### 5. **ExclusionWindowsDefender (Windows 11)**

- **Main Function**: Herramienta para evitar que **Windows Defender** detecte el archivo ejecutable como una amenaza.
- **Instructions**: Incluya un archivo `carpetaExcluidaWindowsDefender.ps1` para crear una carpeta excluida de los análisis de Windows Defender, asegurando que no se detecte el archivo ejecutable.

> NOTE:

Para este script de aquí, de la misma manera que antes, se tendría que hacer algún tipo de ``ingeniería social`` para que el usuario víctima ejecute dicho script y así genere una carpeta que evite ``Windows Defender`` donde está nuestro `` Se deposita `Trojan``. (En Windows 10 no se suele detectar como “Malware”)

---

## **Prerequisites**

Antes de ejecutar este proyecto, asegúrese de tener configurados los siguientes requisitos:

1. **Python 3.x**: Este proyecto está escrito en ``Python3``. Puedes instalarlo desde el siguiente enlace:
    
    - [Download Python3 from the Microsoft Store](https://apps.microsoft.com/detail/9NRWMJP3717K?hl=neutral&gl=ES&ocid=pdpshare)
    
1. **Dependencies**:
    
    - Este proyecto requiere varias bibliotecas ``Python`` que se instalarán automáticamente a través del archivo ``requirements.txt`.
    
    Para instalar las dependencias necesarias, simplemente ejecute el siguiente comando en su terminal:
	
	```
	pip install -r requirements.txt
	```
    
    Esto instalará todas las bibliotecas necesarias para que el proyecto funcione correctamente..
    

---

## **Project Use**

### 1. **Compilando el Bot con `CompilerPYtoEXE.py`**

The ``CompilerPYtoEXE.py`` El script automatiza el proceso de configuración del ``bot`` y de compilación del archivo **.exe**..

#### Steps to run **CompilerPYtoEXE.py**:

1. **Execute the `main.py`** script haciendo doble clic en él.
    
    - **Important**: **Nunca ejecute directamente el script `CompilerPYtoEXE.py`**, ya que hacerlo provocará que falle el proceso de compilación. El script `main.py` es responsable de ejecutar correctamente **CompilerPYtoEXE.py**.
    
2. **Provide bot data**:  

    El script abrirá una ventana de configuración donde deberás ingresar el **Bot Token** y el **Server ID**:
    
    - **Bot Token**: Puedes obtener este token desde el Portal ``Discord Developer``.
    - **Server ID**: Este es el ``ID`` del servidor ``Discord`` al que se conectará el bot. Para obtenerlo activa el modo desarrollador en ``Discord`` y haz clic derecho sobre el servidor para copiar su ``ID``.
    
3. **Select the `botConnect.py` file**:

    Una vez que su bot esté configurado, seleccione el archivo `botConnect.py` que desea usar para construir.
    
4. **Specifies the location of the compiled file**:  

    Después de seleccionar el archivo, se le pedirá que elija la ubicación donde desea guardar el archivo **.exe** compilado..
    
5. **Wait for the build to complete**:  

    El script generará el archivo **.exe** que puede ejecutar en la máquina víctima para que el bot se conecte al servidor ``Discord`` especificado..
    
### Practical video:

https://github.com/user-attachments/assets/d5e40b83-6d99-4d84-95ef-77d46511ccb9

---

### 2. **Bypass SmartScreen Lock**

#### 1. **DuckyScript**:

- **Function**: Deshabilite ``SmartScreen`` para que el archivo ``.exe`` no falle al ejecutarse.
- **Usage**: Simplemente ejecute ``DuckyScript`` en el entorno de la víctima para desactivar ``SmartScreen`` con un ``BadUSB``. (Aunque esto requiere tener la PC de la víctima a nivel físico)

#### 2. **PowerShell script (`ScriptSmartScreen` folder)**:

- A ``PowerShell`` Se incluye un script que desactiva ``SmartScreen`` automáticamente.
- **Run the PowerShell script** para evitar que ``SmartScreen`` bloquee la ejecución del archivo ``.exe`` generado. (Esta técnica requeriría "ingeniería social" para esto)

---

### 3. **Bypass Windows Defender Detection (Windows 11)**

En algunos casos, **Windows Defender** puede detectar el archivo ejecutable como una amenaza en ``Windows 11``. Para evitar esto, se incluyen herramientas para excluir el archivo ejecutable de los análisis de ``Windows Defender``.

#### Pasos para evitar la detección de Windows Defender:

1. **Ejecutar el script `carpetaExcluidaWindowsDefender.ps1`**:
    
    - Este script creará una carpeta que se excluirá de los análisis de ``Windows Defender``..
    - **Ejecute el script con PowerShell** para asegurarse de que la carpeta donde almacenará el archivo ``EXE`` no sea escaneada por ``Windows Defender``.
    
2. **Mueva el archivo .exe a la carpeta excluida**:
    
    - Después de ejecutar el script, mueva el archivo **.exe** generado a la carpeta que se excluyó de los análisis de ``Windows Defender``..

---

### 4. **Haga que el archivo `.exe` sea más realista**

Para que el archivo **.exe** pase desapercibido, se incluye el archivo `guiaAutoextraible.py`, que explica cómo crear un archivo **autoextraíble** con **WinRAR**.

#### Steps to package the `.exe` file as self-extracting:

1. **Prepare el archivo `.exe`** generado y el archivo `fake_error.vbs` (que simula un error de Windows).
2. Utilice **WinRAR** para empaquetar ambos archivos en un archivo **autoextraíble**.
3. El archivo autoextraíble se ejecutará y simulará un error de ``Windows``, haciendo que el bot pase desapercibido.

### Practical video:

https://github.com/user-attachments/assets/1f287107-ead9-4403-a1e7-63d565a0eddb

---

### 5. **Configuración del robot de discordia**

Para configurar el bot de Discord:

1. Ejecute el archivo `DiscordBotPage.bat` para ser redirigido a la página de configuración del bot en el **Portal para desarrolladores de Discord**.
2. Siga los pasos en la página para configurar el **Bot Token** y obtener los permisos necesarios para el bot en su servidor..

---

## **Advertencias y uso responsable**

Este proyecto está destinado a fines educativos y para pruebas de penetración en entornos controlados. **No utilices este proyecto sin el consentimiento explícito del propietario del sistema que estás controlando.** El uso no autorizado de este tipo de herramientas es ilegal y va en contra de los términos de servicio de Discord, así como de las leyes y regulaciones locales. internacional.

Este proyecto no debe utilizarse para actividades maliciosas o para comprometer sistemas sin el consentimiento de las partes involucradas..

---

## **Contribuciones**

Si desea contribuir al proyecto, abra una **solicitud de extracción** o informe cualquier problema en la sección **problemas** de este repositorio..