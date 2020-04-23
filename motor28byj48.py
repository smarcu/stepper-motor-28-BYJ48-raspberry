#!/usr/bin/env python

# import required libs
import time
import RPi.GPIO as GPIO
import sys

class StepperMotor:
  def __init__(self, pins):
    self.pins = pins
    self.totalStepsMoved = 0

    GPIO.cleanup()

    # Use BCM GPIO references
    GPIO.setmode(GPIO.BOARD)

    # be sure you are setting pins accordingly
    # GPIO7,GPIO11,GPIO13,GPIO15
    #StepPins = [7,11,13,15]
    StepPins = self.pins

    # Set all pins as output
    for pin in StepPins:
      GPIO.setup(pin,GPIO.OUT)
      GPIO.output(pin, False)

    #wait some time to start
    time.sleep(0.5)
    return

  def move(self, moveSteps):

    print("moving ", moveSteps)
    # Define some settings
    StepCounter = 0
    #WaitTime = 0.85
    #WaitTime=0.62
    WaitTime=0.001

    StepPins = self.pins

    # steps moved in this method call, when reaching value of moveSteps, it stops
    StepsMovedInThisCall = 0

    # Define advanced sequence
    # as shown in manufacturers datasheet
    StepCount = 8
    Seq = []
    Seq = [0,1,2,3,4,5,6,7]
    Seq[0] = [1,0,0,0]
    Seq[1] = [1,1,0,0]
    Seq[2] = [0,1,0,0]
    Seq[3] = [0,1,1,0]
    Seq[4] = [0,0,1,0]
    Seq[5] = [0,0,1,1]
    Seq[6] = [0,0,0,1]
    Seq[7] = [1,0,0,1]

    # Start main loop
    while 1==1:
      for pin in range(0, 4):
        xpin = StepPins[pin]
        if Seq[StepCounter][pin]!=0:
          #print " Step %i Enable %i" %(StepCounter,xpin)
          GPIO.output(xpin, True)
        else:
          GPIO.output(xpin, False)
      StepCounter += 1

      # If we reach the end of the sequence start again
      if (StepCounter==StepCount):
        StepCounter = 0
      if (StepCounter<0):
        StepCounter = StepCount

      # counting total steps in class
      self.totalStepsMoved += 1
      # counting total steps on this method
      StepsMovedInThisCall += 1
      # print("StepsMovedInThisCall: ", StepsMovedInThisCall, "totalStepsMoved: ", self.totalStepsMoved)
      if (StepsMovedInThisCall >= moveSteps):
        return

      # Wait before moving on
      time.sleep(WaitTime)
    return

  def cleanup(self):
    print "performing cleanup"
    StepPins = self.pins
    GPIO.cleanup();
    GPIO.setmode(GPIO.BOARD)
    for pin in StepPins:
      GPIO.setup(pin,GPIO.OUT)
      GPIO.output(pin, False)
    return
