#!/usr/bin/env python
# coding: utf-8

# Spacewalk
# Personal work following the book “Mission Python” (Sean McManus)

# pgzrun import (+ pgzrun.go() command) makes the code running
# when calling it using the python/python3 command.
import pgzrun


room_map = [ [1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1]
           ]

# Window Size
WIDTH = 800
HEIGHT = 800

top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.floor, images.pillar]

room_height = 7
room_width = 5


def draw():
    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = DEMO_OBJECTS[room_map[y][x]]
            screen.blit(image_to_draw,
                (top_left_x + (x * 30),
                 top_left_y + (y * 30) - image_to_draw.get_height()))

pgzrun.go()
