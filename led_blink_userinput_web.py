from flask import Flask, render_template, request
import RPi.GPIO as gp

gp.setmode(gp.BCM)

gp.setup(37, gp.OUT)

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        state = request.form['led']
        if state == 'on':
            gp.output(37, gp.HIGH)
        elif state == 'off':
            gp.output(37, gp.LOW)
        else:
            print('dengey')
        return render_template('index.html')
    else:
        return render_template('index.html')
  
if __name__ == '__main__':
    app.run(debug=True)

#the +ve end of LED must be connected to pin no 37 and -ve end to pin no 39(refer the pin diagram in the repository)
#create a html page with two buttons 'on' and 'off'
