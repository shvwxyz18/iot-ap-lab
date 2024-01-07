from max30102 import MAX30102
import time

sensor = MAX30102()

sensor.begin()

while True:
    heart_rate, spo2 = sensor.read_sensor()
    print("Heart Rate: {} bpm, SpO2: {}%".format(heart_rate, spo2))
    time.sleep(1)