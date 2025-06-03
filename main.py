"""
@author : Léo Imbert
@created : 30/05/2025
@updated : 31/05/2025
"""

import colorsys
import random
import pyxel
import math
import time

DEFAULT_PYXEL_COLORS = [0x000000, 0x2B335F, 0x7E2072, 0x19959C, 
                        0x8B4852, 0x395C98, 0xA9C1FF, 0xEEEEEE, 
                        0xD4186C, 0xD38441, 0xE9C35B, 0x70C6A9, 
                        0x7696DE, 0xA3A3A3, 0xFF9798, 0xEDC7B0]

characters_matrices = {
    " ":[[0,0,0,0]],
    "A":[[0,0,0,0,0,0],[0,0,1,1,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1]],
    "B":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[1,1,1,1,1,1,0]],
    "C":[[0,0,0,0,0,0,0],[0,0,1,1,1,1,0],[0,1,1,0,0,1,1],[1,1,0,0,0,0,0],[1,1,0,0,0,0,0],[1,1,0,0,0,0,0],[0,1,1,0,0,1,1],[0,0,1,1,1,1,0]],
    "D":[[0,0,0,0,0,0,0],[1,1,1,1,1,0,0],[0,1,1,0,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,1,1,0],[1,1,1,1,1,0,0]],
    "E":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[0,1,1,0,0,0,1],[0,1,1,0,1,0,0],[0,1,1,1,1,0,0],[0,1,1,0,1,0,0],[0,1,1,0,0,0,1],[1,1,1,1,1,1,1]],
    "F":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[0,1,1,0,0,0,1],[0,1,1,0,1,0,0],[0,1,1,1,1,0,0],[0,1,1,0,1,0,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "G":[[0,0,0,0,0,0,0],[0,0,1,1,1,1,0],[0,1,1,0,0,1,1],[1,1,0,0,0,0,0],[1,1,0,0,0,0,0],[1,1,0,0,1,1,1],[0,1,1,0,0,1,1],[0,0,1,1,1,1,1]],
    "H":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1]],
    "I":[[0,0,0,0,0,0],[1,1,1,1,1,1],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[1,1,1,1,1,1]],
    "J":[[0,0,0,0,0,0,0],[0,0,0,1,1,1,1],[0,0,0,0,1,1,0],[0,0,0,0,1,1,0],[0,0,0,0,1,1,0],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,1,0,0]],
    "K":[[0,0,0,0,0,0,0],[1,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,1,1,0],[0,1,1,1,1,0,0],[0,1,1,0,1,1,0],[0,1,1,0,0,1,1],[1,1,1,0,0,1,1]],
    "L":[[0,0,0,0,0,0,0],[1,1,1,1,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,1],[0,1,1,0,0,1,1],[1,1,1,1,1,1,1]],
    "M":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,1,0,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,0,1,0,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1]],
    "N":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,1,0,0,1,1],[1,1,1,1,0,1,1],[1,1,0,1,1,1,1],[1,1,0,0,1,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1]],
    "O":[[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[0,1,1,0,1,1,0],[0,0,1,1,1,0,0]],
    "P":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "Q":[[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,1,1,0,1],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "R":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,1,1,0],[0,1,1,0,0,1,1],[1,1,1,0,0,1,1]],
    "S":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "T":[[0,0,0,0,0,0],[1,1,1,1,1,1],[1,0,1,1,0,1],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,1,1,1,1,0]],
    "U":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "V":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,1,1,0,0]],
    "W":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,1,0,1,1],[1,1,1,1,1,1,1],[1,1,1,0,1,1,1],[1,1,0,0,0,1,1]],
    "X":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[0,1,1,0,1,1,0],[0,0,1,1,1,0,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1]],
    "Y":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,1,1,1,1,0]],
    "Z":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[1,1,0,0,0,1,1],[1,0,0,0,1,1,0],[0,0,0,1,1,0,0],[0,0,1,1,0,0,1],[0,1,1,0,0,1,1],[1,1,1,1,1,1,1]],
    "a":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,0,0,0,1,1,0],[0,1,1,1,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "b":[[0,0,0,0,0,0,0],[1,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[1,1,0,1,1,1,0]],
    "c":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "d":[[0,0,0,0,0,0,0],[0,0,0,1,1,1,0],[0,0,0,0,1,1,0],[0,1,1,1,1,1,0],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "e":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0]],
    "f":[[0,0,0,0,0,0],[0,0,1,1,1,0],[0,1,1,0,1,1],[0,1,1,0,0,0],[1,1,1,1,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[1,1,1,1,0,0]],
    "g":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1],[0,0,0,0,1,1],[1,1,1,1,1,0]],
    "h":[[0,0,0,0,0,0,0],[1,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,1,1,0],[0,1,1,1,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[1,1,1,0,0,1,1]],
    "i":[[0,0,0,0],[0,1,1,0],[0,0,0,0],[1,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[1,1,1,1]],
    "j":[[0,0,0,0,0,0],[0,0,0,0,1,1],[0,0,0,0,0,0],[0,0,0,1,1,1],[0,0,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "k":[[0,0,0,0,0,0,0],[1,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,1,1],[0,1,1,0,1,1,0],[0,1,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,1,0,0,1,1]],
    "l":[[0,0,0,0],[1,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[1,1,1,1]],
    "m":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,0,1,1,0],[1,1,1,1,1,1,1],[1,1,0,1,0,1,1],[1,1,0,1,0,1,1],[1,1,0,0,0,1,1]],
    "n":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1]],
    "o":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "p":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "q":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,1,0,1,1],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,1,1,0],[0,0,0,0,1,1,0],[0,0,0,1,1,1,1]],
    "r":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,1,1,1,0],[0,1,1,1,0,1,1],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "s":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,0,0],[0,1,1,1,1,0],[0,0,0,0,1,1],[1,1,1,1,1,0]],
    "t":[[0,0,0,0,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[1,1,1,1,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[0,1,1,0,1,1],[0,0,1,1,1,0]],
    "u":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1]],
    "v":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,1,1,0,0]],
    "w":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,0,1,0,1,1],[1,1,0,1,0,1,1],[1,1,1,1,1,1,1],[0,1,1,0,1,1,0]],
    "x":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[0,1,1,0,1,1,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1]],
    "y":[[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1],[0,0,0,0,1,1],[1,1,1,1,1,0]],
    "z":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1],[1,0,0,1,1,0],[0,0,1,1,0,0],[0,1,1,0,0,1],[1,1,1,1,1,1]],
    "1":[[0,0,0,0,0,0],[0,0,1,1,0,0],[0,1,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[1,1,1,1,1,1]],
    "2":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[0,0,0,0,1,1],[0,1,1,1,1,0],[1,1,0,0,0,0],[1,1,0,0,1,1],[1,1,1,1,1,1]],
    "3":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[0,0,0,0,1,1],[0,0,1,1,1,0],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "4":[[0,0,0,0,0,0,0],[0,0,0,1,1,1,0],[0,0,1,1,1,1,0],[0,1,1,0,1,1,0],[1,1,0,0,1,1,0],[1,1,1,1,1,1,1],[0,0,0,0,1,1,0],[0,0,0,1,1,1,1]],
    "5":[[0,0,0,0,0,0],[1,1,1,1,1,1],[1,1,0,0,0,1],[1,1,0,0,0,0],[1,1,1,1,1,0],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "6":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[1,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "7":[[0,0,0,0,0,0],[1,1,1,1,1,1],[1,1,0,0,1,1],[0,0,0,0,1,1],[0,0,0,1,1,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0]],
    "8":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "9":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "0":[[0,0,0,0,0,0,0],[0,1,1,1,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,1,1,1],[1,1,0,1,0,1,1],[1,1,1,0,0,1,1],[1,1,0,0,0,1,1],[0,1,1,1,1,1,0]],
    "?":[[0,0,0,0],[1,1,1,0],[1,0,1,1],[0,0,1,1],[0,1,1,0],[0,0,0,0],[0,1,1,0],[0,1,1,0]],
    ",":[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,1,0],[0,1,1,0],[1,1,0,0]],
    ".":[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[1,1,0],[1,1,0]],
    ";":[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,1,1,0],[0,1,1,0],[1,1,0,0]],
    "/":[[0,0,0,0,0,0],[0,0,0,0,1,1],[0,0,0,0,1,0],[0,0,0,1,1,0],[0,0,1,1,0,0],[0,0,1,0,0,0],[0,1,1,0,0,0],[1,1,0,0,0,0]],
    ":":[[0,0],[0,0],[1,1],[1,1],[0,0],[1,1],[1,1],[0,0]],
    "!":[[0,0],[1,1],[1,1],[1,1],[1,1],[0,0],[1,1],[1,1]],
    "&":[[0,1,1,1,0,0,0],[1,0,0,0,1,0,0],[1,0,0,0,1,0,0],[0,1,1,1,0,0,0],[1,1,0,1,1,0,0],[1,0,0,0,1,0,1],[1,1,0,0,0,1,0],[0,1,1,1,1,0,1]],
    "é":[[0,0,0,1,1,0],[0,1,1,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0]],
    "~":[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,1],[1,0,0,1,0]],
    '"':[[0,0,0,0],[0,1,0,1],[0,1,0,1],[1,0,1,0],[1,0,1,0]],
    "#":[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,0,1,0],[1,1,1,1,1],[0,1,0,1,0],[1,1,1,1,1],[0,1,0,1,0]],
    "'":[[0,0,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,1,1,0,0],[0,1,1,0,0]],
    "{":[[0,0,0],[0,0,1],[0,1,0],[0,1,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1]],
    "(":[[0,0,0],[0,0,1],[0,1,0],[1,0,0],[1,0,0],[1,0,0],[0,1,0],[0,0,1]],
    "[":[[0,0,0],[1,1,1],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,1,1]],
    "-":[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,1],[1,1,1,1],[0,0,0,0],[0,0,0,0]],
    "|":[[1],[1],[1],[1],[1],[1],[1],[1]],
    "è":[[0,1,1,0,0,0],[0,0,0,1,1,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0]],
    "_":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1]],
    "ç":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,0,1,0,0],[0,0,1,0,0,0]],
    "à":[[0,0,1,1,0,0,0],[0,0,0,0,1,1,0],[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,0,0,0,1,1,0],[0,1,1,1,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "@":[[0,0,0,0,0,0,0],[0,0,1,1,1,1,0],[0,1,0,0,0,0,1],[1,0,0,1,1,0,1],[1,0,1,0,0,1,1],[1,0,1,0,0,1,1],[1,0,0,1,1,0,0],[0,1,0,0,0,0,1],[0,0,1,1,1,1,0]],
    "°":[[1,1,1],[1,0,1],[1,1,1]],
    ")":[[0,0,0],[1,0,0],[0,1,0],[0,0,1],[0,0,1],[0,0,1],[0,1,0],[1,0,0]],
    "]":[[0,0,0],[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[1,1,1]],
    "+":[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0]],
    "=":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1],[0,0,0,0,0,0]],
    "}":[[0,0,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1],[0,1,0],[0,1,0],[1,0,0]],
    "*":[[0,0,0],[1,0,1],[0,1,0],[1,0,1]],
    "%":[[0,1,0,0,0,0,0],[1,0,1,0,1,1,0],[0,1,0,0,1,0,0],[0,0,0,1,1,0,0],[0,0,1,1,0,0,0],[0,0,1,0,0,1,0],[0,1,1,0,1,0,1],[1,1,0,0,0,1,0]],
    "€":[[0,0,0,0,0,0],[0,0,1,1,1,0],[0,1,0,0,0,1],[0,1,1,1,0,0],[1,0,0,0,0,0],[0,1,1,1,0,0],[0,1,0,0,0,1],[0,0,1,1,1,0]],
    "$":[[0,0,1,0,0],[0,1,1,1,0],[1,0,1,0,1],[1,0,1,0,0],[0,1,1,1,0],[0,0,1,0,1],[1,0,1,0,1],[0,1,1,1,0],[0,0,1,0,0]]
}

NORMAL_COLOR_MODE = 0
ROTATING_COLOR_MODE = 1
RANDOM_COLOR_MODE = 2

ANCHOR_TOP_LEFT = 0
ANCHOR_TOP_RIGHT = 1
ANCHOR_BOTTOM_LEFT = 2
ANCHOR_BOTTOM_RIGHT = 3
ANCHOR_LEFT = 4
ANCHOR_RIGHT = 5
ANCHOR_TOP = 6
ANCHOR_BOTTOM = 7
ANCHOR_CENTER = 8

class PyxelManager:

    def __init__(self, window_size:tuple, scenes:list, default_scene_id:int, fps:int=60, fullscreen:bool=False, mouse:bool=False, quit_key:int=pyxel.KEY_ESCAPE, camera_x:int=0, camera_y:int=0)-> None:
        """
        PyxelManager
        ===
        Manages scenes, camera, and transitions in a Pyxel-based game.

        Parameters
        ---
        - window_size (tuple): The width and height of the game window.
        - scenes (list): A list of scene objects.
        - default_scene_id (int): The ID of the default scene.
        - fps (int): The frame rate of the game (default: 60).
        - fullscreen (bool): Whether the game starts in fullscreen mode (default: False).
        - mouse (bool): Whether the mouse is enabled (default: False).
        - quit_key (int): The key to quit the game (default: pyxel.KEY_ESCAPE).
        - camera_x (int): The initial x position of the camera (default: 0).
        - camera_y (int): The initial y position of the camera (default: 0).

        Methods
        ---
        ```
        .set_camera()                           # Sets the camera position.
        .move_camera_to()                       # Moves the camera to a target position.
        .shake_camera()                         # Shakes the camera for a duration.
        .change_scene_dither()                  # Transitions to a new scene using a dithering effect.
        .change_palette()                       # Changes the color palette.
        .apply_palette_effect()                 # Applies an effect to the color palette.
        .reset_palette()                        # Resets the color palette to the default scene colors.
        .activate_debug_mode()                  # Activates debug mode.
        .deactivate_debug_mode()                # Deactivates debug mode.
        .update()                               # Updates the camera and the current scene.
        .draw()                                 # Draws the current scene.
        .run()                                  # Starts the game loop.
        ```
        """
        self.__fps = fps
        self.__scenes = scenes
        for scene in self.__scenes:
            if scene.id == default_scene_id:
                self.__current_scene = scene

        self.__camera_x = camera_x
        self.__camera_y = camera_y
        self.__camera_target_x = self.__camera_x
        self.__camera_target_y = self.__camera_y
        self.__shake_amount = 0
        self.__substracting_shake_amount = 0

        self.__transition = {
            "active": False,
            "phase": "none",
            "dither": 0.0,
            "speed": 0.05,
            "color": 0,
            "next_scene_id": None,
            "next_camera_x": 0,
            "next_camera_y": 0,
            "action": None,
        }

        self.__debug_mode = False
        self.__debug_color = 7
        self.__start_time = time.time()
        self.__current_fps = self.__fps

        pyxel.init(window_size[0], window_size[1], fps=self.__fps, quit_key=quit_key)
        pyxel.fullscreen(fullscreen)
        pyxel.mouse(mouse)

        if self.__current_scene.pyxres_path:
            pyxel.load(self.__current_scene.pyxres_path)
        pyxel.title(self.__current_scene.title)
        pyxel.screen_mode(self.__current_scene.screen_mode)
        pyxel.colors.from_list(self.__current_scene.palette)

    @property
    def camera_x(self)-> int:
        """
        Camera X
        ===
        Returns the x position of the camera.
        """
        return self.__camera_x
    
    @property
    def camera_y(self)-> int:
        """
        Camera Y
        ===
        Returns the y position of the camera.
        """
        return self.__camera_y
    
    @property
    def mouse_x(self)-> int:
        """
        Mouse X
        ===
        Returns the x position of the mouse in the world coordinates.
        """
        return self.__camera_x + pyxel.mouse_x
    
    @property
    def mouse_y(self)-> int:
        """
        Mouse Y
        ===
        Returns the y position of the mouse in the world coordinates.
        """
        return self.__camera_y + pyxel.mouse_y

    @property
    def fps(self)-> int:
        """
        FPS
        ===
        Returns the frame rate of the game.
        """
        return self.__fps

    @property
    def current_fps(self)-> int:
        """
        Current FPS
        ===
        Returns the current frame rate of the game.
        """
        return self.__current_fps

    def set_camera(self, new_x:int, new_y:int)-> None:
        """
        Set Camera
        ===
        Sets the camera position.

        Parameters
        ---
        - new_x (int): The new x position of the camera.
        - new_y (int): The new y position of the camera.
        """
        self.__camera_x = new_x
        self.__camera_y = new_y
        self.__camera_target_x = new_x
        self.__camera_target_y = new_y
        pyxel.camera(self.__camera_x, self.__camera_y)

    def move_camera_to(self, target_x:int, target_y:int)-> None:
        """
        Move Camera To
        ===
        Moves the camera to a target position.

        Parameters
        ---
        - target_x (int): The target x position.
        - target_y (int): The target y position.
        """
        self.__camera_target_x = target_x
        self.__camera_target_y = target_y

    def shake_camera(self, amount:int, substracting_shake_amount:int)-> None:
        """
        Shake Camera
        ===
        Shakes the camera for a duration.

        Parameters
        ---
        - amount (int): The intensity of the screen shake.
        - substracting_shake_amount (int): The amount taken every frame to the amount.
        """
        self.__substracting_shake_amount = abs(substracting_shake_amount)
        self.__shake_amount = abs(amount)

    def __switch_scene(self):
        t = self.__transition
        self.set_camera(t["next_camera_x"], t["next_camera_y"])
        if t["action"]:
            t["action"]()

        for scene in self.__scenes:
            if scene.id == t["next_scene_id"]:
                self.__current_scene = scene

        if self.__current_scene.pyxres_path:
            pyxel.load(self.__current_scene.pyxres_path)
        pyxel.title(self.__current_scene.title)
        pyxel.screen_mode(self.__current_scene.screen_mode)
        pyxel.colors.from_list(self.__current_scene.palette)

    def change_scene_dither(self, new_scene_id:int, speed:float, transition_color:int, next_camera_x:int=0, next_camera_y:int=0, action=None)-> None:
        """
        Change Scene Dither
        ===
        Transitions to a new scene using a dithering effect.

        Parameters
        ---
        - new_scene_id (int): The ID of the new scene.
        - speed (float): The speed of the transition.
        - transition_color (int): The color used for the transition.
        - next_camera_x (int): The x position of the camera in the new scene (default: 0).
        - next_camera_y (int): The y position of the camera in the new scene (default: 0).
        - action (function): An optional function to execute during the transition (default: None).
        """
        self.__transition = {
            "active": True,
            "phase": "fade_out",
            "dither": 0.0,
            "speed": speed,
            "color": transition_color,
            "next_scene_id": new_scene_id,
            "next_camera_x": next_camera_x,
            "next_camera_y": next_camera_y,
            "action": action,
        }

    def change_palette(self, new_palette:list)-> None:
        """
        Change Palette
        ===
        Changes the color palette.

        Parameters
        ---
        - new_palette (list): The new color palette.
        """
        pyxel.colors.from_list(new_palette)

    def apply_palette_effect(self, function_effect)-> None:
        """
        Apply Palette Effect
        ===
        Applies an effect to the color palette.

        Parameters
        ---
        - function_effect (function): A function that modifies the palette.
        """
        pyxel.colors.from_list(function_effect(self.__current_scene.palette))

    def reset_palette(self)-> None:
        """
        Reset Palette
        ===
        Resets the color palette to the default scene colors.
        """
        pyxel.colors.from_list(self.__current_scene.palette)

    def activate_debug(self, debug_color:int=7, camera_speed:int=2)-> None:
        """
        Activate Debug
        ===
        Activates the debug mode.

        Parameters
        ---
        - debug_color (int): The color used for debugging (default: 7).
        - camera_speed (int): The speed of the camera movement (default: 2).
        """
        self.__debug_mode = True
        self.__debug_color = debug_color
        self.__debug_camera_speed = camera_speed

    def deactivate_debug(self)-> None:
        """
        Deactivate Debug
        ===
        Deactivates the debug mode.
        """
        self.__debug_mode = False

    def toogle_debug(self, debug_color:int=7, camera_speed:int=2)-> None:
        """
        Toogle Debug
        ===
        Toggles the debug mode on and off.

        Parameters
        ---
        - debug_color (int): The color used for debugging (default: 7).
        - camera_speed (int): The speed of the camera movement (default: 2).
        """
        self.__debug_mode = not self.__debug_mode
        self.__debug_color = debug_color
        self.__debug_camera_speed = camera_speed

    def update(self)-> None:
        """
        Update
        ===
        Updates the camera and the current scene.
        """
        if self.__transition["active"]:
            t = self.__transition
            if t["phase"] == "fade_out":
                t["dither"] += t["speed"]
                if t["dither"] >= 1.0:
                    t["dither"] = 1.0
                    self.__switch_scene()
                    t["phase"] = "fade_in"
            elif t["phase"] == "fade_in":
                t["dither"] -= t["speed"]
                if t["dither"] <= 0.0:
                    t["dither"] = 0.0
                    t["active"] = False
                    t["phase"] = "none"
            return

        if self.__debug_mode:
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.set_camera(self.__camera_x + self.__debug_camera_speed, self.__camera_y)
            if pyxel.btn(pyxel.KEY_LEFT):
                self.set_camera(self.__camera_x - self.__debug_camera_speed, self.__camera_y)
            if pyxel.btn(pyxel.KEY_UP):
                self.set_camera(self.__camera_x, self.__camera_y - self.__debug_camera_speed)
            if pyxel.btn(pyxel.KEY_DOWN):
                self.set_camera(self.__camera_x, self.__camera_y + self.__debug_camera_speed)

        self.__camera_x += (self.__camera_target_x - self.__camera_x) * 0.1
        self.__camera_y += (self.__camera_target_y - self.__camera_y) * 0.1

        if self.__shake_amount > 0:
            amount = int(self.__shake_amount)
            pyxel.camera(self.__camera_x + random.randint(-amount, amount), self.__camera_y + random.randint(-amount, amount))
            self.__shake_amount -= self.__substracting_shake_amount
        else:
            pyxel.camera(self.__camera_x, self.__camera_y)

        self.__current_scene.update()

    def draw(self)-> None:
        """
        Draw
        ===
        Draws the current scene.
        """
        self.__current_scene.draw()
        if self.__transition["active"]:
            pyxel.dither(self.__transition["dither"])
            pyxel.rect(0, 0, pyxel.width, pyxel.height, self.__transition["color"])
            pyxel.dither(1)
        if self.__debug_mode:
            pyxel.text(self.camera_x + 5, self.camera_y + 5, f"({int(self.mouse_x)},{int(self.mouse_y)})", self.__debug_color)
            pyxel.text(self.camera_x + 5, self.camera_y + 15, f"fps:{self.__current_fps}", self.__debug_color)
        if pyxel.frame_count % self.__fps == 0:
            self.__current_fps = int(1 / (time.time() - self.__start_time))
        self.__start_time = time.time()
    
    def run(self)-> None:
        """
        Run
        ===
        Starts the game loop.
        """
        pyxel.run(self.update, self.draw)

class Scene:

    def __init__(self, id:int, title:str, update, draw, pyxres_path:str=None, palette:list=DEFAULT_PYXEL_COLORS, screen_mode:int=0)-> None:
        """
        Scene
        ===
        Represents a game scene with an update function, a draw function, and optional resources.

        Parameters
        ---
        - id (int): The unique identifier for the scene.
        - title (str): The title of the scene.
        - update (function): The function to update the scene logic.
        - draw (function): The function to render the scene.
        - pyxres_path (str): The path to the Pyxel resource file (default: None).
        - palette (list): The color palette for the scene (default: DEFAULT_PYXEL_COLORS).
        - screen_mode (int): The screen mode for the scene (default: 0).
        """
        self.__id = id
        self.__title = title
        self.__update = update
        self.__draw = draw
        self.__pyxres_path = pyxres_path
        self.__palette = palette
        self.__screen_mode = screen_mode

    @property
    def id(self)-> int:
        """
        Id
        ===
        Returns the unique identifier of the scene.
        """
        return self.__id
    
    @property
    def title(self)-> str:
        """
        Title
        ===
        Returns the title of the scene.
        """
        return self.__title

    @property
    def update(self):
        """
        Update
        ===
        Returns the update function of the scene.
        """
        return self.__update
    
    @property
    def draw(self):
        """
        Draw
        ===
        Returns the draw function of the scene.
        """
        return self.__draw
    
    @property
    def pyxres_path(self)-> str:
        """
        Pyxres Path
        ===
        Returns the path to the Pyxel resource file.
        """
        return self.__pyxres_path
    
    @property
    def palette(self)-> list:
        """
        Palette
        ===
        Returns the color palette for the scene.
        """
        return self.__palette

    @property
    def screen_mode(self)-> int:
        """
        Screen Mode
        ===
        Returns the screen mode for the scene.
        """
        return self.__screen_mode

class Sprite:

    def __init__(self, img:int, u:int, v:int, width:int, height:int, colkey:int=None)-> None:
        """
        Sprite
        ===
        Represents a graphical sprite with properties for rendering.

        Parameters
        ---
        - img (int): The image bank index.
        - u (int): The x-coordinate of the sprite in the image bank.
        - v (int): The y-coordinate of the sprite in the image bank.
        - width (int): The width of the sprite.
        - height (int): The height of the sprite.
        - colkey (int|None): The color key for transparency (default: None).
        """
        self.__img = img
        self.__u = u
        self.__v= v
        self.__width = width    
        self.__height = height
        self.__colkey = 0 if colkey == 0 else colkey

    @property
    def img(self)-> int:
        """
        Img
        ===
        Gets the image bank index.
        """
        return self.__img

    @property
    def u(self)-> int:
        """
        U
        ===
        Gets the x-coordinate of the sprite in the image bank.
        """
        return self.__u
    
    @property
    def v(self)-> int:
        """
        V
        ===
        Gets the y-coordinate of the sprite in the image bank.
        """
        return self.__v

    @property
    def width(self)-> int:
        """
        Width
        ===
        Gets the width of the sprite.
        """
        return self.__width

    @property
    def height(self)-> int:
        """
        Height
        ===
        Gets the height of the sprite.
        """
        return self.__height
    
    @property
    def colkey(self)-> int|None:
        """
        Colkey
        ===
        Gets the color key for transparency.
        """
        return self.__colkey

class Text:

    def __init__(self, text:str, x:int, y:int, text_colors:list|int, font_size:int=0, anchor:int=ANCHOR_TOP_LEFT, color_mode:int=NORMAL_COLOR_MODE, color_speed:int|float=5, relative:bool=False, wavy:bool=False, wave_speed:int|float=10, wave_height:int=3, shadow:bool=False, shadow_color:int=0, shadow_offset:int=1, glitch_intensity:int=0, underline:bool=False, underline_color:int=0, blinking:bool=False, blinking_frames:int=30)-> None:
        """
        Text
        ===
        Creates a text object.

        Parameters
        ---
        - text (str): The text to display.
        - x (int): The x-coordinate of the text.
        - y (int): The y-coordinate of the text.
        - text_colors (list | int): The colors of the text.
        - font_size (int): The font size, if it is 0, it uses the default pyxel text else our custom font (default: 0).
        - anchor (int): The anchor of the text (default: ANCHOR_TOP_LEFT).
        - color_mode (int): The color mode (default: NORMAL_COLOR_MODE).
        - color_speed (int | float): The color speed (default: 5).
        - relative (bool): Whether the text is relative to the camera (default: False).
        - wavy (bool): Whether the text is wavy (default: False).
        - wave_speed (int | float): The speed of the wave (default: 10).
        - wave_height (int): The height of the wave (default: 3).
        - shadow (bool): Whether the text has a shadow (default: False).
        - shadow_color (int): The color of the shadow (default: 0).
        - shadow_offset (int): The offset of the shadow (default: 1).
        - glitch_intensity (int): The intensity of the glitch effect (default: 0).
        - underline (bool): Whether the text is underlined. You can't underline the text if the font size is 0 (default: False).
        - underline_color (int): The color of the underline (default: 0).
        - blinking (bool): Whether the text is blinking (default: False).
        - blinking_frames (int): The number of frames between each blink (default: 30).

        Methods
        ---
        ```
        .update()    # Updates the text.
        .draw()      # Draws the text.
        ```
        """
        self.text = text
        self.x = x
        self.y = y
        self.__font_size = font_size
        self.__text_width, self.__text_height = text_size(text, font_size)
        self.__anchor = anchor
        self.__relative = relative
        self.__wavy = wavy
        self.__wave_speed = wave_speed
        self.__wave_height = wave_height
        self.__shadow = shadow
        self.__shadow_color = shadow_color
        self.__shadow_x = self.x + shadow_offset
        self.__shadow_y = self.y + shadow_offset
        self.__shadow_offset = shadow_offset
        self.__glitch_intensity = glitch_intensity
        self.__underline = underline
        self.__underline_color = underline_color
        self.__blinking = blinking
        self.__blinking_frames = blinking_frames

        self.__text_colors = [text_colors] if isinstance(text_colors, int) else text_colors
        self.__original_text_colors = [x for x in self.__text_colors]
        self.__color_mode = color_mode
        self.__color_speed = color_speed
        self.__last_change_color_time = pyxel.frame_count

        if "\n" not in self.text:
            if anchor in [ANCHOR_TOP_RIGHT, ANCHOR_BOTTOM_RIGHT, ANCHOR_RIGHT]:
                self.x -= self.__text_width
            if anchor in [ANCHOR_BOTTOM_LEFT, ANCHOR_BOTTOM_RIGHT, ANCHOR_BOTTOM]:
                self.y -= self.__text_height
            if anchor in [ANCHOR_TOP, ANCHOR_BOTTOM, ANCHOR_CENTER]:
                self.x -= self.__text_width // 2
            if anchor in [ANCHOR_LEFT, ANCHOR_RIGHT, ANCHOR_CENTER]:
                self.y -= self.__text_height // 2

    def __draw_line(self, text:str, y:int, camera_x:int=0, camera_y:int=0)-> None:
        """
        Draw Line
        ===
        Draws a line of text at the given y-coordinate.

        Parameters
        ---
        - text (str): The text to be drawn.
        - y (int): The y-coordinate of the line.
        - camera_x (int): The x-coordinate of the camera (default: 0).
        - camera_y (int): The y-coordinate of the camera (default: 0).
        """
        x = self.x
        text_width, text_height = text_size(text, self.__font_size)

        if self.__shadow:
            Text(text, x + self.__shadow_offset, y + self.__shadow_offset, self.__shadow_color, self.__font_size, self.__anchor, relative=self.__relative, underline=self.__underline, underline_color=self.__shadow_color, wavy=self.__wavy, wave_height=self.__wave_height, wave_speed=self.__wave_speed).draw(camera_x, camera_y)

        if self.__anchor in [ANCHOR_TOP_RIGHT, ANCHOR_BOTTOM_RIGHT, ANCHOR_RIGHT]:
            x -= text_width
        if self.__anchor in [ANCHOR_BOTTOM_LEFT, ANCHOR_BOTTOM_RIGHT, ANCHOR_BOTTOM]:
            y -= self.__text_height
        if self.__anchor in [ANCHOR_TOP, ANCHOR_BOTTOM, ANCHOR_CENTER]:
            x -= text_width // 2
        if self.__anchor in [ANCHOR_LEFT, ANCHOR_RIGHT, ANCHOR_CENTER]:
            y -= self.__text_height // 2

        if self.__relative:
            x += camera_x
            y += camera_y

        char_x = x

        if self.__font_size > 0:
            for char_index, char in enumerate(text):
                char_y = y + math.cos(pyxel.frame_count / self.__wave_speed + char_index * 0.3) * self.__wave_height if self.__wavy else y

                if char in characters_matrices:
                    char_matrix = characters_matrices[char]
                    char_width = len(char_matrix[0]) * self.__font_size

                    x += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                    char_y += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                    
                    for row_index, row in enumerate(char_matrix):
                        for col_index, pixel in enumerate(row):
                            if pixel:
                                pyxel.rect(x + col_index * self.__font_size, char_y + row_index * self.__font_size + (1 * self.__font_size if char in "gjpqy" else 0), self.__font_size, self.__font_size, self.__text_colors[char_index % len(self.__text_colors)])
                    
                    x += char_width + self.__font_size

            if self.__underline:
                pyxel.rect(char_x, y + text_height - self.__font_size, text_width, self.__font_size, self.__underline_color)
        else:
            for char_index, char in enumerate(text):
                char_y = y + math.cos(pyxel.frame_count / self.__wave_speed + char_index * 0.3) * self.__wave_height if self.__wavy else y
                x += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                char_y += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                pyxel.text(x, char_y, char, self.__text_colors[char_index % len(self.__text_colors)])
                x += 4

    def update(self)-> None:
        """
        Update
        ===
        Updates the text.
        """
        if self.__color_mode and pyxel.frame_count - self.__last_change_color_time >= self.__color_speed:
            if self.__color_mode == ROTATING_COLOR_MODE:
                self.__last_change_color_time = pyxel.frame_count
                self.__text_colors = [self.__text_colors[-1]] + self.__text_colors[:-1]
            elif self.__color_mode == RANDOM_COLOR_MODE:
                self.__last_change_color_time = pyxel.frame_count
                self.__text_colors = [random.choice(self.__original_text_colors) for _ in range(len(self.text))]

    def draw(self, camera_x:int=0, camera_y:int=0)-> None:
        """
        Draw
        ===
        Draws the text.

        Parameters
        ---
        - camera_x (int): The x-coordinate of the camera (default: 0).
        - camera_y (int): The y-coordinate of the camera (default: 0).
        """
        if self.__blinking and pyxel.frame_count % (self.__blinking_frames) >= self.__blinking_frames // 2:
            return

        x = self.x
        y = self.y

        if "\n" in self.text:
            lines = self.text.split("\n")
            for i, line in enumerate(lines):
                if self.__font_size > 0:
                    self.__draw_line(line, y + i * (9 * self.__font_size), camera_x, camera_y)
                else:
                    self.__draw_line(line, y + i * 6, camera_x, camera_y)
            return
        
        if self.__relative:
            x += camera_x
            y += camera_y

        if self.__shadow:
            Text(self.text, self.__shadow_x, self.__shadow_y, self.__shadow_color, self.__font_size, self.__anchor, relative=self.__relative, underline=self.__underline, underline_color=self.__shadow_color, wavy=self.__wavy, wave_height=self.__wave_height, wave_speed=self.__wave_speed).draw(camera_x, camera_y)

        if self.__font_size > 0:
            for char_index, char in enumerate(self.text):
                char_y = y + math.cos(pyxel.frame_count / self.__wave_speed + char_index * 0.3) * self.__wave_height if self.__wavy else y

                if char in characters_matrices:
                    char_matrix = characters_matrices[char]
                    char_width = len(char_matrix[0]) * self.__font_size

                    x += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                    char_y += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                    
                    for row_index, row in enumerate(char_matrix):
                        for col_index, pixel in enumerate(row):
                            if pixel:
                                pyxel.rect(x + col_index * self.__font_size, char_y + row_index * self.__font_size + (1 * self.__font_size if char in "gjpqy" else 0), self.__font_size, self.__font_size, self.__text_colors[char_index % len(self.__text_colors)])
                    
                    x += char_width + self.__font_size

            if self.__underline:
                pyxel.rect(self.x, y + self.__text_height - self.__font_size, self.__text_width, self.__font_size, self.__underline_color)
        else:
            for char_index, char in enumerate(self.text):
                char_y = y + math.cos(pyxel.frame_count / self.__wave_speed + char_index * 0.3) * self.__wave_height if self.__wavy else y
                x += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                char_y += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                pyxel.text(x, char_y, char, self.__text_colors[char_index % len(self.__text_colors)])
                x += 4

class Button:

    def __init__(self, text:str, x:int, y:int, background_color:int, text_colors:list|int, hover_background_color:int, hover_text_colors:list|int, font_size:int=1, border:bool=False, border_color:int=0, color_mode:int=NORMAL_COLOR_MODE, color_speed:int=10, relative:bool=True, anchor:int=ANCHOR_TOP_LEFT, command=None)-> None:
        """
        Button
        ===
        Creates a button.

        Parameters
        ---
        - text (str): The text of the button.
        - x (int): The x position of the button.
        - y (int): The y position of the button.
        - background_color (int): The background color of the button.
        - text_colors (list | int): The colors of the text.
        - hover_background_color (int): The background color of the button when hovered.
        - hover_text_colors (list | int): The colors of the text when hovered.
        - font_size (int): The size of the font (default: 1).
        - border (bool): Whether the button has a border (default: False).
        - border_color (int): The color of the border (default: 0).
        - color_mode (int): The color mode (default: NORMAL_COLOR_MODE).
        - color_speed (int): The speed of the color change (default: 10).
        - relative (bool): Whether the button is relative to the camera (default: True).
        - anchor (int): The anchor of the button (default: ANCHOR_TOP_LEFT).
        - command (function): The command to execute when the button is clicked (default: None).

        Methods
        ---
        ```
        .is_hovered()    # Returns whether the button is hovered.
        .update()        # Updates the button.
        .draw()          # Draws the button.
        ```
        """
        self.__x = x
        self.__y = y
        self.__width, self.__height = text_size(text, font_size)
        self.__width += 4 if border else 2
        self.__height += 4 if border else 2
        self.__background_color = background_color
        self.__hover_background_color = hover_background_color
        self.__border = border
        self.__border_color = border_color
        self.__relative = relative
        self.__command = command

        if anchor in [ANCHOR_TOP_RIGHT, ANCHOR_BOTTOM_RIGHT, ANCHOR_RIGHT]:
            self.__x -= self.__width
        if anchor in [ANCHOR_BOTTOM_LEFT, ANCHOR_BOTTOM_RIGHT, ANCHOR_BOTTOM]:
            self.__y -= self.__height
        if anchor in [ANCHOR_TOP, ANCHOR_BOTTOM, ANCHOR_CENTER]:
            self.__x -= self.__width // 2
        if anchor in [ANCHOR_LEFT, ANCHOR_RIGHT, ANCHOR_CENTER]:
            self.__y -= self.__height // 2

        self.__text = Text(text, self.__x + 2 if border else self.__x + 1, self.__y + 2 if border else self.__y + 1, text_colors, font_size, color_mode=color_mode, color_speed=color_speed, relative=relative)
        self.__hover_text = Text(text, self.__x + 2 if border else self.__x + 1, self.__y + 2 if border else self.__y + 1, hover_text_colors, font_size, color_mode=color_mode, color_speed=color_speed, relative=relative)

    def is_hovered(self, camera_x:int=0, camera_y:int=0)-> bool:
        """
        Is Hovered
        ===
        Returns whether the button is hovered.

        Parameters
        ---
        - camera_x (int): The x position of the camera (default: 0).
        - camera_y (int): The y position of the camera (default: 0).

        Returns
        ---
        - (bool): Whether the button is hovered.
        """
        if self.__x <= pyxel.mouse_x < self.__x + self.__width and self.__y <= pyxel.mouse_y < self.__y + self.__height and self.__relative:
            return True
        if self.__x <= camera_x + pyxel.mouse_x < self.__x + self.__width and self.__y <= camera_y + pyxel.mouse_y < self.__y + self.__height and not self.__relative:
            return True
        
    def update(self, camera_x:int=0, camera_y:int=0)-> None:
        """
        Update
        ===
        Updates the button.

        Parameters
        ---
        - camera_x (int): The x position of the camera (default: 0).
        - camera_y (int): The y position of the camera (default: 0).
        """
        self.__text.update()
        self.__hover_text.update()
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.is_hovered(camera_x, camera_y) and self.__command:
            self.__command()

    def draw(self, camera_x:int=0, camera_y:int=0)-> None:
        """
        Draw
        ===
        Draws the button.

        Parameters
        ---
        - camera_x (int): The x position of the camera (default: 0).
        - camera_y (int): The y position of the camera (default: 0).
        """
        x = camera_x + self.__x if self.__relative else self.__x
        y = camera_y + self.__y if self.__relative else self.__y
        if self.is_hovered(camera_x, camera_y):
            pyxel.rect(x, y, self.__width, self.__height, self.__hover_background_color)
            self.__hover_text.draw(camera_x, camera_y)
        else:
            pyxel.rect(x, y, self.__width, self.__height, self.__background_color)
            self.__text.draw(camera_x, camera_y)
        if self.__border:
            pyxel.rectb(x, y, self.__width, self.__height, self.__border_color)

class IconButton:

    def __init__(self, x:int, y:int, background_color:int, hover_background_color:int, sprite:Sprite, border:bool=False, border_color:int=0, relative:bool=True, anchor:int=ANCHOR_TOP_LEFT, command=None)-> None:
        """
        Icon Button
        ===
        Creates an icon button.

        Parameters
        ---
        - x (int): The x position of the button.
        - y (int): The y position of the button.
        - background_color (int): The background color of the button.
        - hover_background_color (int): The background color when the button is hovered.
        - sprite (Sprite): The sprite representing the icon of the button.
        - border (bool): True if you want a border (default: False).
        - border_color (int): The color of the border (default: 0).
        - relative (bool): True if you want the button to be relative to the camera (default: True).
        - anchor (int): The anchor of the button placement (default: ANCHOR_TOP_LEFT).
        - command (callable): The command you want to be executed when clicking on the button (default: None).

        Methods
        ---
        ```
        .is_hovered()    # Returns if the button is hovered.
        .update()        # Updates the icon button.
        .draw()          # Draws the icon button.
        ```
        """
        self.__x = x + 1 if not border else x + 2
        self.__y = y + 1 if not border else y + 2
        self.__width = sprite.width + 2 if not border else sprite.width + 4
        self.__height = sprite.height + 2 if not border else sprite.height + 4
        self.__background_color = background_color
        self.__hover_background_color = hover_background_color
        self.__sprite = sprite
        self.__border = border
        self.__border_color = border_color
        self.__relative = relative
        self.__command = command

        if anchor in [ANCHOR_TOP_RIGHT, ANCHOR_BOTTOM_RIGHT, ANCHOR_RIGHT]:
            self.__x -= self.__width
        if anchor in [ANCHOR_BOTTOM_LEFT, ANCHOR_BOTTOM_RIGHT, ANCHOR_BOTTOM]:
            self.__y -= self.__height
        if anchor in [ANCHOR_TOP, ANCHOR_BOTTOM, ANCHOR_CENTER]:
            self.__x -= self.__width // 2
        if anchor in [ANCHOR_LEFT, ANCHOR_RIGHT, ANCHOR_CENTER]:
            self.__y -= self.__height // 2

    def is_hovered(self, camera_x:int=0, camera_y:int=0)-> bool:
        """
        Is Hovered
        ===
        Returns if the button is hovered.

        Parameters
        ---
        - camera_x (int): The x position of the camera (default: 0).
        - camera_y (int): The y position of the camera (default: 0).

        Returns
        ---
        - (bool): True if the button is hovered.
        """
        if self.__x - 2 < pyxel.mouse_x < self.__x + self.__sprite.width + 1 and self.__y - 2 < pyxel.mouse_y < self.__y + self.__sprite.height + 1 and self.__relative:
            return True
        elif self.__x - 2 < camera_x + pyxel.mouse_x < self.__x + self.__sprite.width + 1 and self.__y - 2 < camera_y + pyxel.mouse_y < self.__y + self.__sprite.height + 1 and not self.__relative:
            return True
        
    def update(self, camera_x:int=0, camera_y:int=0)-> None:
        """
        Update
        ===
        Updates the icon button.

        Parameters
        ---
        - camera_x (int): The x position of the camera (default: 0).
        - camera_y (int): The y position of the camera (default: 0).
        """
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.is_hovered(camera_x, camera_y) and self.__command:
            self.__command()

    def draw(self, camera_x:int=0, camera_y:int=0)-> None:
        """
        Draw
        ===
        Draws the icon button.

        Parameters
        ---
        - camera_x (int): The x position of the camera (default: 0).
        - camera_y (int): The y position of the camera (default: 0).
        """
        x = camera_x + self.__x if self.__relative else self.__x
        y = camera_y + self.__y if self.__relative else self.__y

        if self.__border:
            pyxel.rectb(x - 2, y - 2, self.__sprite.width + 4, self.__sprite.height + 4, self.__border_color)
        if self.is_hovered(camera_x, camera_y):
            pyxel.rect(x - 1, y - 1, self.__sprite.width + 2, self.__sprite.height + 2, self.__hover_background_color)
        else:
            pyxel.rect(x - 1, y - 1, self.__sprite.width + 2, self.__sprite.height + 2, self.__background_color)
        pyxel.blt(x, y, self.__sprite.img, self.__sprite.u, self.__sprite.v, self.__sprite.width, self.__sprite.height, self.__sprite.colkey)

class UIBar:

    def __init__(self, x:int, y:int, width:int, height:int, border_color:int, bar_color:int, starting_value:int, max_value:int, relative:bool=True, horizontal:bool=True, regen:bool=False, speed_regen:int=0.5, value_regen:int=1, anchor:int=ANCHOR_TOP_LEFT)-> None:
        """
        UIBar
        ===
        Creates a UI bar.

        Parameters
        ---
        - x (int): The x-coordinate of the bar.
        - y (int): The y-coordinate of the bar.
        - width (int): The width of the bar.
        - height (int): The height of the bar.
        - border_color (int): The color of the border.
        - bar_color (int): The color of the bar.
        - starting_value (int): The starting value of the bar.
        - max_value (int): The maximum value of the bar.
        - relative (bool): Whether the bar is relative to the camera (default: True).
        - horizontal (bool): Whether the bar is horizontal or vertical (default: True).
        - regen (bool): Whether the bar regenerates over time (default: False).
        - speed_regen (int): The speed of the regeneration (default: 0.5).
        - value_regen (int): The value of the regeneration (default: 1).
        - anchor (int): The anchor of the bar (default: ANCHOR_TOP_LEFT).

        Methods
        ---
        ```
        .update()  # Updates the bar.
        .draw()    # Draws the bar.
        ```
        """
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__border_color = border_color
        self.__bar_color = bar_color

        self.current_value = starting_value
        self.max_value = max_value
        self.__relative = relative
        self.__horizontal = horizontal

        self.__regen = regen
        self.__speed_regen = speed_regen
        self.__regen_timer = 0
        self.__value_regen = value_regen
        self.__bar_width = 0
        self.__bar_height = 0
        
        if anchor in [ANCHOR_TOP_RIGHT, ANCHOR_BOTTOM_RIGHT, ANCHOR_RIGHT]:
            self.__x -= (self.__width + 2)
        if anchor in [ANCHOR_BOTTOM_LEFT, ANCHOR_BOTTOM_RIGHT, ANCHOR_BOTTOM]:
            self.__y -= (self.__height + 2)
        if anchor in [ANCHOR_TOP, ANCHOR_BOTTOM, ANCHOR_CENTER]:
            self.__x -= (self.__width + 2) // 2
        if anchor in [ANCHOR_LEFT, ANCHOR_RIGHT, ANCHOR_CENTER]:
            self.__y -= (self.__height + 2) // 2

    def update(self)-> None:
        """
        Update
        ===
        Updates the bar.
        """
        self.__regen_timer += 1
        if self.current_value < 0:
            self.current_value = 0
        if self.current_value < self.max_value and self.__regen and self.__regen_timer >= self.__speed_regen:
            self.__regen_timer = 0
            self.current_value += self.__value_regen
        while self.current_value > self.max_value:
            self.current_value -= 1
        self.__bar_width = self.__width * self.current_value / self.max_value
        self.__bar_height = self.__height * self.current_value / self.max_value

    def draw(self, camera_x:int=0, camera_y:int=0)-> None:
        """
        Draw
        ===
        Draws the bar.

        Parameters
        ---
        - camera_x (int): The x position of the camera.
        - camera_y (int): The y position of the camera.
        """
        if self.__relative:
            if self.__horizontal:
                pyxel.rect(camera_x + self.__x + 1, camera_y + self.__y + 1, self.__bar_width, self.__height, self.__bar_color)
                pyxel.rectb(camera_x + self.__x, camera_y + self.__y, self.__width + 2, self.__height + 2, self.__border_color)
            else:
                pyxel.rect(camera_x + self.__x + 1, camera_y + self.__y + self.__height - self.__bar_height + 1, self.__width, self.__bar_height, self.__bar_color)
                pyxel.rectb(camera_x + self.__x, camera_y + self.__y, self.__width + 2, self.__height + 2, self.__border_color)
        else:
            if self.__horizontal:
                pyxel.rect(self.__x + 1, self.__y + 1, self.__bar_width, self.__height, self.__bar_color)
                pyxel.rectb(self.__x, self.__y, self.__width + 2, self.__height + 2, self.__border_color)
            else:
                pyxel.rect(self.__x + 1, self.__y + self.__height - self.__bar_height + 1, self.__width, self.__bar_height, self.__bar_color)
                pyxel.rectb(self.__x, self.__y, self.__width + 2, self.__height + 2, self.__border_color)

class RectangleParticle:

    def __init__(self, x:int, y:int, width:int, height:int, colors:list|int, lifespan:int,  speed:int|float, target_x:int, target_y:int, growing_speed:int|float=0, acceleration_speed:int|float=0, dither_duration:int|float=0, hollow:bool=False)-> None:
        """
        Rectangle Particle
        ===
        Represents a rectangular particle that moves towards a target position while changing size, color, and opacity.

        Parameters
        ---
        - x (int): Initial x-coordinate.
        - y (int): Initial y-coordinate.
        - width (int): Initial width of the particle.
        - height (int): Initial height of the particle.
        - colors (list | int): Color or list of colors used in the animation.
        - lifespan (int): Lifespan of the particle before it disappears.
        - speed (int | float): Initial speed of movement towards the target.
        - target_x (int): Target x-coordinate.
        - target_y (int): Target y-coordinate.
        - growing_speed (int | float): Rate at which the particle grows per frame (default: 0).
        - acceleration_speed (int | float): Rate at which the particle accelerates per frame (default: 0).
        - dither_duration (int | float): Duration for which dithering effect occurs (default: 0).
        - hollow (bool): If True, draws a hollow rectangle instead of a filled one (default: False).

        Methods
        ---
        ```
        .update()    # Updates the particle's position, size, color, and lifespan.
        .draw()      # Draws the particle using Pyxel.
        ```
        """
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__colors = [colors] if isinstance(colors, int) else colors
        self.__colors_length = len(self.__colors)
        self.__current_color = 0
        self.__lifespan = round(lifespan / self.__colors_length) * self.__colors_length
        self.__starting_lifespan = self.__lifespan
        self.__growing_speed = growing_speed
        self.__acceleration_speed = acceleration_speed
        self.__hollow = hollow
        self.__dither = 1
        self.__dither_duration = dither_duration

        self.__direction_x = -1 if target_x - self.__x < 0 else 1
        self.__direction_y = -1 if target_y - self.__y < 0 else 1

        direction_x = target_x - self.__x
        direction_y = target_y - self.__y
        distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
        if distance != 0:
            direction_x /= distance
            direction_y /= distance

        self.__speed_x = direction_x * speed
        self.__speed_y = direction_y * speed

    @property
    def lifespan(self)-> int:
        """
        Lifespan
        ===
        Returns the current lifespan of the particle.
        """
        return self.__lifespan

    def update(self)-> None:
        """
        Update
        ===
        Updates the particle's position, size, color, and lifespan.
        """
        self.__speed_x = abs(self.__speed_x) + self.__acceleration_speed
        self.__speed_y = abs(self.__speed_y) + self.__acceleration_speed

        self.__x += abs(self.__speed_x) * self.__direction_x
        self.__y += abs(self.__speed_y) * self.__direction_y

        self.__lifespan -= 1
        self.__width += self.__growing_speed
        self.__height += self.__growing_speed

        if self.__width <= 0 or self.__height <= 0:
            self.__lifespan = 0

        if self.__lifespan <= self.__dither_duration and self.__dither_duration:
            self.__dither -= 1 / self.__dither_duration

        if self.__lifespan % (self.__starting_lifespan / self.__colors_length) == 0 and self.__lifespan != 0:
            self.__current_color = (self.__current_color + 1) % self.__colors_length

    def draw(self)-> None:
        """
        Draw
        ===
        Draws the particle using Pyxel.
        """
        pyxel.dither(self.__dither)
        if self.__hollow:   
            pyxel.rectb(self.__x - self.__width / 2, self.__y - self.__height / 2, self.__width, self.__height, self.__colors[self.__current_color])
        else:             
            pyxel.rect(self.__x - self.__width / 2, self.__y - self.__height / 2, self.__width, self.__height, self.__colors[self.__current_color])
        pyxel.dither(1)

class ParticleManager:

    def __init__(self)-> None:
        """
        Particle Manager
        ===
        Manages a collection of particles, allowing for their addition, updating, and drawing. It supports the removal of expired particles.

        Methods
        ---
        ```
        .reset()           # Resets the particle list by clearing all particles.
        .add_particle()    # Adds a new particle to the particle list.
        .update()          # Updates the state of all particles, removing expired ones.
        .draw()            # Draws all active particles to the screen.
        ```
        """
        self.__particles :list[RectangleParticle] = []

    def reset(self)-> None:
        """
        Reset
        ===
        Clears the particle list, effectively removing all particles.
        """
        self.__particles = []

    def add_particle(self, new_particle:RectangleParticle)-> None:
        """
        Add Particle
        ===
        Adds a new particle to the particle manager's list.

        Parameters
        ---
        - new_particle (RectangleParticle): The particle to be added to the manager.
        """
        self.__particles.append(new_particle)

    def update(self)-> None:
        """
        Update
        ===
        Updates the state of all particles in the list. Removes particles whose lifespan has expired.
        """
        for particle in self.__particles:
            particle.update()

        self.__particles = [particle for particle in self.__particles if particle.lifespan > 0]

    def draw(self)-> None:
        """
        Draw
        ===
        Draws all active particles to the screen.
        """
        for particle in self.__particles:
            particle.draw()

def text_size(text:str, font_size:int=1)-> tuple:
    """
    Text Size
    ===
    Calculates the size of a text based on its font size.

    Parameters
    ---
    - text (str): The text to calculate the size for.
    - font_size (int): The font size (default: 1).

    Returns
    ---
    - (tuple): The width and height of the text.
    """
    lines = text.split("\n")
    if font_size == 0:
        return (max(len(line) * 4 for line in lines), 6 * len(lines))
    text_width = max(sum(len(characters_matrices[char][0]) * font_size + font_size for char in line) - font_size for line in lines)
    text_height = (9 * font_size + 1) * len(lines)

    return (text_width, text_height)

def draw_brick_wall(x:int, y:int, width:int, height:int, brick_width:int, brick_height:int, color:int, mortar_color:int, mortar_thickness:int=1)-> None:
    """
    Draw Brick Wall
    ===
    Draws a brick wall pattern with mortar.
    
    Parameters
    ---
    - x (int): The x-coordinate of the top-left corner.
    - y (int): The y-coordinate of the top-left corner.
    - width (int): The width of the wall.
    - height (int): The height of the wall.
    - brick_width (int): The width of each brick.
    - brick_height (int): The height of each brick.
    - color (int): The color of the bricks.
    - mortar_color (int): The color of the mortar.
    - mortar_thickness (int): The thickness of the mortar (default: 1).
    """
    pyxel.rect(x, y, width, height, mortar_color)
    
    row = 0
    while row * (brick_height + mortar_thickness) < height:
        offset = (row % 2) * (brick_width + mortar_thickness) // 2
        
        col = 0
        while col * (brick_width + mortar_thickness) - offset < width:
            brick_x = x + col * (brick_width + mortar_thickness) - offset
            brick_y = y + row * (brick_height + mortar_thickness)
            
            if brick_x < x + width and brick_y < y + height:
                actual_width = min(brick_width, x + width - brick_x)
                actual_height = min(brick_height, y + height - brick_y)
                if actual_width > 0 and actual_height > 0:
                    pyxel.rect(brick_x, brick_y, actual_width, actual_height, color)
            
            col += 1
        row += 1

def rounded_rect(x:int, y:int, width:int, height:int, corner_radius:int, color:int)-> None:
    """
    Rounded Rectangle
    ===
    Draws a rectangle with rounded corners filled with a given color.
    
    Parameters
    ---
    - x (int): The x-coordinate of the top-left corner.
    - y (int): The y-coordinate of the top-left corner.
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.
    - corner_radius (int): The radius of the corner rounding.
    - color (int): The color of the rectangle.
    - fill (bool): Whether to fill the rectangle.
    """
    corner_radius = min(corner_radius, min(width, height) // 2)
    corner_radius = int(corner_radius)

    pyxel.rect(x + corner_radius, y, width - 2 * corner_radius, height, color)
    pyxel.rect(x, y + corner_radius, width, height - 2 * corner_radius, color)
    
    for cx, cy, sx, sy in [(x + corner_radius, y + corner_radius, -1, -1), (x + width - corner_radius - 1, y + corner_radius, 1, -1), (x + corner_radius, y + height - corner_radius - 1, -1, 1), (x + width - corner_radius - 1, y + height - corner_radius - 1, 1, 1)]:
        for i in range(corner_radius + 1):
            for j in range(corner_radius + 1):
                if i*i + j*j <= corner_radius*corner_radius:
                    pyxel.pset(cx + sx * i, cy + sy * j, color)

def rounded_rectb(x:int, y:int, width:int, height:int, corner_radius:int, color:int)-> None:
    """
    Rounded Rectangle
    ===
    Draws a rectangle with rounded corners without fill.
    
    Parameters
    ---
    - x (int): The x-coordinate of the top-left corner.
    - y (int): The y-coordinate of the top-left corner.
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.
    - corner_radius (int): The radius of the corner rounding.
    - color (int): The color of the rectangle.
    - fill (bool): Whether to fill the rectangle.
    """
    corner_radius = min(corner_radius, min(width, height) // 2)

    pyxel.line(x + corner_radius, y, x + width - corner_radius - 1, y, color)
    pyxel.line(x + corner_radius, y + height - 1, x + width - corner_radius - 1, y + height - 1, color)
    pyxel.line(x, y + corner_radius, x, y + height - corner_radius - 1, color)
    pyxel.line(x + width - 1, y + corner_radius, x + width - 1, y + height - corner_radius - 1, color)
    
    for cx, cy, sx, sy in [(x + corner_radius, y + corner_radius, -1, -1), (x + width - corner_radius - 1, y + corner_radius, 1, -1), (x + corner_radius, y + height - corner_radius - 1, -1, 1), (x + width - corner_radius - 1, y + height - corner_radius - 1, 1, 1)]:
        for i in range(corner_radius + 1):
            for j in range(corner_radius + 1):
                dist = math.sqrt(i*i + j*j)
                if corner_radius - 0.5 <= dist <= corner_radius + 0.5:
                    pyxel.pset(cx + sx * i, cy + sy * j, color)

def hex_to_rgb(hex_val:int)-> tuple:
    """
    Hex to RGB
    ===
    Converts a hexadecimal color value to RGB.

    Parameters
    ---
    - hex_val (int): The hexadecimal color value.

    Returns
    ---
    - (tuple): The RGB values as a tuple (r, g, b).
    """
    r = (hex_val >> 16) & 0xFF
    g = (hex_val >> 8) & 0xFF
    b = hex_val & 0xFF
    return r, g, b

def rgb_to_hex(r:int, g:int, b:int)-> int:
    """
    RGB to Hex
    ===
    Converts RGB values to a hexadecimal color value.

    Parameters
    ---
    - r (int): The red component (0-255).
    - g (int): The green component (0-255).
    - b (int): The blue component (0-255).

    Returns
    ---
    - (int): The hexadecimal color value.
    """
    return int(f"0x{r:02X}{g:02X}{b:02X}", 16)

def neon_palette(original_palette:list)-> list:
    """
    Neon Palette
    ===
    Creates a neon palette by converting the original palette to grayscale and applying a neon effect.

    Parameters
    ---
    - original_palette (list): The original palette to create a neon effect for.

    Returns
    ---
    - (list): The neon palette.
    """
    palette = []
    for color in original_palette:
        r, g, b = hex_to_rgb(color)
        brightness = (r + g + b) / 3
        if brightness > 30:
            max_val = max(r, g, b)
            if max_val == r:
                r = min(255, int(r * 1.5))
            elif max_val == g:
                g = min(255, int(g * 1.5))
            elif max_val == b:
                b = min(255, int(b * 1.5))
        palette.append(rgb_to_hex(r, g, b))

    return palette

def psychedelic_shifting_palette(original_palette:list)-> list:
    """
    Psychedelic Shifting Palette
    ===
    Creates a psychedelic shifting palette by shifting the hue of the original palette.

    Parameters
    ---
    - original_palette (list): The original palette to create a psychedelic shifting effect for.

    Returns
    ---
    - (list): The psychedelic shifting palette.
    """
    palette = []
    for color in original_palette:
        r, g, b = hex_to_rgb(color)
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        h = (h + time.time() % 1) % 1
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        palette.append(rgb_to_hex(int(r * 255), int(g * 255), int(b * 255)))
        
    return palette

def midi_notes_to_pyxel(notes:list)-> str:
    note_names = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
    pyxel_notes = []
    for n in notes:
        if n == -1:
            pyxel_notes.append("r")
        else:
            semitone_offset = n - 33
            octave = 2 + (semitone_offset // 12)
            note_index = semitone_offset % 12
            pyxel_notes.append(f"{note_names[note_index]}{octave}")

    string = ""
    for char in " ".join(pyxel_notes):
        if char != "-":
            string += char
    return string

PALETTE = [0x000000, 0xFFFFFF, 0xe4a672, 0xb86f50,
           0x743f39, 0x3f2832, 0x9e2835, 0xe53b44,
           0xfb922b, 0xffe762, 0x63c64d, 0x327345,
           0x193d3f, 0xafbfd2, 0x149ef5, 0x0484d1]

EXTENDED_CHANNELS = [
    (0.125, 0),     #? Sounds
    (0.125, 0),     #? Sounds
    (0.1 / 2.0, 0), #? Melody
    (0.1, 0)        #? Bass Line
]

EXTENDED_TONES = [
    (1.0, 0, [8, 9, 10, 11, 12, 13, 14, 15, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7]),     #? T
    (0.3, 0, [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), #? S
    (0.3, 0, [15, 15, 15, 15, 15, 15, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),         #? P
    (0.6, 2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),                 #? N
    (0.8, 0, [15, 15, 15, 15, 15, 15, 15, 15, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]),   #? Melody
    (1.0, 0, [15, 15, 14, 14, 13, 13, 12, 12, 11, 11, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0])      #? Bass
]

GRAFFITIS = [
    (0, 0, 62, 47, 4, [1, 3, 7, 6]),
    (2, 48, 63, 33, 2, [6, 8, 9]),
    (0, 88, 87, 40, 3, [1, 5, 7, 11]),
    (0, 128, 81, 67, 5, [1, 2, 6, 9, 10, 11, 14]),
    (0, 200, 68, 49, 5, [0, 5, 9, 10, 14]),
    (88, 0, 73, 53, 4, [1, 3, 15])
]

class Graffiti:

    def __init__(self, health_multiplier:int):
        self.u, self.v, self.w, self.h, self.max_health, self.colors = random.choice(GRAFFITIS)
        self.x, self.y = random.randint(0, 228 - self.w), random.randint(0, 128 - self.h)
        self.max_health *= health_multiplier
        self.health = self.max_health
        self.health_multiplier = health_multiplier
        self.dither = 1

    def update(self, game):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.x <= pyxel.mouse_x <= self.x + self.w and self.y <= pyxel.mouse_y <= self.y + self.h and not game.clicked:
            self.health -= 1
            pyxel.play(0, 1)
            game.clicked = True
        
        if self.health <= 0:
            pyxel.play(1, 2)
            game.neon_timer = 20
            game.pyxel_manager.shake_camera(4, 0.2)
            for _ in range(30 * self.health_multiplier):
                x, y = random.randint(self.x, self.x + self.w), random.randint(self.y, self.y + self.h)
                dir_x, dir_y = random.choice([-1, 0, 1]), random.choice([-1, 0, 1])
                s = random.randint(1, 3)
                c = [random.choice(self.colors) for _ in range(5)]
                game.particle_manager.add_particle(RectangleParticle(x, y, s, s, c, 50, 2, x + dir_x, y + dir_y, acceleration_speed=-0.05, dither_duration=10))

        self.dither = self.health / self.max_health

    def draw(self):
        pyxel.dither(self.dither)
        pyxel.blt(self.x, self.y, 1, self.u, self.v, self.w, self.h, 0)
        pyxel.dither(1)

class Powerup:

    def __init__(self):
        self.u, self.v, self.w, self.h = (0, 56, 14, 13)
        self.x, self.y = random.randint(0, 228 - self.w), -self.h
        self.type = random.randint(1, 3)
        self.alive = True

    def update(self, game):
        self.y += 1

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.x <= pyxel.mouse_x <= self.x + self.w and self.y <= pyxel.mouse_y <= self.y + self.h:
            self.alive = False
            pyxel.play(0, 8)
            game.pyxel_manager.shake_camera(2, 0.1)
            game.psychedelic_timer = 20
            for _ in range(30):
                x, y = random.randint(self.x, self.x + self.w), random.randint(self.y, self.y + self.h)
                dir_x, dir_y = random.choice([-1, 0, 1]), random.choice([-1, 0, 1])
                s = random.randint(1, 2)
                c = [random.choice([6, 7, 9]) for _ in range(3)]
                game.particle_manager.add_particle(RectangleParticle(x, y, s, s, c, 50, 2, x + dir_x, y + dir_y, acceleration_speed=-0.05, dither_duration=10))

            if self.type == 1:
                for graffiti in game.graffitis:
                    graffiti.health = 0
            elif self.type == 2:
                game.paint_bar.current_value = game.paint_bar.max_value
            elif self.type == 3:
                game.score += 50

        if self.y > 128:
            self.alive = False

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.u, self.v, self.w, self.h, 0)

class Game:

    def __init__(self):
        #? Pyxel Configuration
        main_menu_scene = Scene(0, "Graffiti Cleanup Rush - Main Menu", self.update_main_menu, self.draw_main_menu, "assets.pyxres", PALETTE)
        credits_scene = Scene(1, "Graffiti Cleanup Rush - Credits", self.update_credits, self.draw_credits, "assets.pyxres", PALETTE)
        game_scene = Scene(2, "Graffiti Cleanup Rush - Game", self.update_game, self.draw_game, "assets.pyxres", PALETTE)
        lose_scene = Scene(3, "Graffiti Cleanup Rush - Lose", self.update_lose, self.draw_lose, "assets.pyxres", PALETTE)
        scenes = [main_menu_scene, credits_scene, game_scene, lose_scene]
        self.pyxel_manager = PyxelManager((228, 128), scenes, 0)

        #? Main Menu Variables
        self.main_menu_title = Text("Graffiti Cleanup\nRush", 114, 5, [7, 7, 7, 7, 7, 6, 6, 6, 6, 6], 2, ANCHOR_TOP, ROTATING_COLOR_MODE, 15, shadow=True, wavy=True)
        self.main_menu_play_button = Button("Play", 114, 60, 6, 7, 7, 6, 1, True, 7, anchor=ANCHOR_TOP, command=lambda:self.button_click(2))
        self.main_menu_credits_button = Button("Credits", 114, 80, 6, 7, 7, 6, 1, True, 7, anchor=ANCHOR_TOP, command=lambda:self.button_click(1))
        self.main_menu_quit_button = Button("Quit", 114, 100, 6, 7, 7, 6, 1, True, 7, anchor=ANCHOR_TOP, command=lambda:pyxel.quit())
        self.main_menu_sound_button = IconButton(2, 107, 6, 7, Sprite(0, 0, 72, 14, 14, 11), True, 7, anchor=ANCHOR_BOTTOM_LEFT, command=self.music)
        self.main_menu_mute_button = IconButton(2, 126, 6, 7, Sprite(0, 16, 72, 16, 14, 11), True, 7, anchor=ANCHOR_BOTTOM_LEFT, command=self.mute)

        #? Credits Variables
        self.credits_title = Text("Credits", 114, 5, [7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6], 2, ANCHOR_TOP, ROTATING_COLOR_MODE, 15, shadow=True)
        self.credits_text = Text("This game was created for the\nMini Jame Game #43.\nIt was made by Léo Imbert\nusing the pyxel module in python.\n\n\nThank's to Craftpix for\nthe graffiti designs.", 114, 30, 7, 1, ANCHOR_TOP, shadow=True)
        
        self.back_button = Button("Back", 2, 126, 6, 7, 7, 6, 1, True, 7, anchor=ANCHOR_BOTTOM_LEFT, command=lambda:self.button_click(0))

        #? Game Variables
        self.score_text = Text("Score : 0", 4, 5, [7] * 7 + [9] * 7, 1, shadow=True)
        self.score = 0
        self.highscore = 0
        self.clicked = False
        self.graffitis = []
        self.powerups = []
        self.neon_timer = 0
        self.psychedelic_timer = 0
        self.particle_manager = ParticleManager()
        self.paint_bar = UIBar(2, 100, 15, 55, 7, 13, 100, 100, horizontal=False, anchor=ANCHOR_BOTTOM_LEFT)

        #? Lose Variables
        self.lose_tite = Text("You lost !", 114, 5, [7] * 4 + [6] * 4, 2, ANCHOR_TOP, ROTATING_COLOR_MODE, 15, shadow=True)
        self.lose_text = Text("Your score is 0\nand your highscore is 0", 114, 60, 7, 1, ANCHOR_TOP, shadow=True)

        #? Start
        self.extend_audio()
        self.music()

        #? Manager Running
        self.pyxel_manager.run()

    def mute(self):
        pyxel.stop(2)
        pyxel.stop(3)

    def extend_audio(self):
        channels = []
        for gain, detune in EXTENDED_CHANNELS:
            channel = pyxel.Channel()
            channel.gain = gain
            channel.detune = detune
            channels.append(channel)
        pyxel.channels.from_list(channels)

        tones = []
        for gain, noise, waveform in EXTENDED_TONES:
            tone = pyxel.Tone()
            tone.gain = gain
            tone.noise = noise
            tone.waveform.from_list(waveform)
            tones.append(tone)
        pyxel.tones.from_list(tones)

    def music(self):
        pyxel.sounds[4].set(midi_notes_to_pyxel(pyxel.sounds[4].notes.to_list()), "4", "3", "vvvfnnnf", 30)
        pyxel.sounds[5].set(midi_notes_to_pyxel(pyxel.sounds[5].notes.to_list()), "5", "2", "f", 30)
        pyxel.musics[0].set([], [], [4], [5])
        pyxel.playm(0, loop=True)

    def reset(self):
        self.graffitis = []
        self.powerups = []
        self.score = 0
        self.score_text.text = "Score : 0"
        self.neon_timer = 0
        self.particle_manager.reset()
        self.paint_bar.current_value = self.paint_bar.max_value
        self.paint_bar.update()

    def button_click(self, new_scene:int):
        pyxel.play(0, 0)
        if new_scene == 2:
            self.pyxel_manager.change_scene_dither(new_scene, 0.1, 7, action=self.reset)
        else:
            self.pyxel_manager.change_scene_dither(new_scene, 0.1, 7, action=lambda:time.sleep(0.2))
        
    def graffiti_timer_progression(self, score:int)-> int:
        if score <= 200:
            return 120
        elif score <= 400:
            return 140
        elif score <= 600:
            return 120
        else:
            return 90
    
    def graffiti_health_progression(self, score:int)-> int:
        if score <= 100:
            return 1
        elif score <= 200:
            return 2
        elif score <= 400:
            return 3
        else:
            return 4

    def update_main_menu(self):
        self.main_menu_title.update()
        self.main_menu_play_button.update()
        self.main_menu_credits_button.update()
        self.main_menu_quit_button.update()
        self.main_menu_sound_button.update()
        self.main_menu_mute_button.update()

    def draw_main_menu(self):
        draw_brick_wall(0, 0, 228, 128, 8, 4, 1, 13, 1)
        pyxel.blt(20, 75, 1, 0, 88, 87, 40, 0)
        pyxel.blt(150, 30, 1, 2, 48, 63, 33, 0)

        self.main_menu_title.draw()
        self.main_menu_play_button.draw()
        self.main_menu_credits_button.draw()
        self.main_menu_quit_button.draw()
        self.main_menu_sound_button.draw()
        self.main_menu_mute_button.draw()

        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 8, 16, 16, 5)

    def update_credits(self):
        self.credits_title.update()
        self.credits_text.update()
        self.back_button.update()

    def draw_credits(self):
        draw_brick_wall(0, 0, 228, 128, 8, 4, 1, 13, 1)
        pyxel.blt(150, 80, 1, 88, 0, 73, 53, 0)
        pyxel.blt(10, -5, 1, 0, 0, 62, 47, 0)
        
        self.credits_title.draw()
        self.credits_text.draw()
        self.back_button.draw()

        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 8, 16, 16, 5)

    def update_game(self):
        if len(self.graffitis) > 10:
            if self.score > self.highscore:
                self.highscore = self.score
            self.lose_text.text = f"Your score is {self.score}\n and your highscore is {self.highscore}"
            pyxel.play(1, 3)
            self.pyxel_manager.change_scene_dither(3, 0.1, 7, action=lambda:time.sleep(0.2))
            return

        if pyxel.frame_count % self.graffiti_timer_progression(self.score) == 0:
            pyxel.play(1, 9)
            self.graffitis.append(Graffiti(self.graffiti_health_progression(self.score)))

        if pyxel.frame_count % 300 == 0 and random.random() <= 0.2:
            self.powerups.append(Powerup())

        if 205 <= pyxel.mouse_x <= 219 and 110 <= pyxel.mouse_y <= 115 and self.paint_bar.current_value < self.paint_bar.max_value:
            self.paint_bar.current_value += 0.5
            pyxel.play(0, 6)

        self.score_text.text = f"Score : {self.score}"
        self.score_text.update()
        self.paint_bar.update()
        self.back_button.update()
        self.particle_manager.update()

        if self.neon_timer > 0:
            self.neon_timer -= 1
            self.pyxel_manager.apply_palette_effect(neon_palette)
        if self.psychedelic_timer > 0:
            self.psychedelic_timer -= 1
            self.pyxel_manager.apply_palette_effect(psychedelic_shifting_palette)
        if self.neon_timer <= 0 and self.psychedelic_timer <= 0:
            self.pyxel_manager.reset_palette()

        for powerup in self.powerups:
            powerup.update(self)
        self.powerups = [powerup for powerup in self.powerups if powerup.alive]

        self.clicked = False
        if self.paint_bar.current_value > 0:
            for graffiti in self.graffitis[::-1]:
                graffiti.update(self)
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.play(0, 7)

        if self.clicked:
            self.paint_bar.current_value -= 1

        self.score += sum([graffiti.max_health for graffiti in self.graffitis if graffiti.health <= 0])
        self.graffitis = [graffiti for graffiti in self.graffitis if graffiti.health > 0]

    def draw_game(self):
        draw_brick_wall(0, 0, 228, 128, 8, 4, 1, 13, 1)

        for graffiti in self.graffitis:
            graffiti.draw()
        self.particle_manager.draw()

        for powerup in self.powerups:
            powerup.draw()

        rounded_rect(2, 2, 80, 16, 4, 6)
        rounded_rectb(2, 2, 80, 16, 4, 7)
        self.score_text.draw()
        self.paint_bar.draw()
        self.back_button.draw()

        pyxel.blt(202, 107, 0, 0, 32, 21, 23, 11)   #? Bucket

        if self.paint_bar.current_value > 0:
            pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 16, 8, 21, 21, 0)
        else:
            pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 40, 8, 21, 21, 0)

    def update_lose(self):
        self.lose_tite.update()
        self.lose_text.update()
        self.back_button.update()

    def draw_lose(self):
        draw_brick_wall(0, 0, 228, 128, 8, 4, 1, 13, 1)
        pyxel.blt(150, 10, 1, 0, 200, 68, 49, 0)
        pyxel.blt(-5, 70, 1, 0, 0, 62, 47, 0)

        self.lose_tite.draw()
        self.lose_text.draw()
        self.back_button.draw()

        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 8, 16, 16, 5)

if __name__ == "__main__":
    Game()