# component_parrot_app

Intallation
===========
pip install pydub

Sudo apt-get install ffmpeg         //This allows play sound
sudo apt-get install libav-tools    //This allows play sound

sudo npm install socket.io          //This allows your Raspberry PI to send messages
sudo npm install socket.io-client   //This allows your Raspberry PI to hear messages from a Web server.

pip install "python-socketio[client]"       //https://python-socketio.readthedocs.io/en/latest/client.html#installation
export PATH="/home/raspberry/.local/bin:$PATH"
echo $PATH

IP static Configuration
=======================
ifconfig
nano /etc/dhcpcd.conf
sudo reboot

Raspberry-screen
================
IP Lab 192.168.0.158
gateway 192.168.0.1
255.255.255.0

D-Link
=======
Endereço IP
192.168.1.1
Subrede
255.255.255.0
Intervalo IP
192.168.1.2 ~ 192.168.1.11
gateway 192.168.0.1






