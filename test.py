#!/usr/bin/env python

# import required libs
import motor28byj48
import time
import sys

# RUN THE PROGRAM, if pass parameter move with steps, if no param passed, move 9 steps every 10 seconds

# Use BCM GPIO references
# be sure you are setting pins accordingly
# GPIO7,GPIO11,GPIO13,GPIO15
#StepPins = [7,11,13,15]
motor = motor28byj48.StepperMotor([7,11,13,15])

try:
  if (len(sys.argv)>1):
    motor.move(int(sys.argv[1]))
  else:
    while(1==1):
      motor.move(10)
      time.sleep(5)
except Exception as ex:
  print ex
  motor.cleanup()
finally:
  motor.cleanup()
