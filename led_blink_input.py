import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BCM)

gp.setup(37, gp.OUT)

inp = int(input())

while 1 :
    if inp == 1:
        gp.output(gp.HIGH)
    elif inp == 0:
        gp.output(gp.LOW)
    else:
        print('dengey')
    inp = int(input())