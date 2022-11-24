from servo import * 
pwm=Servo()
def poop_Servo():
    try:
        while True:
for i in range(50,110,1): pwm.setServoPwm('3',i) time.sleep(0.01)
for i in range(110,50,-1): pwm.setServoPwm('3',i) time.sleep(0.01)
except KeyboardInterrupt:
  pwm.setServoPwm('3',90) print "\nEnd of program"
