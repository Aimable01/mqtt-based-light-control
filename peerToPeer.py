import paho.mqtt.client as mqtt
import serial

# Serial setup for Arduino
ser = serial.Serial('COM4', 9600)

# MQTT setup
broker = "157.173.101.159"
port = 1883
topic = "relay/wigo"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker.")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    payload = msg.payload.decode().strip()
    print(f"Received MQTT message: {payload}")
    if payload == "1":
        ser.write(b'1')  # Turn relay ON
        print("Relay ON")
    elif payload == "0":
        ser.write(b'0')  # Turn relay OFF
        print("Relay OFF")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)
client.loop_forever()
