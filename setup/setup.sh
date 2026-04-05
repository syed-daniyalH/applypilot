#!/bin/bash
'''
Author:     Daniyal
LinkedIn:   https://www.linkedin.com/in/daniyal-automation/
GitHub:     https://github.com/syed-daniyalH
Version:    26.01.20.5.08
'''

# Check if Python is installed
if ! (python3 -V &> /dev/null || python -V &> /dev/null); then
    echo "Python is not installed. Please install Python 3.10 or above and add it to PATH."
    exit 1
fi

# Step 1: Get the JSON data for Chrome for Testing
echo "Fetching latest ChromeDriver information..."
latest_versions_info=$(curl -sS "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json")

# Step 2: Get the download URL for the current platform (defaulting to linux64 for .sh)
# Note: This is an automated setup script example
download_url=$(echo "$latest_versions_info" | grep -A 5 '"platform": "linux64",' | grep 'url":' | awk -F'"' '{print $4}')

if [ -z "$download_url" ]; then
    echo "Could not find a valid download URL for your platform."
    exit 1
fi

echo "Downloading ChromeDriver from: $download_url"
curl -o chromedriver.zip "$download_url"

# Step 3: Extract
echo "Extracting ChromeDriver..."
unzip -q chromedriver.zip
# Cleanup zip
rm chromedriver.zip

echo "Setup complete. Please ensure the chromedriver binary is in your PATH."
echo "Visit https://github.com/syed-daniyalH for support."
