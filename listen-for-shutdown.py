#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(27, GPIO.OUT)
GPIO.output(27, GPIO.HIGH)

GPIO.wait_for_edge(3, GPIO.FALLING)

GPIO.output(27, GPIO.LOW)
subprocess.call(['shutdown', '-h', 'now'], shell=False)
