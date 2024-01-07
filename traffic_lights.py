from gpiozero import TrafficLights
from time import sleep

traffic_lights = TrafficLights(16, 18, 37) #red, yellow, green

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

#red LED must be connected as +ve -> 16 and -ve -> 14
#amber/yellow LED must be connected as +ve -> 18 and -ve -> 20
#green LED must be connected as +ve -> 37 and -ve -> 39
