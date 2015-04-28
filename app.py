import time
import RPi.GPIO as io

io.setmode(io.BCM)

door_pin = 17
led_pin = 4

io.setup(led_pin, io.OUT)
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)
 
while True:
  if not io.input(door_pin):
    io.output(led_pin, True)
  else:
    io.output(led_pin, False)  
	
  time.sleep(0.5)


