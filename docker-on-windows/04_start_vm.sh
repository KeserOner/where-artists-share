#!/bin/bash
set -e

# clear the MSYS MOTD
clear
VM=$1

echo "Demarrage de la VM."
docker-machine start $VM

echo "Copie du fichier de demarrage dans la VM : $VM"
docker-machine scp ./bootlocal.sh $VM:/home/docker/bootlocal.sh

echo "Copie du fichier de demarrage dans le boot"
docker-machine ssh $VM "cd /home/docker; sudo dos2unix bootlocal.sh; sudo cp /home/docker/bootlocal.sh /var/lib/boot2docker/bootlocal.sh; sudo chmod +x /var/lib/boot2docker/bootlocal.sh"
echo "Redemarrage de la VM $VM"
docker-machine stop $VM
docker-machine start $VM
