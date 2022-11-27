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

# Set up speaker enable pin
#enable = digitalio.DigitalInOut(board.D10)
#enable.direction = digitalio.Direction.OUTPUT
#enable.value = True

speaker = audioio.AudioOut(board.A0)
mp3stream = audiomp3.MP3Decoder(open("sound.mp3", "rb"))

def musicOn():
    speaker.play(mp3stream)
    #while speaker.playing:
        #time.sleep(0.1)

