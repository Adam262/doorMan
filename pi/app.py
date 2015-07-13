import time
import RPi.GPIO as io
import requests
from helpers import url, setup_out, setup_in

io.setmode(io.BCM)
io.setwarnings(False)

busy_url = url(1, 'busy')
free_url = url(1, 'free')

door_pin = 17

setup_in([door_pin])

while True:
  io.wait_for_edge(door_pin, io.FALLING)
  print('room 1 is busy')
  requests.post(busy_url)

  io.wait_for_edge(door_pin, io.RISING)
  print('room 1 is free')
  requests.post(free_url)
io.cleanup()

