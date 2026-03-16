Write-Host "Iniciando proceso de subida a Git..." -ForegroundColor Cyan
cd C:\Users\Charlie\Documents\DAW\DAW
# 1. AÒadir todos los cambios al staging area
Write-Host "Paso 1: AÒadiendo archivos (git add .)" -ForegroundColor Yellow
git add .

# Comprobar si realmente hay cambios para hacer commit
$cambios = git status --porcelain
if ($cambios) {
    
    # ¬°AQU√ç EST√Å LA MAGIA INTERACTIVA!
    # El script se pausar√° y te pedir√° que escribas el motivo
    $mensaje = Read-Host "Xoxoè por favor, escribe el motivo del commit"
    
    # Por si le das al Enter sin querer sin escribir nada, le ponemos un salvavidas
    if ([string]::IsNullOrWhiteSpace($mensaje)) {
        $mensaje = "Actualizacion de codigo sin descripcion"
        Write-Host "No escribiste nada, usando mensaje por defecto..." -ForegroundColor DarkYellow
    }
    
    # 2. Hacer el commit con tu mensaje
    Write-Host "Paso 2: Creando commit..." -ForegroundColor Yellow
    git commit -m $mensaje
    
    # 3. Subir al repositorio remoto
    Write-Host "Paso 3: Subiendo al servidor (git push)..." -ForegroundColor Yellow
    git push
    
    Write-Host "°Todos los cambios se han subido con exito, xoxo!" -ForegroundColor Green
    
} else {
    Write-Host "No hay ningun cambio nuevo para subir. Todo esta al dia." -ForegroundColor Red
}
Read-Host "Presiona Enter para cerrar esta ventana..."