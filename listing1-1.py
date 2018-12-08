#!/usr/bin/env python
# coding: utf-8

# Spacewalk
# Personal work following the book “Mission Python” (Sean McManus)

# pgzrun import (+ pgzrun.go() command) makes the code running
# when calling it using the python/python3 command.
import pgzrun


WIDTH = 800
HEIGHT = 600
player_x = 600
player_y = 350


def draw():
    screen.blit(images.backdrop, (0, 0))

pgzrun.go()
