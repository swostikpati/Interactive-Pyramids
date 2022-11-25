# Write your code here :-)
# Write your code here :-)
# SPDX-FileCopyrightText: 2020 John Park for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Modified for Desert Media Art by Michael Ang

# MP3 playback with tap trigger
# Works on Feather M4 (or other M4 based boards) with Propmaker
import time
import board
import busio
import digitalio
import audioio
import audiomp3
# import adafruit_lis3dh
import neoring_colors

startup_play = False  # set to True to play all samples once on startup

# Set up accelerometer on I2C bus
# i2c = busio.I2C(board.SCL, board.SDA)
# int1 = digitalio.DigitalInOut(board.D6)
# accel = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)
# accel.set_tap(1, 100)  # single or double-tap, threshold

# Set up speaker enable pin
enable = digitalio.DigitalInOut(board.D10)
enable.direction = digitalio.Direction.OUTPUT
enable.value = True

speaker = audioio.AudioOut(board.A0)

sample_number = 0

#happy
#samples = ['music/game-show.mp3', 'music/marvel-piano.mp3', 'music/happy3.mp3']
#sample_duration = [8, 6, 4]

#calm/suspenseful
#samples = ['music/summer-piano.mp3', 'music/just-chill1.mp3', 'music/just-chill2.mp3']
#sample_duration = [7, 9, 10]

#intense
samples = ['music/xmas-calm.mp3', 'music/space-ambient.mp3', 'music/interstellar-track2.mp3']
sample_duration = [11, 8, 12]

def play(a):
    global samples #very important to reference global variables inside
    mp3stream = audiomp3.MP3Decoder(open(samples[a], "rb"))
    speaker.play(mp3stream)
    #neoring_colors.lightLED(color,sample_duration[a])
    neoring_colors.lightLED2(a,sample_duration[a])
    while speaker.playing:
            time.sleep(0.1)
#     sample_number +=1;

