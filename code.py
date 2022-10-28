# Write your code here :-)
# SPDX-FileCopyrightText: 2018 Anne Barela for Adafruit Industries
#
# SPDX-License-Identifier: MIT
print("starting up")
import neoring
import music

#neoring.lightLED()

import time
import board
from analogio import AnalogIn

light_sensor1 = AnalogIn(board.A1)  # potentiometer connected to A1, power & ground

delta_threshold = 1000
brightness = light_sensor1.value
pbrightness = brightness



while True:

    brightness = light_sensor1.value
    print((light_sensor1.value,))      # Display value
    if(brightness - pbrightness > delta_threshold):
        ##also add a max ceiling beyond which it will work
        print("Changed")
        ##function call
        music.musicOn()
        neoring.lightLED()


    pbrightness = brightness

    time.sleep(1)                   # Wait a bit before checking all again
