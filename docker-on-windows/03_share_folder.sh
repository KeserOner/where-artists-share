#!/bin/bash
set -e

# clear the MSYS MOTD
clear


echo "Configure Windows share (samba)"

echo "Docker Machine IP (192.168.99.XX):"
read IP
echo "Your directory shared (d):"
read DIR
echo "Your user name (user windows):"
read USER
echo "Your password (password windows):"
read PASSWORD

touch bootlocal.sh
echo "#!/bin/sh" > bootlocal.sh
echo "cd /tmp" >> bootlocal.sh
echo "su - docker -c 'tce-load -wi wget > /dev/null'" >> bootlocal.sh
echo "su - docker -c 'wget http://distro.ibiblio.org/tinycorelinux/5.x/x86/tcz/cifs-utils.tcz > /dev/null'" >> bootlocal.sh
echo "su - docker -c 'tce-load -i cifs-utils.tcz > /dev/null'" >> bootlocal.sh

echo "sudo mkdir -p /mnt/share > /dev/null" >> bootlocal.sh
#echo "sudo echo '//${IP}/${DIR}    /mnt/share        cifs    username=$USER,password=\"${PASSWORD}\",uid=1000,gid=1000 0 0' > /etc/fstab" >> bootlocal.sh
echo "sudo mount -t cifs //${IP}/${DIR} /mnt/share -o user=$USER,password=\"${PASSWORD}\",uid=1000,gid=1000,file_mode=0777,dir_mode=0777,wsize=65536,sec=ntlm > /dev/null" >> bootlocal.sh

echo "sudo touch /home/docker/.ashrc" >> bootlocal.sh

# echo "sudo echo 'alias docker-compose=\"docker run --rm -ti -v `pwd`:/app -v /var/run/docker.sock:/var/run/docker.sock dduportal/docker-compose:latest\"' >> /home/docker/.ashrc" >> bootlocal.sh
# echo "sudo echo 'alias fig=docker-compose' >> /home/docker/.ashrc" >> bootlocal.sh
echo "su - docker -c 'cd /tmp && tce-load -wi python && curl -O https://bootstrap.pypa.io/get-pip.py && sudo python get-pip.py && curl -O https://bootstrap.pypa.io/ez_setup.py && sudo python ez_setup.py && sudo pip install -U docker-compose==1.3.1'" >> bootlocal.sh
#echo "sudo echo 'alias composer=\"docker run --rm -it -v \`pwd\`:/app composer/composer\"' >> /home/docker/.ashrc" >> bootlocal.sh
#echo "sudo echo 'alias symfony=\"docker run --rm -i -t -u \`id -u\` -v \`pwd\`:/src romqin/symfony-installer\"' >> /home/docker/.ashrc" >> bootlocal.sh

