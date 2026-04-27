$projectDir = (Get-Item (Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) ".")).FullName
$workspaceDir = Split-Path -Parent $projectDir
$renpyExe = Join-Path $workspaceDir "renpy-8.5.2-sdk\renpy.exe"

if (-not (Test-Path -LiteralPath $renpyExe)) {
    Write-Host "RenPy not found:"
    Write-Host $renpyExe
    Read-Host "Press Enter to exit"
    exit 1
}

Start-Process -FilePath $renpyExe -ArgumentList @($projectDir, "run")
