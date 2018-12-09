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

LANDER_SECTOR = random.randint(1, 24)
LANDER_X = random.randint(2, 11)
LANDER_Y = random.randint(2, 11)

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

objects = {
    0: [images.floor,
        None,
        "The floor is shiny and clean."],
    1: [images.pillar,
        images.full_shadow,
        "The wall is smooth and cold."],
    2: [images.soil,
        None,
        "It’s like a desert. Or should that be dessert?"],
    3: [images.pillar_low,
        images.half_shadow,
        "The wall is smooth and cold."],
    4: [images.bed,
        images.half_shadow,
        "A tidy and comfortable bed."],
    5: [images.table,
        images.half_shadow,
        "It’s made from strong plastic."],
    6: [images.chair_left,
        None,
        "A chair with a soft cushion."],
    7: [images.chair_right,
        None,
        "A chair with a soft cushion."],
    8: [images.bookcase_tall,
        images.full_shadow,
        "Bookshelves, stacked with reference books."],
    9: [images.bookcase_small,
        images.half_shadow,
        "Bookshelves, stacked with reference books."],
    10: [images.cabinet,
         images.half_shadow,
        "A small locker, for storing personal items."],
    11: [images.desk_computer,
         images.half_shadow,
         "A computer. Use it to run life support diagnostics."],
    12: [images.plant,
         images.plant_shadow,
         "A spaceberry plant, grown here."],
    13: [images.electrical1,
         images.half_shadow,
         "Electrical systems used for powering the space station."],
    14: [images.electrical2,
         images.half_shadow,
         "Electrical systems used for powering the space station."],
    15: [images.cactus,
         images.cactus_shadow,
         "Ouch! Careful on the cactus!"],
    16: [images.shrub,
         images.shrub_shadow,
         "A space lettuce. A bit limp, but amazing it’s growing here!"],
    17: [images.pipes1,
         images.pipes1_shadow,
         "Water purification pipes."],
    18: [images.pipes2,
         images.pipes2_shadow,
         "Pipes for the life support systems."],
    19: [images.pipes3,
         images.pipes3_shadow,
         "Pipes for the life support systems."],
    20: [images.door,
         images.door_shadow,
         "Safety door. Opens automatically \
         for astronauts in functioning spacesuits."],
    21: [images.door,
         images.door_shadow,
         "The airlock door. \
         For safety reasons, it requires two person operation."],
    22: [images.door,
         images.door_shadow,
         "A locked door. It needs " + PLAYER_NAME + "’s access card."],
    23: [images.door,
         images.door_shadow,
         "A locked door. It needs " + FRIEND1_NAME + "’s access card."],
    24: [images.door,
         images.door_shadow,
         "A locked door. It needs " + FRIEND2_NAME + "’s access card."],
    25: [images.door,
         images.door_shadow,
         "A locked door. It is opened from Main Mission Control."],
    26: [images.door,
         images.door_shadow,
         "A locked door in the engineering bay."],
    27: [images.map,
         images.full_shadow,
         "The screen says the crash site was Sector: " \
         + str(LANDER_SECTOR) + " // X: " + str(LANDER_X) \
         + " // Y " + str(LANDER_Y)],
    28: [images.rock_large,
         images.rock_large_shadow,
         "A rock. Its coarse surface feels like a whetstone",
         "the rock"],
    29: [images.rock_small,
         images.rock_small_shadow,
         "A small but heavy piece of Martian rock."],
    30: [images.crater,
         None,
         "A crater in the planet surface."],
    31: [images.fence,
         None,
         "A fine gauze fence. \
         It helps protect the station from dust storms."],
    32: [images.contraption,
         images.contraption_shadow,
         "One of the scientific experiments. It gently vibrates."],
    33: [images.robot_arm,
         images.robot_arm_shadow,
         "A robot arm, used for heavy lifting."],
    34: [images.toilet,
         images.half_shadow,
         "A sparkling clean toilet."],
    35: [images.sink,
         None,
         "A sink with running water.",
         "the taps"],
    36: [images.globe,
         images.globe_shadow,
         "A giant globe of the planet. \
         It gently glows from inside."],
    37: [images.science_lab_table,
         None,
         "A table of experiments, analyzing the planet soil and dust."],
    38: [images.vending_machine,
         images.full_shadow,
         "A vending machine. It requires a credit.",
         "the vending machine"],
    39: [images.floor_pad,
         None,
         "A pressure sensor to make sure nobody goes out alone."],
    40: [images.rescue_ship,
         images.rescue_ship_shadow,
         "A rescue ship!"],
    41: [images.mission_control_desk,
         images.mission_control_desk_shadow,
         "Mission Control stations."],
    42: [images.button,
         images.button_shadow,
         "The button for opening the time-locked door in engineering."],
    43: [images.whiteboard,
         images.full_shadow,
         "The whiteboard is used in brainstorms and planning meetings."],
    44: [images.window,
         images.full_shadow,
         "The window provides a view out onto the planet surface."],
    45: [images.robot,
         images.robot_shadow,
         "A cleaning robot, turned off."],
    46: [images.robot2,
         images.robot2_shadow,
         "A planet surface exploration robot, awaiting set-up."],
    47: [images.rocket,
         images.rocket_shadow,
         "A 1-person craft in repair."],
    48: [images.toxic_floor,
         None,
         "Toxic floor - do not walk on!"],
    49: [images.drone,
         None,
         "A delivery drone."],
    50: [images.energy_ball,
         None,
         "An energy ball - dangerous!"],
    51: [images.energy_ball2,
         None,
         "An energy ball - dangerous!"],
    52: [images.computer,
         images.computer_shadow,
         "A computer workstation, for managing space station systems."],
    53: [images.clipboard,
         None,
         "A clipboard. Someone has doodled on it.",
         "the clipboard"],
    54: [images.bubble_gum,
         None,
         "A piece of sticky bubble gum. Spaceberry flavour.",
         "bubble gum"],
    55: [images.yoyo,
         None,
         "A toy made of fine, strong string and plastic. \
         Used for antigrav experiments.",
         PLAYER_NAME + "’s yoyo"],
    56: [images.thread,
         None,
         "A piece of fine, strong string.",
         "a piece of string"],
    57: [images.needle,
         None,
         "A sharp needle from a cactus plant.",
         "a cactus needle"],
    58: [images.threaded_needle,
         None,
         "A cactus needle, spearing a length of string",
         "needle and string"],
    59: [images.canister,
         None,
         "The air canister has a leak.",
         "a leaky air canister"],
    60: [images.canister,
         None,
         "It looks like the seal will hold!",
         "a sealed air canister"],
    61: [images.mirror,
         None,
         "The mirror throws a circle of light on the walls.",
         "a mirror"],
    62: [images.bin_empty,
         None,
         "A rarely bin, made of light plastic",
         "a bin"],
    63: [images.bin_full,
         None,
         "A heavy bin full of water.",
         "a bin full of water"],
    64: [images.rags,
         None,
         "An oily rag. Pick it up by a corner if you must!",
         "an oily rag"],
    65: [images.hammer,
         None,
         "A hammer. Maybe good for cracking things open…",
         "a hammer"],
    66: [images.spoon,
         None,
         "A large serving spoon.",
         "a spoon"],
    67: [images.food_pouch,
         None,
         "A dehydrated food pouch. It needs water.",
         "a dry food pack"],
    68: [images.food,
         None,
         "A food pouch. Use it to get 100% energy.",
         "ready-to-eat food"],
    69: [images.book,
         None,
         "The book has the words 'Don’t Panic' \
         on the cover in large, friendly letters.",
         "a book"],
    70: [images.mp3_player,
         None,
         "An MP3 player, with all the latest tunes.",
         "an MP3 player"],
    71: [images.lander,
         None,
         "The Poodle, a small space exploration craft. \
         Its black box has a radio sealed inside.",
         "the Poodle lander"],
    72: [images.radio,
         None,
         "A radio communications system, from the Poodle.",
         "a communications radio"],
    73: [images.gps_module,
         None,
         "A GPS Module",
         "a GPS module"],
    74: [images.positioning_system,
         None,
         "Part of a positioning system. \
         Needs a GPS module.",
         "a positioning interface"],
    75: [images.positioning_system,
         None,
         "A working positioning system.",
         "a positioning computer"],
    76: [images.scissors,
         None,
         "Scissors. They’re too blunt to cut anything. \
         Can you sharpen them?",
         "blunt scissors"],
    77: [images.scissors,
         None,
         "Razor-sharp scissors. Careful!",
         "sharpened scissors"],
    78: [images.credit,
         None,
         "A small coin for the station’s vending systems.",
         "a station credit"],
    79: [images.access_card,
         None,
         "This access card belongs to " + PLAYER_NAME,
         "an access card"],
    80: [images.access_card,
         None,
         "This access card belongs to " + FRIEND1_NAME,
         "an access card"],
    81: [images.access_card,
         None,
         "This access card belongs to " + FRIEND2_NAME,
         "an access card"]
         }

items_player_may_carry = list(range(53, 82))
# Numbers for floor, pressure pad, soil and toxic floor.
items_player_may_stand_on = items_player_may_carry + [0, 39, 2, 48]


def get_floor_type():
    if current_room in outdoor_rooms:
        return 2 # soil
    else:
        return 0 # tiled floor

def generate_map():
    global room_map, room_width, room_height, room_name, hazard_map
    global top_left_x, top_left_y, wall_transparency_frame
    room_data = GAME_MAP[current_room]
    room_name = room_data[0]
    room_height = room_data[1]
    room_width = room_data[2]

    floor_type = get_floor_type()
    if current_room in range(1, 21):
        bottom_edge = 2 # soil
        side_edge = 2
    if current_room in range(21, 26):
        bottom_edge = 1 # wall
        side_edge = 2
    if current_room > 25:
        bottom_edge = 1
        side_edge = 1

    # Top line of room map
    room_map = [[side_edge] * room_width]

    # Add middle lines (wall, floor to fill width, wall)
    for y in range(room_height - 2):
        room_map.append([side_edge]
                        + [floor_type] * (room_width - 2) + [side_edge])

    # Add bottom line of room map
    room_map.append([bottom_edge] * room_width)

    # Add doorways
    middle_row = int(room_height / 2)
    middle_column = int(room_width / 2)

    if room_data[4]: # If exit at right of this room
        room_map[middle_row][room_width - 1] = floor_type
        room_map[middle_row + 1][room_width - 1] = floor_type
        room_map[middle_row - 1][room_width - 1] = floor_type

    if current_room % MAP_WIDTH != 1: # If not on the left of the map
        room_to_left = GAME_MAP[current_room - 1]
        if room_to_left[4]:
            room_map[middle_row][0] = floor_type
            room_map[middle_row + 1][0] = floor_type
            room_map[middle_row - 1][0] = floor_type

    if room_data[3]: # If exit at top of this room
        room_map[0][middle_column] = floor_type
        room_map[0][middle_column + 1] = floor_type
        room_map[0][middle_column - 1] = floor_type

    if current_room <= MAP_SIZE - MAP_WIDTH: # If room not on bottom row
        room_below = GAME_MAP[current_room + MAP_WIDTH]
        if room_below[3]:
            room_map[room_height - 1][middle_column] = floor_type
            room_map[room_height - 1][middle_column + 1] = floor_type
            room_map[room_height - 1][middle_column - 1] = floor_type


def draw():
    global room_height, room_width, room_map
    generate_map()
    screen.clear()
    room_map[2][4] = 7
    room_map[2][6] = 6
    room_map[1][1] = 8
    room_map[1][2] = 9
    room_map[1][8] = 12
    room_map[1][9] = 9

    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = objects[room_map[y][x]][0]
            screen.blit(image_to_draw,
                        (top_left_x + (x * 30),
                         top_left_y + (y * 30) - image_to_draw.get_height()))

# Exploring the room
def movement():
    global current_room
    old_room = current_room

    if keyboard.left:
        current_room -= 1
    if keyboard.right:
        current_room += 1
    if keyboard.up:
        current_room -= MAP_WIDTH
    if keyboard.down:
        current_room += MAP_WIDTH

    if current_room > 50:
        current_room = 50
    if current_room < 1:
        current_room = 1

    if current_room != old_room:
        print("Entering room: " + str(current_room))

clock.schedule_interval(movement, 0.1)

pgzrun.go()
