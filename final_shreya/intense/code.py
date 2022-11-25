# Write your code here :-)
# SPDX-FileCopyrightText: 2018 Anne Barela for Adafruit Industries
#
# SPDX-License-Identifier: MIT
print("starting up")
import neoring_colors
import musicCode

#neoring.lightLED()

import time
import board
from analogio import AnalogIn

light_sensor1 = AnalogIn(board.A1)  # potentiometer connected to A1, power & ground

delta_threshold = 700
brightness = light_sensor1.value
pbrightness = brightness

# colorArr = [0, 10, 30, 85, 100, 137, 170, 213]

#suspenseful
# colorArr = [0, 10, 30, 50]

#happy
#colorArr = [70, 80]




#neoring_colors.lightOff()
i = 0
flag = True;
while True:
    #print
    #musicCode.stop()
    brightness = light_sensor1.value
    print((light_sensor1.value))      # Display value
    if(brightness - pbrightness > delta_threshold and flag):
        ##also add a max ceiling beyond which it will work
        print(light_sensor1.value)
        print("Changed")
        ##function call
        #music.musicOn()
        musicCode.play(i+1)
        i=(i+1)%1
        flag = False
        print(i)
    else:
        flag = True
    pbrightness = brightness

    time.sleep(1)                   # Wait a bit before checking all again

