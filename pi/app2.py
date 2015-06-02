import time
import RPi.GPIO as io
import requests
from helpers import url, setup_out, setup_in

io.setmode(io.BCM)
io.setwarnings(False)

busy_url = url(3, 'busy')
free_url = url(3, 'free')

door_pin = 27 

setup_in([door_pin])

while True:
  io.wait_for_edge(door_pin, io.FALLING)
  print('room 2 is busy')
  requests.post(busy_url)

  io.wait_for_edge(door_pin, io.RISING)
  print('room 2 is free')
  requests.post(free_url)
io.cleanup()

