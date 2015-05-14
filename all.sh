#!/usr/bin/env bash

echo $(tput setaf 1) #red
python ./civiweb.py
echo $(tput setaf 2) #green
python ./gemalto.py
echo $(tput setaf 3) #yellow
python ./goalsystems.py
echo $(tput setaf 5) #pink
python ./coordinationsud.py
echo $(tput setaf 6) #blue
python ./asalf.py

echo $(tput sgr0) #reset

read -p "Press [Enter] key to exit"



