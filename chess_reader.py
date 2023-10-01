""" Converts a chess FEN string into speech """
import os

import gtts
from playsound import playsound
from readchar import readchar

START_POSITION = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
PIECES = {
    "r": "Rook",
    "b": "Bishop",
    "n": "Knight",
    "q": "Queen",
    "k": "King",
    "p": "Pawn",
}


class Board():
    """ Stores the position of the pieces in the board. """

    def __init__(self):
        self.pieces = {}
        for piece in all_pieces():
            self.pieces[piece] = []

    def add(self, piece, rank, file):
        """ Set a piece on the board, e.g. ("r", 4, 1) """
        self.pieces[piece].append((rank, file,))

    def query(self, piece):
        """ Iterate through all pieces of that type. """
        for position in self.pieces[piece]:
            yield position


def letter(num):
    """ name of file from file number """
    return "abcdefgh"[num - 1]


def phoneme(num):
    """ Make the letters sound right """
    return ["ay", "b", "c", "d", "e", "f", "g", "h"][num - 1]


def colour(character):
    """ Black pieces are lower case, white are upper """
    return "black" if character.islower() else "white"


def piece_name(character):
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


def main(fen):
    """ Currently just echoes out the start position. """
    board = Board()
    coords = [1, 8]
    for character in fen:
        if character == "/":
            coords[0] = 1
            coords[1] -= 1
        elif character in all_pieces():
            board.add(character, coords[0], coords[1])
            coords[0] += 1
        elif character.isdigit():
            coords[0] += int(character)

    quitting = False
    print("".join(all_pieces()) + " to list piece position, or 'x' to exit")
    while not quitting:
        character = readchar()
        print(character)
        if character == 'x':
            quitting = True
        if character in all_pieces():
            for position in board.query(character):
                say(
                    colour(character)
                    + " "
                    + piece_name(character)
                    + " "
                    + phoneme(position[0])
                    + " "
                    + str(position[1])
                )


main(START_POSITION)
