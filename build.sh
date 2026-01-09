#!/bin/bash

# Main Python script name
SCRIPT_NAME="main.py"

APP_NAME="my_app"

# PyInstaller options
ONEFILE="--onefile"  # Creates a single executable file
# ONEDIR="--onedir"  # Alternative: creates a folder with dependencies

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build dist *.spec

# Check if PyInstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "PyInstaller not found. Installing..."
    pip install pyinstaller
fi

# Create the executable
echo "Creating executable with PyInstaller..."
pyinstaller $ONEFILE \
    --name "$APP_NAME" \
    --clean \
    --noconfirm \
    "$SCRIPT_NAME"

# Check the result
if [ $? -eq 0 ]; then
    echo "Executable successfully created at: dist/$APP_NAME"
else
    echo "Error creating executable"
    exit 1
fi
