from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

while True:
  e = (randint(0,255), randint(0,255), randint(0,255))

  image = [
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e
  ]

  sense.set_pixels(image)
  sleep(0.1)
