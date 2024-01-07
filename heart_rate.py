from max30102 import MAX30102
import time

sensor = MAX30102()

sensor.begin()

while True:
    heart_rate, spo2 = sensor.read_sensor()
    print("Heart Rate: {} bpm, SpO2: {}%".format(heart_rate, spo2))
    time.sleep(1)

#the two SDA pin must be connected to pin no 3 and 5, VIN must be connected to pin no 4 and GND to pin no 6 i.e., the pins are connected only in between 3, 4, 5 and 6
#refer the pin diagram for more clarity
#for the max30102 sensor pin diagram refer max30102.png
