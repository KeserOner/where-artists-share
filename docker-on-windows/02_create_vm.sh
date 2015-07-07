#!/bin/bash
set -e

echo "### VM ###"
echo "Nom de la VM:"
read VM

echo "Creation Docker VM..."
MEM=`wmic memorychip get capacity | grep -v "Capacity" | awk '{sum+=$1} END {print sum/1024/1024/2}'`

docker-machine create $VM --virtualbox-cpu-count "-1" --virtualbox-memory "$MEM" --driver virtualbox 

echo "Mise a jour des ENVVARS"
eval "$(docker-machine env $VM)"
