' Buscaminas en VBScript simplificado

' Inicialización del juego
Dim tablero(5, 5)
Dim minas(5, 5)
Dim i, j, fila, columna
Dim mina_count, max_minhas, game_over

' Configuración
max_minhas = 5
mina_count = 0
game_over = False

' Inicializar el tablero (sin minas)
For i = 0 To 5
    For j = 0 To 5
        tablero(i, j) = 0
    Next
Next

' Colocar minas aleatoriamente
Do While mina_count < max_minhas
    fila = Int(Rnd * 5)
    columna = Int(Rnd * 5)
    If minas(fila, columna) = 0 Then
        minas(fila, columna) = 1
        mina_count = mina_count + 1
    End If
Loop

' Mostrar instrucciones
MsgBox "Bienvenido al Buscaminas! Tienes que evitar las minas. Usa las coordenadas (fila,columna) para seleccionar.", vbInformation, "Instrucciones"

' Función para verificar si la celda seleccionada es una mina
Function EsMina(fila, columna)
    If minas(fila, columna) = 1 Then
        EsMina = True
    Else
        EsMina = False
    End If
End Function

' Bucle principal del juego
Do While Not game_over
    ' Pedir al jugador las coordenadas de la celda
    fila = InputBox("Ingresa la fila (0-5):", "Selección de fila")
    columna = InputBox("Ingresa la columna (0-5):", "Selección de columna")
    
    ' Validar entradas (asegúrate de que sean números)
    If IsNumeric(fila) And IsNumeric(columna) Then
        fila = CInt(fila)
        columna = CInt(columna)
        
        ' Validar si las coordenadas están en el rango correcto
        If fila < 0 Or fila > 5 Or columna < 0 Or columna > 5 Then
            MsgBox "Las coordenadas deben estar entre 0 y 5. Intenta de nuevo.", vbExclamation, "Error"
        Else
            ' Verificar si el jugador ha seleccionado una mina
            If EsMina(fila, columna) Then
                MsgBox "¡BOOM! Has pisado una mina. Fin del juego.", vbCritical, "Perdiste"
                game_over = True
            Else
                MsgBox "¡Bien hecho! No es una mina. Sigue buscando.", vbInformation, "Seguir jugando"
            End If
        End If
    Else
        MsgBox "Por favor ingresa números válidos para la fila y la columna.", vbExclamation, "Error de entrada"
    End If
Loop

MsgBox "Fin del juego", vbInformation, "Game Over"
