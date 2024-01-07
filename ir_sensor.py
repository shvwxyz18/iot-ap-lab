import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BCM)

gp.setup(18, gp.OUT)
gp.setup(16, gp.IN)

while 1:
    inp = gp.input(16)
    if inp:
        gp.output(gp.HIGH)
    else :
        gp.output(gp.LOW)
    sleep(1)