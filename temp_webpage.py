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