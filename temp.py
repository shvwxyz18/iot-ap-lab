from w1thermsensor import W1ThermSensor
from time import sleep

sensor = W1ThermSensor()

while 1 :
    temp = sensor.get_temperature()
    print('Temperature is {}'.format(temp))
    sleep(1)

#the VCC must be connected to pin no 2, DATA must be connected to pin no 7 and GND to pin no 9
