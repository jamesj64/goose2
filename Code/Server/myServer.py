#flask run --app myServer run --host=0.0.0.0 
#flask run --app myServer run

from flask import Flask
from flask import render_template, make_response
from flask import redirect, request, jsonify, url_for
import RPi.GPIO as GPIO
import os
import time
from Motor import *
from servo import *
from Ultrasonic import *
from PCA9685 import PCA9685
from random import *
import atexit

bState = False


GPIO.setwarnings(False)
Buzzer_Pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(Buzzer_Pin,GPIO.OUT)

def stopMovement():
    PWM.setMotorModel(0,0,0,0)

def moveForward():
    PWM.setMotorModel(500,500,500,500)

app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")

@app.route("/", methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        content = request.form
        #bState = True if content['buzzer'] == "0" else False
        if content['moveForward'] == "1":
            moveForward()
        if content['stopMovement'] == "1":
            stopMovement()
        if content['buzzer'] == "1":
            bState = not bState
        if bState:
            GPIO.output(Buzzer_Pin,GPIO.HIGH)
            print("buzz on \n")
        else:
            GPIO.output(Buzzer_Pin,GPIO.LOW)
            print("buzz off \n")
        return ""
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

def exit_handler():
    GPIO.cleanup()
    GPIO.output(Buzzer_Pin,GPIO.LOW)
    PWM.setMotorModel(0,0,0,0)
