import serial
import time
from datetime import datetime

# Use COM3 as per your Arduino setup
ser = serial.Serial('COM3', 9600)
print("Connected to Arduino on COM3.")

# Define your scheduled times (HH:MM format)
on_time = "14:24"
off_time = "14:25"

while True:
    now = datetime.now().strftime('%H:%M')
    print(f"Current time: {now}")

    if now == on_time:
        ser.write(b'1')  # Turn relay ON
        print("Relay ON")
    elif now == off_time:
        ser.write(b'0')  # Turn relay OFF
        print("Relay OFF")

    time.sleep(30)
