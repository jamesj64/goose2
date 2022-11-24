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

ultrasonic = Ultrasonic()

bState = False

class Servo:
    def __init__(self):
        self.PwmServo = PCA9685(0x40, debug=True)
    def setServoPwm(self,channel,angle,error=10):
        angle=int(angle)
        if channel=='2':
            self.PwmServo.setServoPulse(10,500+int((angle+error)/0.09))

GPIO.setwarnings(False)
Buzzer_Pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(Buzzer_Pin,GPIO.OUT)

def stopMovement():
    PWM.setMotorModel(0,0,0,0)
    print("stopMovement")

def moveForward():
    PWM.setMotorModel(1000,1000,1000,1000)
    print("moveForward")

def moveRight():
    PWM.setMotorModel(1400,1400,-1050,-1050)
    print("moveRight")

def moveLeft():
    PWM.setMotorModel(-1050,-1050,1400,1400)
    print("moveLeft")

def moveBackward():
    PWM.setMotorModel(-1000,-1000,-1000,-1000)
    print("moveBackward")

def poop():
    servoThing = Servo()
    servoThing.setServoPwm('2',0)
    servoThing.setServoPwm('2',100)
    time.sleep(0.1)
    servoThing.setServoPwm('2',0)

app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")

@app.route("/", methods = ['POST', 'GET'])
def hello_world():
    global bState
    if request.method == 'POST':
        content = request.form
        if content['moveForward'] == "1":
            moveForward()
        if content['moveBackward'] == "1":
            moveBackward()
        if content['stopMovement'] == "1":
            stopMovement()
        if content['moveRight'] == "1":
            moveRight()
        if content['moveLeft'] == '1':
            moveLeft()
        if content['buzzer'] == "1":
            bState = not bState
        if content['getDistance'] == "1":
            print(ultrasonic.get_distance())
            return jsonify({"distance": ultrasonic.get_distance()}), 200
        if content['poop'] == "1":
            print("poop")
            poop()
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
    print("exit")
    GPIO.cleanup()
    GPIO.output(Buzzer_Pin,GPIO.LOW)
    PWM.setMotorModel(0,0,0,0)

atexit.register(exit_handler)
