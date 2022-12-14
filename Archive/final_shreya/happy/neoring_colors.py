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
        #calm1(t1)
        #intense1(t1)
    elif (b==1):
        happy2(t1)
        #calm2(t1)
        #intense2(t1)
    else:
        happy3(t1)
        #calm3(t1)
        #intense3(t1)
    strip.fill(0)




####################### HAPPY SOUNDS ################################


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


def happy3(t):
    time.sleep(.2)
    for i in range(6):
        strip[i]=colorwheel(10) #cyan
    time.sleep(.5)
    for i in range(6):
        strip[i+6]=colorwheel(213) # light purple
    time.sleep(.5)
    for i in range(4):
        strip[i-2]=colorwheel(30) # yellow
    time.sleep(.2)
    for i in range(4):
        strip[i+2]=colorwheel(5) # light green
    time.sleep(.2)
    for i in range(4):
        strip[i+6]=colorwheel(55) # light green
    time.sleep(.4)
    strip.fill(0)
    #time.sleep(0.2)
    for i in range(6):
        strip[i]=colorwheel(10) #cyan
    time.sleep(.5)
    for i in range(6):
        strip[i+6]=colorwheel(213) # light purple
    time.sleep(.5)
    for i in range(4):
        strip[i-2]=colorwheel(30) # yellow
    time.sleep(.2)
    for i in range(4):
        strip[i+2]=colorwheel(5) # light green
    time.sleep(.2)
    for i in range(4):
        strip[i+6]=colorwheel(55) # light green
    time.sleep(.4)
    #strip.fill(0)

#     strip.fill((125, 249, 255)) # electric blue
#     time.sleep(1)
#     strip.fill((245,218,223)) # light pink
#     time.sleep(.6)
#     strip.fill((0,0,0))
#     for i in [0,1,2,9,10,11]:
#         strip[i]=(64,224,208) #turquiose
#     time.sleep(t/12)
#     strip.fill((0,0,0))
#     for i in [3,4,5,6,7,8]:
#         strip[i]=(231,178,255) # light purple
#     time.sleep(t/12)
#     strip.fill((0,0,0))
#     for i in range(6):
#         strip[i]=(84,255,251) #cyan
#     time.sleep(t/12)
#     strip.fill((0,0,0))
#     for i in range(6):
#         strip[i+6]=(127,255,212) # aquamarine
#     time.sleep(t/12)
#     for i in [0,1,2,9,10,11]:
#         strip[i]=(245,218,223) #light pink
#     time.sleep(t/12)



####################### CALM SOUNDS ################################


def calm1(t):
    for i in range(5):
        #j = 156+9.9*i
        strip.fill((0+84*0.2*i,99+(255-99)*0.2*i,156+(251-156)*0.2*i))
        time.sleep(t/50)
    for i in range(5):
        strip.fill((84+(231-84)*0.2*i,255-(255-178)*0.2*i,255))
        time.sleep(t/50)
    time.sleep(t/10)
    for i in range(4):
        strip[i+4]=colorwheel(137)
    time.sleep(t/10)
    for i in range(4):
        strip[i+8]=(125, 249, 255) # electric blue
    time.sleep(t/10)
    for i in range(4):
        #strip[i]=((0,99,156))
        strip[i]=(colorwheel(157)) # light pink
    time.sleep(t/5)
    for i in range(5):
        strip.fill((84+(127-84)*0.2*i,255,251-(251-212)*0.2*i))
        time.sleep(t/50)
    for i in range(5):
        strip.fill((127+(245-127)*0.2*i,255-(255-218)*0.2*i,223))
        time.sleep(t/50)
    time.sleep(t/5)

# def calm1(t):
#     for i in range(45):
#         strip[(11-i)%12]=(i*5,0,255-i*5)
#         time.sleep(t/80)
#     for i in range(45):
#         strip[(11-(i+9))%12]=(225-i*5,0,30+i*5)
#         time.sleep(t/80)

def calm2(t):
    for i in range(45):
        strip[i%12]=(0,i*5,255-i*5)
        time.sleep(t/80)
    for i in range(45):
        strip[(i+9)%12]=(0,225-i*5,30+i*5)
        time.sleep(t/80)

def calm3(t):
    for i in range(45):
        strip.fill((i*5,255-i*5,0))
        time.sleep(t/80)
    for i in range(45):
        strip.fill((225-i*5,30+i*5,0))
        time.sleep(t/80)



####################### INTENSE SOUNDS ################################


def intense1(t):
    #strip.fill((100,110,210,255))
    strip.fill(colorwheel(117))
    time.sleep(0.9)
    strip.fill(colorwheel(110))
    time.sleep(.9)
    strip.fill((155,255,155,205))
    time.sleep(1.5)
    strip.fill((108,128,78,128))
    time.sleep(1.2)
    strip.fill((215,215,50,155))
    time.sleep(1.1)
    strip.fill((215,215,30,215))
    time.sleep(.7)
    strip.fill((215,215,110,255))
    time.sleep(1.2)
    strip.fill((255,50,255,255))
    time.sleep(t/3)

def intense2(t):
    strip.fill(colorwheel(30))
    time.sleep(t/6)
    strip.fill(colorwheel(25))
    time.sleep(t/6)
    strip.fill(colorwheel(20))
    time.sleep(t/6)
    strip.fill(colorwheel(15))
    time.sleep(t/6)
    strip.fill(colorwheel(10))
    time.sleep(t/3)
    strip.fill((255,0,0,255))
    time.sleep(2.7)
    for i in range(51):
        strip.fill((255-i*5,0,0,255))
        time.sleep(0.05)

def intense3(t):
    for i in range(51):
        strip.fill((i*5,0,255-i*5))
        time.sleep(t/51)
    strip.fill((255,0,0))
    time.sleep(0.2)
    for i in range(51):
        strip.fill((255-i*5,0,0))
        time.sleep(0.02)
#     for i in range(45):
#         strip.fill((i*5,0,255-i*5))
#         time.sleep(t/80)
#     for i in range(45):
#         strip.fill((225-i*5,0,30+i*5))
#         time.sleep(t/80)



'''while True:
    #for i in range(255):
        #strip.fill((colorwheel(i)))
    strip.fill(colorwheel(1))'''
# Write your code here :-)# Write your code here :-)
