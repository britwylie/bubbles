
'''
lights.py: sets up neopixels for back lighting

__author__ = "Brit W"

'''

import board
import neopixel
import numpy as np

# Change the number to the number of LEDs
pixels = neopixel.NeoPixel(board.D18, 50)

# value from 0 to 1
bright = 0.5

# Color values
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Current color of LEDs
ccolor = white

# Turn on LEDs
pixels.fill(tuple(bright *np.array(ccolor)))


