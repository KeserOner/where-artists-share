#!/bin/bash
set -e

echo "Installation Docker Client..."
if [ ! -e "/bin/docker" ]; then
   curl -L -k "https://get.docker.com/builds/Windows/x86_64/docker-latest.exe" > /bin/docker
fi

echo "Installation Docker Machine..."
if [ ! -e "/bin/docker-machine" ]; then
   curl -L -k "https://github.com/docker/machine/releases/download/v0.3.0/docker-machine_windows-amd64.exe" > /bin/docker-machine
fi
