from flask import Flask
from w1thermsensor import W1ThermSensor
from time import sleep

sensor = W1ThermSensor()
app = Flask(__name__)

@app.route('/')
def home():
    temp = sensor.get_temperature()
    return 'temp: {} degree C'.format(temp)

if __name__ == '__main__':
    app.run(debug = True)

#the VCC must be connected to pin no 2, DATA must be connected to pin no 7 and GND to pin no 9
#no need to create an 'index.html' file, the return will do it on its own
