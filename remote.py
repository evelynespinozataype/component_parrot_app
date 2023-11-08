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
sio.connect('http://192.168.15.5:3000',namespaces=['/remotep'])

print('connecting with remote Aquarela')

# Emit to the server Aquarela
parrot_flag = 1  # happy=1, sad=0
sio.emit('join_component_parrot', parrot_flag, namespace ='/remotep')

# Function ECG to send the Flag of emotional state in HeartRate
def sendValueToAquarela(parrot_flag):
    parrot_flag = 1  # happy=1, sad=0
    sio.emit('join_component_parrot', parrot_flag, namespace ='/remotep')

@sio.on('join_component_aquarela', namespace = '/remotep')
def receiveValueToAquarela(data):
    print('Connected to AQUARELA')
    start_parrot()

@sio.on('feedback_parrot_sound', namespace = '/remotep')
def receiveValueToAquarelaSound(data):
    print('QR emotion AQUARELA',data)
    emotion(data)

@sio.on('feedback_parrot_interaction', namespace = '/remotep')
def receive_QRAquarela(data):
    print('QR interaction Aquarela', data)
    interaction(data)

# Wait for a moment to allow the event to be sent
#sio.sleep(2)

# Disconnect from the server
#sio.disconnect()
