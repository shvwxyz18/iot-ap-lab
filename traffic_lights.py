from gpiozero import TrafficLights
from time import sleep

traffic_lights = TrafficLights(14, 16, 37) #red, yellow, green

while True:
    traffic_lights.green.on()
    sleep(2)
    traffic_lights.green.off()

    traffic_lights.amber.on()
    sleep(2)
    traffic_lights.amber.off()

    traffic_lights.red.on()
    sleep(2)
    traffic_lights.red.off()
    sleep(2)  
