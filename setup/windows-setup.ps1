<#
Author:     Daniyal
LinkedIn:   https://www.linkedin.com/in/daniyal-automation/
GitHub:     https://github.com/syed-daniyalH
Version:    26.01.20.5.08
#>

# Check if Python is installed
try {
    $pyCheck = python --version 2>&1
    if ($null -eq $pyCheck) { throw }
} catch {
    Write-Host "Python is not installed. Please install Python 3.10+ and add it to PATH." -ForegroundColor Red
    Write-Host "Download: https://www.python.org/downloads/"
    Read-Host -Prompt "Press Enter to exit"
    exit
}

Write-Host "Python is installed: $pyCheck" -ForegroundColor Green

# Check if Google Chrome is installed
$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
if (-not (Test-Path $chromePath)) {
    Write-Host "Google Chrome not found in the default location." -ForegroundColor Yellow
    Write-Host "Download: https://www.google.com/chrome/"
    Read-Host -Prompt "Press Enter to exit"
    exit
}

Write-Host "Google Chrome found." -ForegroundColor Green

# Install required Python packages
Write-Host "Installing dependencies..." -ForegroundColor Cyan
pip install selenium undetected-chromedriver pyautogui flask flask-cors openai

# Get the latest ChromeDriver version
Write-Host "Fetching ChromeDriver version..." -ForegroundColor Cyan
$jsonDownload = Invoke-RestMethod -Uri "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"
$downloadUrl = ($jsonDownload.channels.Stable.downloads.chromedriver | Where-Object { $_.platform -eq "win64" }).url

if (-not $downloadUrl) {
    Write-Host "Could not find a valid download URL." -ForegroundColor Red
    exit
}

Write-Host "Downloading ChromeDriver from: $downloadUrl" -ForegroundColor Cyan
Invoke-WebRequest -Uri $downloadUrl -OutFile "chromedriver.zip"

# Extraction
Write-Host "Extracting..." -ForegroundColor Cyan
Expand-Archive -Path "chromedriver.zip" -DestinationPath "$PWD\chromedriver" -Force
Remove-Item -Path "chromedriver.zip"

Write-Host "Setup complete. Visit https://github.com/syed-daniyalH for updates." -ForegroundColor Green
Read-Host -Prompt "Press Enter to continue..."
