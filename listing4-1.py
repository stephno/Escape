#!/usr/bin/env python
# coding: utf-8

# Escape - A Python Adventure
# Personal work following the book “Mission Python” (Sean McManus)

# pgzrun import (+ pgzrun.go() command) makes the code running
# when calling it using the python/python3 command.
import pgzrun
import time, random, math


# Window Size
WIDTH = 800
HEIGHT = 800

PLAYER_NAME = "Steph"
FRIEND1_NAME = "Friend 1"
FRIEND2_NAME = "Friend 2"

DEMO_OBJECTS = [images.floor, images.pillar, images.soil]

MAP_WIDTH = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT
GAME_MAP = [["Room 0 - Where unused objects are kept", 0, 0, False, False]]

current_room = 31
outdoor_rooms = range(1, 26)

top_left_x = 100
top_left_y = 150


for planetsectors in range(1, 26):
    GAME_MAP.append(["The dusty planet surface", 13, 13, True, True])

GAME_MAP += [["The airlock", 13, 5, True, False], # room 26
             ["The engineering lab", 13, 13, False, False],
             ["Poodle Mission Control", 9, 13, False, True], # room 28
             ["The viewing gallery", 9, 15, False, False],
             ["The crew’s bathroom", 5, 5, False, False], # room 30
             ["The airlock entry bay", 7, 11, True, True],
             ["Left elbow room", 9, 7, True, False], # room 32
             ["Right elbow room", 7, 13, True, True],
             ["The science lab", 13, 13, False, True], # room 34
             ["The greenhouse", 13, 13, True, False],
             [PLAYER_NAME + "’s sleeping quarters", 9, 11, False, False],
             ["West corridor", 15, 5, True, True],
             ["The briefing room", 7, 13, False, True], # room 38
             ["The crew’s community room", 11, 13, True, False],
             ["Main Mission Control", 14, 14, False, False], # room 40
             ["The sick bay", 12, 7, True, False],
             ["West corridor", 9, 7, True, False], # room 42
             ["Utilities control room", 9, 9, False, True],
             ["Systems engineering bay", 9, 11, False, False], # room 44
             ["Security portal to Mission Control", 7, 7, True, False],
             [FRIEND1_NAME + "’s sleeping quarters", 9, 11, True, True],
             [FRIEND2_NAME + "’s sleeping quarters", 9, 11, True, True],
             ["The pipeworks", 13, 11, True, False], # room 48
             ["The chief scientist’s office", 9, 7, True, True],
             ["The robot workshop", 9, 11, True, False]
            ]

assert len(GAME_MAP) - 1 == MAP_SIZE, "Map size and GAME_MAP don’t match."

pgzrun.go()
