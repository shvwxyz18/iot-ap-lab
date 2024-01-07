from w1thermsensor import W1ThermSensor
from time import sleep

sensor = W1ThermSensor()

while 1 :
    temp = sensor.get_temperature()
    print('Temperature is {}'.format(temp))
    sleep(1)