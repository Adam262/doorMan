import time
import RPi.GPIO as io
import requests

io.setmode(io.BCM)
io.setwarnings(False)

base_url = 'http://intense-crag-9901.herokuapp.com/1/status?status='
busy_url = base_url + 'busy'
free_url = base_url + 'free'

door_pin = 17
led_pin = 4
pir_pin = 22

io.setup(led_pin, io.OUT)
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)
io.setup(pir_pin, io.IN) 

# while True:
  # if not io.input(door_pin):
 # if not io.input(pir_pin):
    # io.output(led_pin, True)
  # else:
    # io.output(led_pin, False)  
	
  # time.sleep(0.5)

# def turn_on(led_pin):
  # io.output(led_pin, True)

# def turn_off(led_pin):
  # io.output(led_pin, False)

# io.add_event_detect(door_pin, io.RISING, callback=turn_off)
# io.add_event_detect(door_pin, io.FALLING, callback=turn_on)

while True:
  io.wait_for_edge(door_pin, io.FALLING)
  print('room is busy')
  requests.post(busy_url)
  io.output(led_pin, True)

  io.wait_for_edge(door_pin, io.RISING)
  print('room is free')
  requests.post(free_url)
  io.output(led_pin, False)
io.cleanup()


