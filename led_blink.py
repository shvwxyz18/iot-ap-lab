import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BCM)

gp.setup(37, gp.OUT)

while 1 :
    gp.output(gp.HIGH)
    sleep(1)
    gp.output(gp.LOW)
    sleep(1)

#the +ve end of LED must be connected to pin no 37 and -ve end to pin no 39(refer the pin diagram in the repository)
