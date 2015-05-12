import time
import RPi.GPIO as io
import requests

io.setmode(io.BCM)
io.setwarnings(False)

def url( id, status ):
  return 'http://intense-crag-9901.herokuapp.com/' + str(id) + '/status?status=' + status

def setup_out(pins):
  for pin in pins:
    io.setup(pin, io.OUT)

def setup_in(pins):
  for pin in pins:
    io.setup(pin, io.IN, pull_up_down=io.PUD_UP)

busy_url_1 = url(1, 'busy')
free_url_1 = url(1, 'free')
busy_url_2 = url(3, 'busy')
free_url_2 = url(3, 'free')

door_pin_1 = 17
door_pin_2 = 27 

setup_in([door_pin_1, door_pin_2])

while True:
  io.wait_for_edge(door_pin_1, io.FALLING)
  print('room 1 is busy')
  requests.post(busy_url_1)

  io.wait_for_edge(door_pin_1, io.RISING)
  print('room 1 is free')
  requests.post(free_url_1)

# io.wait_for_edge(door_pin_2, io.FALLING)
# print('room 2 is busy')
# requests.post(busy_url_2)

# io.wait_for_edge(door_pin_2, io.RISING)
# print('room 2 is free')
# requests.post(free_url_2)
io.cleanup()

