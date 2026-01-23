<#
.SYNOPSIS
    Extracts PDF files from P7M containers.

.DESCRIPTION
    This script scans for .p7m files in the specified directory (or current directory if none provided) and extracts the embedded PDF.
    Supports -Path and optional -Recurse parameters.

.PARAMETER Path
    The directory path to scan for .p7m files. Defaults to the script's directory.

.PARAMETER Recurse
    If specified, recursively scans subdirectories for .p7m files.

.PARAMETER Verbose
    If specified, provides detailed processing information in tabular format.

.NOTES
    Version: 0.2.0
    Author: Marcello Anselmi Tamburini

.CHANGELOG
    0.2.0 - Added -Verbose parameter for tabular output.
    0.1.0 - Initial release.

#>

param(
    [Parameter(Mandatory=$false)]
    [ValidateScript({Test-Path $_ -PathType Container})]
    [string]$Path = $PSScriptRoot,
    [Parameter(Mandatory=$false)]
    [switch]$Recurse = $false,
    [Parameter(Mandatory=$false)]
    [switch]$Verbose = $false
)

$files = Get-ChildItem $Path -Filter *.p7m -Recurse:$Recurse
$totalFiles = $files.Count
$currentIndex = 0
$results = @()

$files | ForEach-Object {
    $currentIndex++
    Write-Progress -Activity "Extracting PDFs from P7M files" -Status "Processing $($_.Name)" -PercentComplete (($currentIndex / $totalFiles) * 100) -CurrentOperation "Scanning for PDF header..."

    $bytes = [IO.File]::ReadAllBytes($_.FullName)
    $magic = [byte[]](0x25,0x50,0x44,0x46,0x2D)
    $offset = [Array]::IndexOf($bytes,$magic[0])

    while ($offset -ge 0 -and $offset -lt $bytes.Length-5) {
        if ($bytes[$offset+1] -eq $magic[1] -and
            $bytes[$offset+2] -eq $magic[2] -and
            $bytes[$offset+3] -eq $magic[3] -and
            $bytes[$offset+4] -eq $magic[4]) { break }
        $offset = [Array]::IndexOf($bytes,$magic[0],$offset+1)
    }

    if ($offset -ge 0) {
        Write-Progress -Activity "Extracting PDFs from P7M files" -Status "Processing $($_.Name)" -PercentComplete (($currentIndex / $totalFiles) * 100) -CurrentOperation "Extracting PDF..."
        $out = $_.FullName -replace '\.p7m$','.pdf'
        [IO.File]::WriteAllBytes($out,$bytes[$offset..($bytes.Length-1)])
        $size = (Get-Item $out).Length
        $result = [PSCustomObject]@{
            FileName = $_.Name
            Status = "Extracted"
            OutputFile = $out
            Size = $size
        }
        $results += $result
        if (!$Verbose) { Write-Host "OK $($_.Name)" }
    }
    else {
        Write-Progress -Activity "Extracting PDFs from P7M files" -Status "Processing $($_.Name)" -PercentComplete (($currentIndex / $totalFiles) * 100) -CurrentOperation "No PDF found"
        $result = [PSCustomObject]@{
            FileName = $_.Name
            Status = "No PDF found"
            OutputFile = $null
            Size = $null
        }
        $results += $result
        if (!$Verbose) { Write-Warning "NO PDF in $($_.Name)" }
    }
}

Write-Progress -Activity "Extracting PDFs from P7M files" -Completed

if ($Verbose) {
    $results | Format-Table -AutoSize
}
