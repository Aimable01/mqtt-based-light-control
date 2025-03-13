# MQTT-Based Light Control System

A simple web-based application that allows controlling a virtual light via MQTT. The system consists of two components:

1. **Web Interface**: A browser-based UI with buttons to turn the light on and off
2. **IoT Device Simulator**: A Python script that simulates an ESP8266 device

## Components

### Web Interface (index.html)
A simple HTML page with JavaScript that:
- Connects to a public MQTT broker via WebSockets
- Provides "Turn ON" and "Turn OFF" buttons
- Displays the current light status
- Publishes messages to the MQTT topic `/student_group/light_control`

### IoT Device Simulator (light_simulation.py)
A Python script that:
- Connects to the same MQTT broker
- Subscribes to the `/student_group/light_control` topic
- Prints the light status whenever a message is received

## How to Run

### Step 1: Start the IoT Device Simulator
1. Ensure you have Python installed
2. Install the required MQTT client library:
   ```
   pip install paho-mqtt
   ```
3. Run the simulator:
   ```
   python mqtt_light_control.py
   ```

### Step 2: Open the Web Interface
1. Open `index.html` in a web browser
2. Wait for the connection status to show "Connected"
3. Click the "Turn ON" or "Turn OFF" buttons to control the light

### Step 3: Observe the Simulator
The Python script will print messages showing the light status changes as you click the buttons on the web interface.

## Technical Details

- **MQTT Broker**: Uses the public broker at broker.emqx.io
- **Topic**: `/student_group/light_control`
- **Message Format**: Simple text strings "ON" or "OFF"
- **Web Client**: Uses MQTT.js library over WebSockets (WSS)
- **IoT Simulator**: Uses the Paho MQTT Python client

## Requirements

- Python 3.6+
- Paho MQTT Python client
- Web browser with JavaScript enabled