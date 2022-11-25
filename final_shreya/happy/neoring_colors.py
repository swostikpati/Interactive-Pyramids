# Write your code here :-)
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
BRIGHTNESS = 0.5 # Let's not blind everyone

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

def lightLED2(b,t1):
    if (b==0):
        happy1(t1)
    else:
        happy2(t1)
    strip.fill(0)

def happy1(t):
    time.sleep(.5)
    for i in range(6):
        strip[i]=(83, 205, 20) # keep
    time.sleep(t/12)
    strip.fill((0,0,0))
    for i in range(6):
        strip[i+6]=(0, 205, 0) # keep
    time.sleep(t/12)
    #strip.fill(OFF)
    strip.fill((255, 153, 0)) # keep
    time.sleep(t/12)
    strip.fill((255, 51, 0))
    time.sleep(t/12)
    strip.fill((0,0,0))
    for i in [0,1,2,9,10,11]:
        strip[i]=(0, 155, 0)
    time.sleep(t/12)
    strip.fill((0,0,0))
    for i in [3,4,5,6,7,8]:
        strip[i]=(179, 36, 0)
    time.sleep(t/12)
    strip.fill((0,0,0))
    for i in range(6):
        strip[i]=(128, 255, 0)
    time.sleep(t/12)
    strip.fill((0,0,0))
    for i in range(6):
        strip[i+6]=(230, 92, 0) # keep
    time.sleep(t/12)
    strip.fill((50, 255, 0))
    time.sleep(t/12)
    strip.fill((0,0,0))
    for i in [0,1,2,9,10,11]:
        strip[i]=(128, 255, 0)
    time.sleep(t/12)
    strip.fill((0,0,0))
    for i in [3,4,5,6,7,8]:
        strip[i]=(255, 51, 0) # keep
    time.sleep(t/12)
    strip.fill((255, 153, 0)) #keep
    time.sleep(t/12)

# def lightOff():
#     strip.fill(0)



def happy2(t):
    time.sleep(.5)
    for i in range(4):
        strip[i]=(255, 51, 0) # orange
    time.sleep(.5)
    for i in range(4):
        strip[i+4]=(255, 153, 0) # yellow
    time.sleep(.5)
    for i in range(4):
        strip[i+8]=(0, 205, 0) # green
    time.sleep(.5)
    strip.fill((255, 159, 28)) # white
    time.sleep(1)
    strip.fill((236, 193, 52)) # buish white
    time.sleep(.6)
    strip.fill((0,0,0))
    for i in [0,1,2,9,10,11]:
        strip[i]=(255, 51, 0)
    time.sleep(t/12)
    #strip.fill((0,0,0))
    for i in [3,4,5,6,7,8]:
        strip[i]=(255, 153, 0)
    time.sleep(t/12)
    #strip.fill((0,0,0))
    for i in range(6):
        strip[i]=(0, 205, 0)
    time.sleep(t/12)
    strip.fill((0,0,0))
    for i in range(6):
        strip[i+6]=(255, 153, 0) # yellow
    time.sleep(t/12)
    for i in [0,1,2,9,10,11]:
        strip[i]=(255, 51, 0)
    time.sleep(t/12)


'''while True:
    #for i in range(255):
        #strip.fill((colorwheel(i)))
    strip.fill(colorwheel(1))'''
# Write your code here :-)# Write your code here :-)
