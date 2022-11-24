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
from random import *

rand = Random()
motor = Motor()
ultrasonic = Ultrasonic()
buzzer = Buzzer()
global turning
turning = False

def turnRight(): 
    global turning 
    turning = True
    #PWM.setMotorModel(2000,2000,-500,-500)
    PWM.setMotorModel(1400,1400,-1050,-1050)

def turnLeft(): 
    global turning 
    turning = True
    PWM.setMotorModel(-1050,-1050,1400,1400)

def moveForward():
    global turning 
    turning = False
    PWM.setMotorModel(500,500,500,500)

def buzz(time: int): 
    Buzzer.run('1')
    

try:
    moveForward()
    while True:
        dist=ultrasonic.get_distance()
        print ("Obstacle distance is "+str(dist)+"CM")
        print("turning: " + str(turning))
        if dist < 50 and not turning:
            print("Close")
            buzzer.run('1')
            if rand.randint(1,2) == 1:
                turnRight()
            else:
                turnLeft()
        elif dist > 70 and turning:
            print("Far")
            buzzer.run('0')
            moveForward()
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    PWM.setMotorModel(0,0,0,0)
    print ("\nEnd of program")
