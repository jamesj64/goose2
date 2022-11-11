import io
import os
import socket
import struct
import time
import picamera2
from Motor import *
import RPi.GPIO as GPIO
from servo import *
from PCA9685 import PCA9685
from Ultrasonic import *
from Buzzer import *

motor = Motor()
ultrasonic = Ultrasonic()
turning = False

def turnRight(): 
    PWM.setMotorModel(2000,2000,-500,-500)

def turnLeft(): 
    PWM.setMotorModel(-500,-500,2000,2000)

def moveForward():
    PWM.setMotorModel(1000,1000,1000,1000)


try:
    moveForward()
    while True:
        dist=ultrasonic.get_distance()
        print ("Obstacle distance is "+str(dist)+"CM")
        if dist < 30 and not turning:
            Buzzer.run('1')
            turnRight()
        elif dist > 50 and turning:
            Buzzer.run('0')
            moveForward()
        time.sleep(1)
except KeyboardInterrupt:
    PWM.setMotorModel(0,0,0,0)
    print ("\nEnd of program")
