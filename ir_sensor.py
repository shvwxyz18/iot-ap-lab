import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BCM)

gp.setup(37, gp.OUT)
gp.setup(16, gp.IN)

while 1:
    inp = gp.input(16)
    if inp:
        gp.output(gp.HIGH)
    else :
        gp.output(gp.LOW)
    sleep(1)

#the +ve end of LED must be connected to pin no 37 and -ve end to pin no 39(refer the pin diagram in the repository)
#the data of ir sensor must be connected to pin no 16, GND to no 6 and VCC to pin no 4
