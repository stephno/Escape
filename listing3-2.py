#!/usr/bin/env python
# coding: utf-8

# Spacewalk
# Personal work following the book “Mission Python” (Sean McManus)

room_map = [ [1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1]
           ]

for y in range(7):
    print(room_map[y])
