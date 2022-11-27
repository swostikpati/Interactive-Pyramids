# SPDX-FileCopyrightText: 2019 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT
#
# Modified by Mangtronix for Desert Media Art at NYUAD
# https://desert.nyuadim.com

"""Simple rainbow example for 12-pixel NeoPixel ring"""

print("Starting neoring")

import time
import digitalio
import board
from rainbowio import colorwheel
import neopixel
import musicCode

NUM_PIXELS = 12  # NeoPixel ring length (in pixels)
BRIGHTNESS = 0.25 # Let's not blind everyone

# The power for the NeoPixels is not enabled by default (to save battery power)
# We need to turn on the power by setting pin D10 high
print("Enabling NeoPixel power!")
# enable = digitalio.DigitalInOut(board.D10)
# enable.direction = digitalio.Direction.OUTPUT
# enable.value = True

strip = neopixel.NeoPixel(board.D5, NUM_PIXELS, brightness=BRIGHTNESS)

# colorArr = [0, 10, 30, 85, 100, 137, 170, 213]

# cycle_sequence([
#     range(256),  # rainbow_cycle
#     [0],  # red
#     [10],  # orange
#     [30],  # yellow
#     [85],  # green
#     [137],  # cyan
#     [170],  # blue
#     [213],  # purple
#     [0, 10, 30, 85, 137, 170, 213],  # party mode
# ])

def lightLED(color, t):
    strip.fill(colorwheel(color))
    time.sleep(t)
    strip.fill(0)

# def lightOff():
#     strip.fill(0)



'''while True:
    #for i in range(255):
        #strip.fill((colorwheel(i)))
    strip.fill(colorwheel(1))'''
# Write your code here :-)# Write your code here :-)
