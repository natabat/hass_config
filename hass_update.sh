#!/bin/bash

source /srv/homeassistant/bin/activate

cd ~/.homeassistant

git add .
git status
echo -n "Enter the Description for the Change: " [Minor Update]
read CHANGE_MSG
git commit -m "${CHANGE_MSG}"
git push origin master

exit
