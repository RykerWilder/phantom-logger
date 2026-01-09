#!/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'


# Main Python script name
SCRIPT_NAME="main.py"


# Ask user for executable name
echo -e -n "${GREEN}Enter the name for the executable: ${NC}"
read APP_NAME


# Use default name if input is empty
if [ -z "$APP_NAME" ]; then
    APP_NAME="cache.log"
    echo -e "${YELLOW}No name provided. Using default: $APP_NAME${NC}"
fi


# PyInstaller options
ONEFILE="--onefile"  # Creates a single executable file
# ONEDIR="--onedir"  # Alternative: creates a folder with dependencies


# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build dist *.spec


# Create the executable
echo "Creating executable with PyInstaller..."
pyinstaller $ONEFILE \
    --name "$APP_NAME" \
    --clean \
    --noconfirm \
    "$SCRIPT_NAME"


# Check the result
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Executable successfully created at: dist/$APP_NAME${NC}"
else
    echo -e "${RED}Error creating executable${NC}"
    exit 1
fi
