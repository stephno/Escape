#!/usr/bin/env python
# coding: utf-8

# Escape - A Python Adventure
# Personal work following the book “Mission Python” (Sean McManus)

planets = {"Mercury":
                ["The smallest planet, nearest the Sun", False, 0],
           "Venus":
                ["Venus takes 243 days to rotate", False, 0],
           "Earth":
                ["The only planet known to have native life", False, 1],
           "Mars":
                ["The Red Planet is the second smallest planet", False, 2],
           "Jupiter":
                ["The largest planet, Jupiter is a gas giant", True, 67],
           "Saturn":
                ["The second largest planet is a gas giant", True, 62],
           "Uranus":
                ["An ice giant with a ring system", True, 27],
           "Neptune":
                ["An ice giant and farthest from the Sun", True, 14],
           "Pluto":
                ["Not considered a planet since 2006.", False, 5]
           }

while True:
   query = input("Which planet would you like information on? ")
   if query in planets.keys():
       print(planets[query])
   else:
       print("No data available! Sorry!")
