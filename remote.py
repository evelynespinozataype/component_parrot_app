#connection from AI_EEG to Aquarela
import socketio
from main import *
# Create a SocketIO client instance
sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('Connected to server')

@sio.on('disconnect')
def on_disconnect():
    print('Disconnected from server')

# Establishing a SocketIO connection to Aquarela server
sio.connect('http://192.168.15.4:3000',namespaces=['/remote'])

print('connecting with remote Aquarela')

# Emit to the server Aquarela
parrot_flag = 1  # happy=1, sad=0
sio.emit('join_component_parrot', parrot_flag, namespace ='/remote')

# Function ECG to send the Flag of emotional state in HeartRate
def sendValueToAquarela(parrot_flag):
    parrot_flag = 1  # happy=1, sad=0
    sio.emit('join_component_parrot', parrot_flag)

@sio.on('join_component_aquarela', namespace = '/remote')
def receiveValueToAquarela(data):
    print('Connected to AQUARELA')
    happy_emotion(1)

@sio.on('feedback_parrot_sound')
def receiveValueToAquarelaSound(data):
    print('Connected to AQUARELA')
    happy_emotion(1)

# Wait for a moment to allow the event to be sent
#sio.sleep(2)

# Disconnect from the server
#sio.disconnect()
