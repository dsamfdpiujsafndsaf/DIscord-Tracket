# Comprobar si el script se está ejecutando como administrador
If (-Not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "Este script debe ejecutarse con privilegios de administrador." -ForegroundColor Red
    Start-Process powershell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    Exit
}

# Ruta del Registro de SmartScreen
$regPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer"

# Comprobar si la clave existe
If (Test-Path $regPath) {
    # Cambiar el valor de SmartScreenEnabled a "Off"
    Set-ItemProperty -Path $regPath -Name "SmartScreenEnabled" -Value "Off"
    Write-Host "SmartScreen desactivado con éxito." -ForegroundColor Green
} Else {
    Write-Host "No se encontró la clave de SmartScreen en el registro." -ForegroundColor Yellow
}
