# component_parrot_app

Intallation
===========

sudo apt install python3 idle3

pip install pydub  
sudo apt install python3-pydub

sudo apt-get install nodejs npm


Sudo apt-get install ffmpeg         //This allows play sound
sudo apt-get install libav-tools    //This allows play sound

sudo npm install socket.io          //This allows your Raspberry PI to send messages
sudo npm install socket.io-client   //This allows your Raspberry PI to hear messages from a Web server.

pip install "python-socketio[client]"       //https://python-socketio.readthedocs.io/en/latest/client.html#installation
export PATH="/home/raspberry/.local/bin:$PATH"
echo $PATH

IP static Configuration
=======================
*****dhcpcd.conf
ifconfig
nano /etc/dhcpcd.conf
sudo reboot

 inet 192.168.15.4  netmask 255.255.255.0  broadcast 192.168.15.255
 
******Interface
https://raspberrypi.stackexchange.com/questions/37920/how-do-i-set-up-networking-wifi-static-ip-address-on-raspbian-raspberry-pi-os

https://www.youtube.com/watch?v=oIrcatbj-UY

https://raspberrypi.stackexchange.com/questions/39785/differences-between-etc-dhcpcd-conf-and-etc-network-interfaces

https://raspberrypi.stackexchange.com/questions/37920/how-do-i-set-up-networking-wifi-static-ip-address-on-raspbian-raspberry-pi-os/37921#37921

route -n	 //para conocer datos del ip

/etc/network/interfaces

iface wlan0 inet static
   address 192.168.15.8
   netmask 255.255.255.0 
   network 192.168.15.0
   broadcast 192.168.15.255

You must edit /etc/NetworkManager/NetworkManager.conf
sudo nano /etc/NetworkManager/NetworkManager.conf
managed=true

Raspberry-screen
================
IP Lab 192.168.0.158
gateway 192.168.0.1
255.255.255.0

VNCViewer solution to wayvnc mistake
=====================================
0 preferencias-> raspberry config-> vnc,ssh

1 https://www.realvnc.com/en/blog/raspberry-pi-vnc/
sudo apt update
sudo apt upgrade
sudo apt install realvnc-vnc-server realvnc-vnc-viewer
sudo raspi-config

2 sudo nano .config/wayvnc/config
The file should content enable_auth=false
address=0.0.0.0
enable_auth=false
enable_pam=true
private_key_file=/home/pi/.config/wayvnc/key.pem
certificate_file=/home/pi/.config/wayvnc/cert.pem

3 outras que no funcionan

Update RaspberryPi
sudo apt-get update -y
sudo apt-get upgrade -y

https://github.com/raspberrypi/bookworm-feedback/issues/41#issuecomment-1780432322

D-Link
=======
Endereço IP
192.168.1.1
Subrede
255.255.255.0
Intervalo IP
192.168.1.2 ~ 192.168.1.11
gateway 192.168.0.1






