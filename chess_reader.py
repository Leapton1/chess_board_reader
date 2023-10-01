""" Converts a chess FEN string into speech """
import os
import time

import gtts
from playsound import playsound

START_POSITION = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
PIECES = {
    "r": "Rook",
    "b": "Bishop",
    "n": "Knight",
    "q": "Queen",
    "k": "King",
    "p": "Pawn",
}


def letter(num):
    """ name of file from file number """
    return "abcdefgh"[num - 1]


def phoneme(num):
    """ Make the letters sound right """
    return ["ay", "b", "c", "d", "e", "f", "g", "h"][num - 1]


def colour(character):
    """ Black pieces are lower case, white are upper """
    return "black" if character.islower() else "white"


def piece(character):
    """ Convert the letter to a speakable name """
    return PIECES[character.lower()]


def all_pieces():
    """ All possible letter codes for the pieces, both black and white. """
    return list(PIECES.keys()) + list(map(lambda x: x.upper(), PIECES.keys()))


def say(text):
    """ Output text as speech using Google service. """
    tts = gtts.gTTS(text)
    tts.save("./speech.mp3")
    playsound("./speech.mp3")
    os.remove("./speech.mp3")


def main(position):
    """ Currently just echoes out the start position. """
    coords = [1, 8]
    for character in position:
        if character == "/":
            coords[0] = 1
            coords[1] -= 1
        elif character in all_pieces():
            say(
                colour(character)
                + " "
                + piece(character)
                + " "
                + phoneme(coords[0])
                + " "
                + str(coords[1])
            )
            coords[0] += 1
        elif character.isdigit():
            coords[0] += int(character)
        time.sleep(1)


main(START_POSITION)
