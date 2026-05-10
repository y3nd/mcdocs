# powershell -NoProfile -ExecutionPolicy Bypass -File convert-to-avif.ps1 -InputPath "."

param(
    [Parameter(Mandatory = $true)]
    [string]$InputPath,

    [int]$MaxSide = 800,

    [int]$CRF = 35,

    [switch]$Overwrite
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
    throw "ffmpeg not found in PATH."
}

if (-not (Test-Path -LiteralPath $InputPath)) {
    throw "Input path does not exist: $InputPath"
}

$InputRoot = (Resolve-Path -LiteralPath $InputPath).Path

$files = Get-ChildItem -LiteralPath $InputRoot -Recurse -File |
    Where-Object { $_.Extension -match '^\.(jpe?g|png|gif|webp)$' }

if (-not $files) {
    Write-Host "No supported image files found under: $InputRoot"
    exit 0
}

foreach ($file in $files) {
    $targetFile = Join-Path $file.DirectoryName ($file.BaseName + ".avif")

    # Skip if already converted, unless -Overwrite is used
    if ((Test-Path -LiteralPath $targetFile) -and -not $Overwrite) {
        Write-Host "Skipping already converted: $($file.FullName)"
        continue
    }

    Write-Host "Converting: $($file.FullName)"

    # Resize to max side, avoid upscaling, then flatten transparency onto white.
    $filter = "[0:v]scale='trunc(iw*min(1,min(${MaxSide}/iw,${MaxSide}/ih))/2)*2':'trunc(ih*min(1,min(${MaxSide}/iw,${MaxSide}/ih))/2)*2':in_range=pc:out_range=tv,format=rgba,split[fg][bg];[bg]drawbox=x=0:y=0:w=iw:h=ih:color=white:t=fill[bgw];[bgw][fg]overlay,format=yuv420p"

    $args = @(
        if ($Overwrite) { "-y" } else { "-n" }
        "-i", $file.FullName
        "-filter_complex", $filter
        "-frames:v", "1"
        "-c:v", "libaom-av1"
        "-still-picture", "1"
        "-crf", $CRF
        "-b:v", "0"
        "-pix_fmt", "yuv420p"
        $targetFile
    ) | Where-Object { $_ }

    & ffmpeg @args

    if ($LASTEXITCODE -ne 0) {
        Write-Warning "ffmpeg failed for: $($file.FullName)"
    }
}

Write-Host "Done."