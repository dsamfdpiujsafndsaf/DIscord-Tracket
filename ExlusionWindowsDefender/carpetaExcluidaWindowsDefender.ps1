# Obtener el directorio donde se está ejecutando el script
$currentDir = Get-Location

# Nombre de la carpeta a crear
$folderName = "Excluido"  # Cambia esto si deseas un nombre diferente

# Ruta completa de la carpeta que se va a crear
$exclusionPath = Join-Path -Path $currentDir -ChildPath $folderName

# Crear la carpeta si no existe
If (-Not (Test-Path -Path $exclusionPath)) {
    New-Item -Path $exclusionPath -ItemType Directory -Force
    Write-Host "Carpeta '$exclusionPath' creada." -ForegroundColor Green
} Else {
    Write-Host "La carpeta '$exclusionPath' ya existe." -ForegroundColor Yellow
}

# Agregar la carpeta a las exclusiones de Windows Defender
Add-MpPreference -ExclusionPath $exclusionPath
Write-Host "Carpeta '$exclusionPath' agregada a las exclusiones de Windows Defender." -ForegroundColor Green
