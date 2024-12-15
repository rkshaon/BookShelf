#!/bin/bash

# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m'  # No Color (reset to default)
RESET='\033[0m'  # No Color (reset to default)

echo -e "${GREEN}Deployment proces start...${RESET}"
echo -e "${BLUE}Pull the latest code from GitHub${RESET}"
echo -e "${YELLOW}=======================================${RESET}"

sudo git pull origin master

echo -e "${BLUE}Navigate to the FRONTEND directory${RESET}"
echo -e "${YELLOW}=======================================${RESET}"
cd /var/www/bookshelf.rkshaon.info/frontend

pwd

echo -e "${BLUE}Install Dependencies${RESET}"
echo -e "${YELLOW}=======================================${RESET}"
sudo npm install --legacy-peer-deps

echo -e "${BLUE}Building${RESET}"
echo -e "${YELLOW}=======================================${RESET}"
sudo npm run build

echo -e "${BLUE}Navigate to the BACKEND directory${RESET}"
echo -e "${YELLOW}=======================================${RESET}"
cd /var/www/bookshelf.rkshaon.info/backend

pwd

echo -e "${BLUE}Activating Virtual Environment${RESET}"
echo -e "${YELLOW}=======================================${RESET}"
source env/bin/activate
pip install -r requirements.txt

echo -e "${BLUE}Migrating${RESET}"
echo -e "${YELLOW}=======================================${RESET}"
python manage.py migrate


echo -e "${BLUE}Restart Backend Gunicorn Service${RESET}"
echo -e "${YELLOW}=======================================${RESET}"
systemctl restart gunicorn-bookshelf.service 
systemctl restart celery_bookshelf.service
systemctl restart celery_bookshelf_beat.service

echo -e "${RED}Finish${RESET}..."
