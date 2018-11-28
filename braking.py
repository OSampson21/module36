import RoboPiLib as RPL
import time

RPL.RoboPiInit("/dev/ttyAMA0",115200)

analogSensor = 10
motorR = 1
motorL = 0
speed = 1400

while True:
  reading == RPL.analogReadRaw(analogSensor)
  if reading > 400:
    speed -= 100
    if speed < 0:
      speed = 0
    else:
      speed = speed
    RPL.servoWrite(motorR, speed)
    RPL.servoWrite(motorL, speed+1400)
    time.sleep(0.1)
  else:
    RPL.servoWrtie(motorR, 1400)
    RPL.servoWrite(motorL, 2900)
